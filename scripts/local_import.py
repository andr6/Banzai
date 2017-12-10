#!/usr/bin/python3

'''
IMPORT API TEST
'''

# import the package
from defectdojo_api import defectdojo
import os
from datetime import datetime

# setup DefectDojo connection information
host = 'https://defectdojo.pythonanywhere.com'
api_key = 'e847e71262fbc1398b9cc086b03c11c192f89e8d'
user = 'admin'

# instantiate the DefectDojo api wrapper
dd = defectdojo.DefectDojoAPI(host, api_key, user, debug=True)

upload_scan = dd.upload_scan(7, "Nmap Scan", "/home/brian/Documents/Banzai_Real/ddojo_api_test/output.xml", "true", "2017-12-12", "API")

print(upload_scan)
