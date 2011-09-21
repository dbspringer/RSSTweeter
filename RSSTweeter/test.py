#!/usr/bin/env python
'''Script to test RSSTweeter'''

__author__ = 'Derek Springer'
__author_email__ = 'derekspringer@gmail.com'
__version__ = '0.1.0'

'''
>>> from RSSTweeter import RSSTweeter
>>> tr = RSSTweeter()
>>> tr.hello()
'hello'

'''

if __name__ == '__main__':
    import doctest
    print "Starting test"
    doctest.testfile('test.py')
    doctest.testmod()
    print "done"

