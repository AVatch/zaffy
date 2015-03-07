import urllib2
import json


def pull_reddit_listing(listing='popular'):
    """
    pull a listing of reddit
    """
    endpoint = "https://api.reddit.com/subreddits/" + listing
    try:
        response = urllib2.urlopen(endpoint)
        data = json.load(response)
        print data
    except Exception as e:
        print e


def isimg(link):
    ex = ['.png', '.jpg']
    for e in ex:
        if link[-4:] == e:
            return True

    if 'imgur' in link:
        return True

    return False


def twitter():
    pass


def reddit():
    pairs = []

    try:
        page = urllib2.urlopen('http://www.reddit.com/r/all/top.json?limit=10')
        data = json.load(page)

        for d in data['data']['children']:
            title = d['data']['title']
            link = d['data']['url']
            img = link if isimg(link) else None
            pairs.append((title, img))

        return pairs

    except:
        return None

if __name__ == '__main__':
    reddit_data = reddit()
