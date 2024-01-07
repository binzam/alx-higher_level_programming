#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""
import requests
import sys


def list_commits(repo, owner):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    repo = sys.argv[1]
    owner = sys.argv[2]
    list_commits(repo, owner)
