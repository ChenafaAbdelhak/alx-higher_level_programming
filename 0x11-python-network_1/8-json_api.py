#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests

if __name__ == "__main__":
    
    url = "http://0.0.0.0:5000/search_user"
    try:
        q = argv[1]
    except IndexError:
        q = ""

    r = requests.post(url, data={"q": q})

    json_f = r.json()

    if json_f:
        print("[{}] {}".format(json_f.get("id"), json_f.get("name")))
    else:
        print("No result")
    except ValueError:
        print("Not a valid JSON")
