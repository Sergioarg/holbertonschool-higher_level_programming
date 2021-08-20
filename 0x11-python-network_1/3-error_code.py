#!/usr/bin/python3
"""  sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8) """

import urllib.request
from sys import argv

if __name__ == "__main__":

    url = argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            page = response.read().decode("UTF-8")
            print(page)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
