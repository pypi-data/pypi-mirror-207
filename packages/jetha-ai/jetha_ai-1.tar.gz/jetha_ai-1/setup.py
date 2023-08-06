from setuptools import setup, find_packages
import codecs
import os

VERSION = '1'
DESCRIPTION = 'all solutions'
LONG_DESCRIPTION = 'A package that allows to print all codes of ai lab.'

# Setting up
setup(
    name="jetha_ai",
    version=VERSION,
    author="jetha",
    author_email="jgada402@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)