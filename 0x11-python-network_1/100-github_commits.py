#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.
Usage: ./100-github_commits.py <repository name> <repository owner>
Python script that takes 2 arguments in order to solve this challenge:
-The first argument will be the repository name
-The second argument will be the owner name
-You must use the packages requests and sys
-You are not allowed to import packages other than requests and sys
-You don’t need to check arguments passed to the script (number or type)
Only 17% of applicants for a backend position at Holberton finished this task
in less than 15 minutes.
"""

import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    R = requests.get(url)
    commits = R.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
