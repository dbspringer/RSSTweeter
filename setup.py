#!/usr/bin/env python
from setuptools import setup, find_packages

__author__ = 'Derek Springer'
__version__= '0.1.0'
 
LONG_DESCRIPTION = '''
RSSTweeter
==================

This is a simple tool to read an RSS feed and post any new entries to a 
twitter feed.

Dependencies
------------
* [feedparser](http://www.feedparser.org/)
* [python-twitter](http://code.google.com/p/python-twitter/)
* [simplejson](http://pypi.python.org/pypi/simplejson/)
* [oauth2](http://pypi.python.org/pypi/oauth2)
* [httplib2](http://code.google.com/p/httplib2/)

Installing twitter-rss
-----------------------------

1.  download the source and run 

       'python setup.py install'
'''
 
setup(
    name='RSSTweeter',
    author=__author__ ,
    author_email='derekspringer@gmail.com',
    url='http://github.com/dbspringer/RSSTweeter',
    version=__version__,
    description='A simple tool to read an RSS feed and post any new entries to a twitter feed.',
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Environment :: Web Environment',
    ],
    keywords='twitter,rss',
    license='BSD',
    packages=find_packages(),
    install_requires=[
        'setuptools',
        'feedparser',
        'python-twitter',
        'simplejson',
        'oauth2',
        'httplib2'],
    include_package_data=True,
)

