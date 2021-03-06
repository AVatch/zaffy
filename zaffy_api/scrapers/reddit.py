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
        for s in ['all', 'news']:
            page = urllib2.urlopen(
                'http://www.reddit.com/r/{}/top.json?limit=20'.format(s))
            data = json.load(page)

            for d in data['data']['children']:
                title = d['data']['title']
                link = d['data']['url']
                img = link if isimg(link) else None
                pairs.append((title, img))

        pairs = [map(lambda x: x.encode('ascii', 'ignore') if x else None, p)
                 for p in pairs]
        return pairs

    except Exception as e:
        print e
        return None

if __name__ == '__main__':
    reddit_data = get_data()
