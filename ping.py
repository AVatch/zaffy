import urllib2
import json
import time

token = "71e3dfdb47579116e5f0eef477b05cc6147d616a"
domain = "http://52.0.238.94/"


def ping():
    endpoint = domain + "api/v1/gen/zaffy/"

    request = urllib2.Request(endpoint, headers={"Authorization": "Token " + token})
    urllib2.urlopen(request).read()


if __name__ == '__main__':
    while True:
        ping()
        time.sleep(300)
