import atexit
import os
import platform
import shutil
import stat
import subprocess
import tempfile
import time
import zipfile
from pathlib import Path
from threading import Timer
from typing import Optional

import requests
from flask import Flask

__all__ = ["run_with_ngrok", "start_ngrok", "get_host"]

_ngrok_address = ""


def _get_command() -> str:
    system = platform.system()
    if system in ["Darwin", "Linux"]:
        command = "ngrok"
    elif system == "Windows":
        command = "ngrok.exe"
    else:
        raise Exception(f"{system} is not supported")
    return command


def get_host() -> str:
    return _ngrok_address


def _check_ngrok_available() -> bool:
    cmd = "where" if platform.system() == "Windows" else "which"
    try:
        res = subprocess.call([cmd, "ngrok"])
        return False if res else True  # subprocess will return 1 if not found otherwise 0
    except:
        print("Try installing ngrok")
        return False


def _run_ngrok(host: str, port: int, auth_token: Optional[str] = None) -> str:
    command = _get_command()
    if not _check_ngrok_available():
        ngrok_path = str(Path(tempfile.gettempdir(), "ngrok"))
        _download_ngrok(ngrok_path)
        executable = str(Path(ngrok_path, command))
        os.chmod(executable, stat.S_IEXEC)  # Make file executable for the current user.
    else:
        executable = "ngrok"

    if auth_token:
        os.system(f"{executable} authtoken {auth_token}")

    ngrok = subprocess.Popen([executable, "http", f"{host}:{port}"])
    atexit.register(ngrok.terminate)
    localhost_url = f"http://localhost:4040/api/tunnels"  # Url with tunnel details
    for _ in range(5):
        time.sleep(1)
        tunnels_data = requests.get(localhost_url).json()["tunnels"]
        if len(tunnels_data):
            return tunnels_data[0]["public_url"].replace("https", "http")

    raise ValueError("Not found ngrok tunnel public url after start")


def _download_ngrok(ngrok_path: str):
    if Path(ngrok_path).exists():
        return
    system = platform.system()
    if system == "Darwin":
        url = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-darwin-amd64.zip"
    elif system == "Windows":
        url = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip"
    elif system == "Linux":
        url = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip"
    else:
        raise Exception(f"{system} is not supported")
    download_path = _download_file(url)
    with zipfile.ZipFile(download_path, "r") as zip_ref:
        zip_ref.extractall(ngrok_path)


def _download_file(url: str) -> str:
    local_filename = url.split("/")[-1]
    r = requests.get(url, stream=True)
    download_path = str(Path(tempfile.gettempdir(), local_filename))
    with open(download_path, "wb") as f:
        shutil.copyfileobj(r.raw, f)
    return download_path


def start_ngrok(host: str, port: int, auth_token: Optional[str] = None):
    global _ngrok_address
    _ngrok_address = _run_ngrok(host, port, auth_token)
    print(f" * Running on {_ngrok_address}")
    print(f" * Traffic stats available on http://127.0.0.1:4040")
    requests.get(f"http://{host}:{port}/")


def run_with_ngrok(app: Flask, auth_token: Optional[str] = None):
    """
    The provided Flask app will be securely exposed to the public internet via ngrok when run,
    and the its ngrok address will be printed to stdout
    :param app: a Flask application object
    :param auth_token: ngrok authtoken if exists
    :return: None
    """
    old_run = app.run

    def new_run(*args, **kwargs):
        host = kwargs.get("host", "127.0.0.1")
        port = kwargs.get("port", 5000)
        thread = Timer(1, start_ngrok, args=(host, port, auth_token))
        thread.setDaemon(True)
        thread.start()
        old_run(*args, **kwargs)

    app.run = new_run


if __name__ == "__main__":
    print(_check_ngrok_available())
