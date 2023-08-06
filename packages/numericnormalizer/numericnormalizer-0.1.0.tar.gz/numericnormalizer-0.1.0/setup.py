from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.0'
DESCRIPTION = 'Converting number formats'
LONG_DESCRIPTION = 'This is a basic library used for NLP that can perform conversions between numbers in numerical format and alphabetical / character format.'

# Setting up
setup(
    name="numericnormalizer",
    version=VERSION,
    author="mattcoulter7 (Matt Coulter)",
    author_email="<mattcoul7@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'nlp', 'numeric', 'sentence', 'language', 'convert', 'regex'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)