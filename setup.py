#!/usr/bin/env python

from builtins import str
import os
import sys
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'VERSION')) as f:
  VERSION = f.read().strip()

# Read requirements without using pip internals
def read_requirements(filename):
    with open(os.path.join(here, filename)) as f:
        return [line.strip() for line in f
                if line.strip() and not line.startswith('#') and not line.startswith('-r')]

install_reqs = read_requirements(
    './requirements.txt' if not sys.argv[1] in ['develop', 'test'] else './requirements-dev.txt'
)

setup(
    name='discovery',
    version=VERSION,
    author='Clever (https://clever.com)',
    author_email='tech-notify@clever.com',
    url='https://github.com/Clever/discovery-python/',
    packages=['discovery'],
    install_requires=install_reqs,
    setup_requires=['nose>=1.0'],
    test_suite='nose.collector',
    long_description="""\
    Programmatically find service endpoints.
    """
)
