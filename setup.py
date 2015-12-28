#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

README_FILE = open('README.rst')
try:
    long_description = README_FILE.read()
finally:
    README_FILE.close()

packages = (
    'tagtools',
)

setup(
    name='django-tag-tools',
    version='0.2.0',
    packages=('tagtools',),
    include_package_data=True,
    zip_safe=False,
    platforms=['any'],
    description='Tag cloud for django-taggit.',
    author_email='kaleissin@gmail.com',
    author='kaleissin',
    long_description=long_description,
    url='https://github.com/kaleissin/django-tag-tools',
    classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Topic :: Software Development :: Libraries :: Application Frameworks',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Framework :: Django :: 1.8',
            'Framework :: Django :: 1.9',
    ]
)
