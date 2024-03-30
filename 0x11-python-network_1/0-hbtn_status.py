#!/usr/bin/python3
"""
module that fetches a response from a url.
"""
from urllib import request


url = 'https://alx-intranet.hbtn.io/status'
with request.urlopen(url) as response:
    html = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode("utf-8")))
