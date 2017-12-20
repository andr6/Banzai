#!/usr/bin/python3

import sys
import os

# import DefectDojo + StackStorm modules
from defectdojo_api import defectdojo
from st2actions.runners.pythonrunner import Action

# hardcoded info - change later for dynamic requests
#test_id = sys.argv[1]
#print("TEST ID = {}".format(test_id))
#test_id = int(test_id)

host = 'http://172.18.0.8:8000'
api_key = '721d5ba4622e04958da1e673608344a5ae72a29a'
user = 'admin'

class Dojo_Import(Action):
    def run(self):
        # instantiate the DefectDojo api wrapper
        dd = defectdojo.DefectDojoAPI(host, api_key, user, debug=True)

        # perform upload request + print response
        upload_scan = dd.reupload_scan(1, "Nmap Scan", "/opt/stackstorm/scan_output/nmap_results.xml", "true", "2024/1/1", "API")
        print("Test number: {}".format(upload_scan))


