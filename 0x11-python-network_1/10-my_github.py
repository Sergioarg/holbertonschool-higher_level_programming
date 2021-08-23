#!/usr/bin/python3
""" Module for use the GitHub API """
import requests
from sys import argv


if __name__ == "__main__":
    """ Takes your GitHub credentials (username and password) and
    uses the GitHub API to display your id """
    username = argv[1]
    password = argv[2]
    github = "https://api.github.com/user"

    req = requests.get(url=github, auth=(username, password))
    print(req.json().get("id"))
