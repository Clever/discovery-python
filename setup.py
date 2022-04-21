#!/usr/bin/env python

from builtins import str
import os
import sys
from setuptools import setup, find_packages
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements
import pkg_resources

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'VERSION')) as f:
  VERSION = f.read().strip()

pr_kwargs = {"session": False}

install_reqs = parse_requirements(
    os.path.join(
        here,
        './requirements.txt' if not sys.argv[1] in ['develop', 'test'] else './requirements-dev.txt'
    ), **pr_kwargs)

setup(
    name='discovery',
    version=VERSION,
    author='Clever (https://clever.com)',
    author_email='tech-notify@clever.com',
    url='https://github.com/Clever/discovery-python/',
    packages=['discovery'],
    install_requires=[str(ir.requirement) for ir in install_reqs],
    setup_requires=['nose>=1.0'],
    test_suite='nose.collector',
    long_description="""\
    Programmatically find service endpoints.
    """
)
