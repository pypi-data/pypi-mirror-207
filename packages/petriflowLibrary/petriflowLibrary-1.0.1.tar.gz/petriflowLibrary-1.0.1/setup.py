# Always prefer setuptools over distutils
from setuptools import setup

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="petriflowLibrary",
    version="1.0.1",
    packages=["petriflow", "resources", "tests"],
    package_data={
        "resources": ["*.xml", "*.xsd"],
    },
    description="Import/Export library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Peter Kopecký",
    author_email="xkopecky@stuba.sk",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent"
    ],
    include_package_data=True,
    install_requires=[
        'setuptools~=65.6.3',
        'six~=1.16.0',
        'lxml~=4.9.1',
        'chardet~=5.1.0',
    ]
)
