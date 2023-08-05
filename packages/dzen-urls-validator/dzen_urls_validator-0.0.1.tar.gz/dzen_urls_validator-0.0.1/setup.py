import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

VERSION = '0.0.1'
DESCRIPTION = 'Validator for Dzen URLs.'

# Setting up
setup(
    name="dzen_urls_validator",
    version=VERSION,
    author="Emir Takhaviev",
    author_email="tah116emir@outlook.com",
    description=DESCRIPTION,
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Wiped-Out/dzen_urls_validator",
    download_url="https://github.com/Wiped-Out/dzen_urls_validator/releases/latest",
    packages=find_packages(exclude=["tests*"]),
    keywords=['python', 'dzen urls', 'validation'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
