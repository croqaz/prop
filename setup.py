#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

NAME = 'prop'
DESCRIPTION = 'Library for parsing JSON lines.'
KEYWORDS = 'prop attr dot object dict list'
URL = 'https://github.com/croqaz/prop'
AUTHOR = 'Cristi Constantin'
EMAIL = 'cristi.constantin@speedpost.net'
REQUIRES_PYTHON = '>=3.6.0'

here = os.path.abspath(os.path.dirname(__file__))
about = {}

try:
    with open(os.path.join(here, 'README.md')) as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

with open(os.path.join(here, NAME, '__version__.py')) as f:
    exec(f.read(), about)

REQUIRED = []
# for line in open('requirements.txt'):
#     line = line.strip()
#     if line and line[0] != '#':
#         REQUIRED.append(line)

setup(
    version=about['__version__'],
    name=NAME,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=KEYWORDS,
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    license='MIT',
    packages=find_packages(exclude=['test', 'tests']),
    include_package_data=True,
    zip_safe=True,
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED,
    extras_require={
        'dev': ['flake8'],
        'test': ['pytest'],
    },
    classifiers=[
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
    ])
