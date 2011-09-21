#!/usr/bin/env python
'''A library that provides a python interface to the Twitter API for RSS feeds'''

__author__ = 'Derek Springer'
__author_email__ = 'derekspringer@gmail.com'
__version__ = '0.1.0'

class RSSTweeter:
    '''
    A simple tool to read an RSS feed and post any new entries to a twitter feed.
    '''
    def __init__(self,
                 rss_feeds=[],
                 consumer_key=None,
                 consumer_secret=None,
                 access_token_key=None,
                 access_token_secret=None,
                 sqlite_db='last_checked.db'):
        '''Instantiate a new RSSTweeter object.
            Args:
                rss_feeds:
                    A list containing the full URL(s) to the rss feed(s)
                    you want to parse
                consumer_key:
                    Your Twitter user's consumer_key.
                consumer_secret:
                    Your Twitter user's consumer_secret.
                access_token_key:
                    The oAuth access token key value you retrieved
                    from running get_access_token.py.
                access_token_secret:
                    The oAuth access token's secret, also retrieved
                    from the get_access_token.py run.
        '''
    
    def hello(self):
        return 'hello'

