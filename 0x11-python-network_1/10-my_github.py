#!/usr/bin/python3
import sys
import requests
from sys import argv

from requests.models import to_key_val_list

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    github = "https://api.github.com/user"

    req = requests.get(url=github, auth=(username, password))
    print(req.json().get("id"))
