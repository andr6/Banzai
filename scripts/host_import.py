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
api_key = 'd5300ae832fd73e64b9ca1697a91ff63ef917dd1'
user = 'admin'

# instantiate the DefectDojo api wrapper
dd = defectdojo.DefectDojoAPI(host, api_key, user, debug=True)

upload_scan = dd.upload_scan(1, "Nmap Scan", "/home/brian/Documents/Banzai_Real/ddojo_api_test/output.xml", "true", "2017-11-30", "API")

print(upload_scan)
