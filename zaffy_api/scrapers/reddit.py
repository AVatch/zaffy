import urllib2
import json


def isimg(link):
    ex = ['.png', '.jpg']
    for e in ex:
        if link[-4:] == e:
            return True

    if 'imgur' in link:
        return True

    return False


def get_data():
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
    reddit_data = get_data()
