from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.2'
DESCRIPTION = 'chatbot'
LONG_DESCRIPTION = 'Just a chatbot'

# Setting up
setup(
    name="ZephyrusChatbot",
    version=VERSION,
    author="RGB_CATT",
    author_email="",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'chat', 'bot', 'chatbot'],
    classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
])
