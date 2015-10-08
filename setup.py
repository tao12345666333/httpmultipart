#!/usr/bin/env python

import os
import re
import sys
from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'httpmultipart',
]

requires = []

version = ''
with open('httpmultipart/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='httpmultipart',
    version=version,
    description='A httpmultipart post handler',
    long_description=readme + '\n\n',
    author='TaoBeier',
    author_email='zhangjintao9020@gmail.com',
    url='https://github.com/tao12345666333/httpmultipart',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'httpmultipart': 'httpmultipart'},
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    zip_safe=False,
    platforms='any',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
