#!/usr/bin/python3

'''
IMPORT API TEST
'''

# import the package
from defectdojo_api import defectdojo
import requests
import json
import os
from datetime import datetime

print("\n--------------------- TESTING IMPORT API ------------------\n")

# header value for auth
header = {'content-type': 'application/json',
           'Authorization': 'ApiKey admin:4edd4e7927f1d8e37bfb2608465b47369409bc3d'}
           #'Authorization': 'ApiKey admin:9ae3f8e01d0ec94dc4155113da123890a78ce0d7'}

# importscan API
url_import = 'http://localhost:8000/api/v1/importscan/'

# XML file path
file = "output.xml"

complete_path = "/home/brian/Documents/Banzai/output.xml"
f = open(complete_path, 'r')
xml = f.read()
f.close()

print(xml)

date = datetime.now()

data = {
    'file': xml,
    'engagement': '/api/v1/engagements/1/',
    'scan_type': 'Nmap Scan',
    'active': 'true',
    'scan_date': "2017-11-30",
    'tags': ('', ''),
    'build_id': ('', 'API')
}

data = json.dumps(data)

# perform request
r = requests.post(url_import, headers=header, data=data)

print("RESPONSE = {}".format(r))
print("IMPORT API RESPONSE:\n {} : {}".format(r, r.text))