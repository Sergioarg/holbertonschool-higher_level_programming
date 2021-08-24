#!/usr/bin/python3
""" Module for use the GitHub API """

import requests
from sys import argv

if __name__ == "__main__":
    """ Print the last 10 commits of one repo """
    repo = argv[1]
    user = argv[2]

    github = "https://api.github.com/repos/{}/{}/commits?per_page=10".format(
        user, repo)

    req = requests.get(url=github)

    for commit in req.json():
        sha = commit.get("sha")
        usr = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, usr))
