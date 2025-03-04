#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and displays
 the value of the X-Request-Id variable found in the header of the response
"""
import sys
import urllib.request
url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    headers = response.headers

    if 'X-Request-Id' in headers:
        # Print the value of 'X-Request-Id'
        print(headers['X-Request-Id'])
    else:
        print("X-Request-Id not found in the response headers.")
