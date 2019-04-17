# -*- coding: utf-8 -*-

import setuptools

from compress import __version__

with open("README.md", "r") as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    requires = f.readlines()

setuptools.setup(
    name='compress',
    version=__version__,
    description='Compress data help for big data & unbalanced data classification.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Zeroto521',
    author_email='Zeroto521@gmail.com',
    maintainer='Zeroto521',
    maintainer_email='Zeroto521@gmail.com',
    license="MIT",
    py_modules=['compress'],
    requires=requires,
    url='https://github.com/Zeroto521/compress',
    download_url='https://github.com/Zeroto521/compress/archive/master.zip',
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    platforms=['linux', 'windows', 'macos'],
    keywords=[
        'machine learning',
        'big data',
        'data processing',
        'data compression'
    ]
)
