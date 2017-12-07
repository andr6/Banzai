#!/usr/bin/python3

'''
IMPORT API TEST
'''

# import the package
from defectdojo_api import defectdojo
import os
from datetime import datetime

# setup DefectDojo connection information
host = 'http://localhost:8000'
api_key = '4edd4e7927f1d8e37bfb2608465b47369409bc3d'
user = 'admin'

# instantiate the DefectDojo api wrapper
dd = defectdojo.DefectDojoAPI(host, api_key, user, debug=True)

upload_scan = dd.upload_scan(1, "Nmap Scan", "/home/brian/Documents/Banzai/output.xml", "true", "2017-11-30", "API")

print(upload_scan)