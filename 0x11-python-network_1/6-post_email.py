#!/usr/bin/python3
"""  sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8) """

import urllib.request
import urllib.parse
from urllib import parse
import requests
from sys import argv

if __name__ == "__main__":

    url = argv[1]
    email = argv[2]

    data = {"email": email}
    req = requests.post(url, data=data)
    print(req.text)
