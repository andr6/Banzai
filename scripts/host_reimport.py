#!/usr/bin/python3

'''
RE-IMPORT SCAN RESULTS

Re-upload scan results into an existing test.
'''

# import the package
from defectdojo_api import defectdojo
import os
from datetime import datetime

# setup DefectDojo connection information
host = 'http://localhost:8000'
api_key = '69db82421964ed926d0d99e027d2f9f73120e1d9'
user = 'admin'

# instantiate DefectDojo api wrapper and perform api call
dd = defectdojo.DefectDojoAPI(host, api_key, user, debug=True)
upload_scan = dd.reupload_scan(39, "Nmap Scan", "/home/brian/Documents/Banzai_Real/ddojo_api_test/output.xml", "true", "2020/10/10")

print(upload_scan)
