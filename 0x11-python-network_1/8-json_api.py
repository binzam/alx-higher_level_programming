#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    params = {"q": letter}
    response = requests.post(url, data=params)
    try:
        data = response.json()
        if data:
            user_name = data.get("name")
            user_id = data.get("id")
            print(f"[{user_id}] {user_name}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
