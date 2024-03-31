#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

r = requests.get('https://alx-intranet.hbtn.io/status')

print("Body responses:")
print("\t- type: {}".format(type(r.testx())))
print("\t- content: {}".format(r.text))

