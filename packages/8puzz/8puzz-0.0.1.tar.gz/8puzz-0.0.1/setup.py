from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = '8_puzzle_problem'
LONG_DESCRIPTION = 'A package that allows to print 8 puzzle code.'

# Setting up
setup(
    name="8puzz",
    version=VERSION,
    author="yuvraj",
    author_email="yuvrajdevnani03@gmail.com",
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