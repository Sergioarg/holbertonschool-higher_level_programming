#!/usr/bin/python3
""" Module for use the GitHub API """
import json
import requests
from sys import argv

if __name__ == "__main__":
    """ Print the last 10 commits of one repo """
    repo = argv[1]
    user = argv[2]

    github = "https://api.github.com/repos/{}/{}/commits".format(repo, user)

    req = requests.get(github)

    for commit in req.json():
        sha = commit.get("sha")
        user = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, user))
