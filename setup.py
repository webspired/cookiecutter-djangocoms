#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Our version ALWAYS matches the version of Django cms we support
# If Django CMS has a new release, we branch, tag, then update this setting after the tag.
version = '3.4.1'

if sys.argv[-1] == 'tag':
    os.system('git tag -a %s -m "version %s"' % (version, version))
    os.system('git push --tags')
    sys.exit()

with open('README.rst') as readme_file:
    long_description = readme_file.read()

setup(
    name='cookiecutter-djangocms',
    version=version,
    description='A Cookiecutter template for creating production-ready Django CMS projects quickly.',
    long_description=long_description,
    author='Juergen Schackmann',
    author_email='juergen.schackmann@webspired.com',
    url='https://github.com/webspired/cookiecutter-djangocms',
    packages=[],
    license='BSD',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
    keywords=(
        'cookiecutter, Python, projects, project templates, django, '
        'skeleton, scaffolding, project directory, setup.py'
    ),
)
