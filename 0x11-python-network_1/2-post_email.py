#!/usr/bin/python3
"""  sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8) """

import urllib.request
import urllib.parse
from urllib import parse
from sys import argv

if __name__ == "__main__":

    url = argv[1]
    email = argv[2]

    data = {"email": email}
    data = parse.urlencode(data).encode()
    req = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(req) as response:
        html = response.read().decode("UTF-8")
        print(html)
