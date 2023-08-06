from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "a test"
LONG_DESCRIPTION = "a test but long"

# Setting up
setup(
    name="guimplOUI",
    version=VERSION,
    author="testGUIMPL",
    author_email="testmail@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["matplotlib"],
    keywords=["python", "video", "stream", "video stream", "camera stream", "sockets"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
