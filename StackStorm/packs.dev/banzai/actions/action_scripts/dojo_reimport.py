#!/usr/bin/python3

import sys
import os

# import DefectDojo + StackStorm modules
from defectdojo_api import defectdojo
from st2actions.runners.pythonrunner import Action

# hardcoded info - change later for dynamic requests
host = 'http://172.21.0.3:8000'
api_key = 'a41360c47b7a459c16ecff6665475681b7b58c9d'
user = 'admin'

class Dojo_Import(Action):
    def run(self):
        # instantiate the DefectDojo api wrapper
        dd = defectdojo.DefectDojoAPI(host, api_key, user, debug=True)

        # perform upload request + print response
        upload_scan = dd.reupload_scan(7, "Nmap Scan", "/opt/stackstorm/scan_output/nmap_results.xml", "true", "2024/1/1", "API")
        print("Test number: {}".format(upload_scan))


