import random
import re
import sys
import urllib2


def pick_img(word):
    page = urllib2.urlopen('http://imgur.com/search?q={}'.format(word))
    rawdata = page.read()

    urlpattern = r'\/\/i\.imgur\.com\/([a-zA-Z0-9]*)\.jpg'
    sublinks = re.findall(urlpattern, rawdata)
    links = ['http://i.imgur.com/{}.jpg'.format(s[:-1]) for s in sublinks]
    return random.choice(links)


if __name__ == '__main__':
    print pick_img(sys.argv[1])
