#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and
displays the body of the response. """

import requests
from sys import argv

if __name__ == "__main__":

    url = "http://0.0.0.0:5000/search_user"

    # First get the page
    if len(argv) > 1:
        query = argv[1]
    else:
        query = ''

    data = {'q': query}

    req = requests.post(url=url, data=data)

    try:
        # Request to JSON file
        req_json = req.json()

        if len(req_json) == 0:
            print("No result")
        else:
            print("[{}] {}".format(req_json.get('id'), req_json.get('name')))

    except:
        print("Not a valid JSON")
