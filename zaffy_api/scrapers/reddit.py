import urllib2
import json


def pull_reddit_listing(listing='popular'):
    """
    pull a listing of reddit
    """
    endpoint = "https://api.reddit.com/" + listing
    try:
        response = urllib2.urlopen(endpoint)
        data = json.load(response)
        print data
    except Exception as e:
        print e


if __name__ == '__main__':
    pull_reddit_listing()
