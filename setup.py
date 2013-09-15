#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

README_FILE = open('README.txt')
try:
    long_description = README_FILE.read()
finally:
    README_FILE.close()

packages = (
        'tagtools',
        'tagtools.backends',
        'tagtools.backends.taggit',
        'tagtools.backends.tagging',
)

setup(name='django-tag-tools',
        version='0.1.1',
        packages=('tagtools',),
        include_package_data=True,
        zip_safe=False,
        platforms=['any'],
        description='Tag cloud for django tagging and django-taggit.',
        author_email='kaleissin@gmail.com',
        author='kaleissin',
        long_description=long_description,
        url='https://github.com/kaleissin/django-tag-tools',
        classifiers=[
                'Development Status :: 4 - Beta',
                'Environment :: Web Environment',
                'Framework :: Django',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: MIT License',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Topic :: Software Development :: Libraries :: Application Frameworks',
                'Topic :: Software Development :: Libraries :: Python Modules',
        ]
)
