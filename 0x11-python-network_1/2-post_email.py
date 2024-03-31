#!/usr/bin/python3
"""
script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from urllib import parse, request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    data = parse.urlencode({"email": email})
    data = data.encode("utf-8")
    req = request.Request(url, data=data)
    with request.urlopen(req) as response:
        page = response.read()

    print(page.decode("utf-8"))
