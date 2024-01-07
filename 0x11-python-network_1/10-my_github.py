#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    auth = (username, password)
    url = "https://api.github.com/user"
    response = requests.get(url, auth=auth)
    user_id = response.json().get("id")
    print(user_id)
