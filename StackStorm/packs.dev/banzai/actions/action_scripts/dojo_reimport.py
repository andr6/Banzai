#!/usr/bin/python3

import sys
import os
import re

# import DefectDojo + StackStorm modules
from defectdojo_api import defectdojo
from st2actions.runners.pythonrunner import Action

# hardcoded info - change later for dynamic requests
#test_id = sys.argv[1]
#print("TEST ID = {}".format(test_id))
#test_id = int(test_id)

#host = 'http://172.18.0.8:8000'

# grab DefectDojo container IP
network_file = open("/opt/stackstorm/common/networks.txt", "r")
data = network_file.readlines()
DD_IP = ''
for line in data:
    if re.search('DD_IP', line):
        DD_IP = re.sub('DD_IP=', '', line)
DD_IP = DD_IP.replace('\n', '')
network_file.close()

# grab DefectDojo API Key
apikey_file = open("/opt/stackstorm/common/api_keys.txt", "r")
data = apikey_file.readlines()
api_key = ''
for line in data:
    if re.search('DD_APIKEY', line):
        api_key = re.sub('DD_APIKEY=', '', line)
api_key = api_key.replace('\n', '')
apikey_file.close()


host = "http://" + DD_IP + ":8000"
#api_key = 'ba1853066904cb2a99d44e9e8820fad5809156d5'
user = 'admin'

class Dojo_Import(Action):
    def run(self):
        # instantiate the DefectDojo api wrapper
        dd = defectdojo.DefectDojoAPI(host, api_key, user, debug=True)

        # perform upload request + print response
        upload_scan = dd.reupload_scan(1, "Nmap Scan", "/opt/stackstorm/scan_output/nmap_results.xml", "true", "2024/1/1", "API")
        print("Test number: {}".format(upload_scan))


