import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flask-ngrok3",
    version="0.3.0",
    author="Partycode",
    description="A successor to flask-ngrok and flask-ngrok2 for demo Flask apps using ngrok.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Partycode/flask-ngrok3",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    keywords='flask ngrok demo',
    install_requires=['Flask>=0.8', 'requests'],
    py_modules=['flask_ngrok3']
)
