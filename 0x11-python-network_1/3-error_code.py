#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""
from urllib.request import urlopen, Request
from urllib.error import HTTPError
import urllib.error
from sys import argv

if __name__ == "__main__":
    url: str = argv[1]
    req = Request(url)

    try:
        with urlopen(req) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
