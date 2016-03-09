#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages
from pip.req import parse_requirements

import pkg_resources

here = os.path.abspath(os.path.dirname(__file__))

pr_kwargs = {}
if pkg_resources.get_distribution("pip").version >= '6.0':
  pr_kwargs = {"session": False}

install_reqs = parse_requirements(
    os.path.join(
        here,
        './requirements.txt' if not sys.argv[1] in ['develop', 'test'] else './requirements-dev.txt'
    ), **pr_kwargs)

setup(
    name='discovery',
    version='0.1.0',
    author='Clever (https://clever.com)',
    author_email='tech-notify@clever.com',
    url='https://github.com/Clever/discovery-python/',
    packages=['discovery'],
    install_requires=[str(ir.req) for ir in install_reqs],
    setup_requires=['nose>=1.0'],
    test_suite='nose.collector',
    long_description="""\
    Programmatically find service endpoints.
    """
)
