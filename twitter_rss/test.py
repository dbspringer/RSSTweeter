#!/usr/bin/env python
'''Script to test twitter_rss'''

__author__ = 'Derek Springer'
__author_email__ = 'derekspringer@gmail.com'
__version__ = '0.1.0'

'''
>>> from twitter_rss import TwitterRSS
>>> tr = TwitterRSS()
>>> tr.hello()
'hello'

'''

if __name__ == '__main__':
    import doctest
    doctest.testfile('test.py')
    doctest.testmod()
