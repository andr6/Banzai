#!/usr/bin/python3

# ----------------------------------------------------------------------------------------------
# Base DefectDojo API call example.
# Example taken off DefectDojo documentation, but edited to support Python 3 syntax and methods.
# Change code to add more API calls or features.
# ----------------------------------------------------------------------------------------------

import requests
import json

# ---------------------
# api/v1/users API test
# ---------------------

print("\n--------------------- TESTING USERS API ------------------\n")

# header value for auth
headers = {'content-type': 'application/json',
           'Authorization': 'ApiKey admin:9ae3f8e01d0ec94dc4155113da123890a78ce0d7'}

# api url (local instance)
url = 'http://127.0.0.1:8000/api/v1/users'

# request list of users in DefectDojo
r = requests.get(url, headers=headers, verify=True) # set verify to False if ssl cert is self-signed

users = r.json()

print(users)

for key, value in users.items():
        print(key)
        print(value)
