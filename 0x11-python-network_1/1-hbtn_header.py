#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import sys
from urllib import request

if __name__ == "__main__":
    url = sys.argv[1]
    req = request.Request(url)
    with request.urlopen(req) as response:
        header = response.getheader("X-Request-Id")

    print(header)
