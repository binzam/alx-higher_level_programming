#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status
using the requests package"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    body = response.text
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
