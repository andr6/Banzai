#!/usr/bin/python3

'''
IMPORT SCAN RESULTS

This creates a new test in an existing engagement.
'''

# import the package
from defectdojo_api import defectdojo
import os
from datetime import datetime

# setup DefectDojo connection information
host = 'http://localhost:8000'
api_key = '69db82421964ed926d0d99e027d2f9f73120e1d9'
user = 'admin'

# instantiate the DefectDojo api wrapper
dd = defectdojo.DefectDojoAPI(host, api_key, user, debug=True)

upload_scan = dd.upload_scan(1, "Nmap Scan", "/home/brian/Documents/Banzai_Real/ddojo_api_test/output.xml", "true", "2017-11-30", "API")

print(upload_scan)
