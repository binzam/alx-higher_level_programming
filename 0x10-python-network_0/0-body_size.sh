#!/bin/bash
# script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response(in bytes)
url=$1
curl -s "$url" | wc -c
