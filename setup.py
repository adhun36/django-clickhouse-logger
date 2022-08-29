import os
import sys
import setuptools

__author__ = 'Sobolev Andrey <email.asobolev@gmail.com>'
__version__ = '0.1.3'

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='django-clickhouse-logger',
    version=__version__,
    install_requires=['clickhouse-driver==0.2.4', 'shortuuid==1.0.9'],
    author='Sobolev Andrey',
    author_email='email.asobolev@gmail.com',
    description='Logging django errors to the clickhouse database with daily rotation.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url="https://github.com/Sobolev5/django-clickhouse-logger/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)