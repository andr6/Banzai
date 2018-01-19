import requests
import json
import time
import sys

# stackstorm action runner module
from st2actions.runners.pythonrunner import Action

#### SCAN INFORMATION NEEDED
# authenticated to pwc admin
accessKey = "2174eecd9114dccdbdb68ea5fbcc3c3c5d7945fc04686de1bfa60d234a300680"
secretKey = "f1f907b62b28043dc691e1b04ad8243aaf36cec1444306423c6f6ac8ca04dc78"
# Policy template uuid and id - Basic Network Scan
uuid = "731a8e52-3ea6-a291-ec0a-d2ff0619c19d7bd788d6be818b65"
policy_id = 28
# Default Banzai folder ID to store all scans
folder_id = 27

class Nessus_Scan(Action):
    #### POST to API
    def post_request(url, payload):
      r = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
      return r.text

    #### GET from API
    def get_request(url, payload):
      r = requests.get(url, headers=headers, data=json.dumps(payload), verify=False)
      return r.text

    #### GET scan details
    def get_scan_details():
      res = get_request(url+"scans/"+str(scan_id), '')
      scan = json.loads(res)
      return scan['history'][0]['status'], scan['history'][0]['history_id']

    #### GET report status
    def get_report_status(file_id):
      res = get_request(url+"scans/"+str(scan_id)+"/export/"+str(file_id)+"/status", '')
      status = json.loads(res)
      return status["status"]

    def run(self, url, testid):
      text_targets = url              # Target of scan
      dd_id = testid                     # Name of scan - Defect Dojo ID

      #### Nessus information for API request
      url = "https://10.142.120.140:8834/"                      # link to Nessus API
      headers = {"X-ApiKeys": "accessKey=" + accessKey + ";secretKey="+ secretKey,"Content-Type": "application/json"}

      #### MAIN FLOW
      # (1) Create a new scan & obtain scan_id
      new_scan = { "uuid": uuid, "settings": { "name": str(dd_id), "text_targets": text_targets, "policy_id": policy_id, "folder_id": folder_id } }
      res = post_request(url+"scans", new_scan)               # fetch scan creation details
      scan = json.loads(res)                                  # fetch scan id for (2)
      scan_id = scan['scan']['id']
      print scan_id

      # (2) Launch the scan created from (1)
      post_request(url+"scans/"+str(scan_id)+"/launch", '')

      # (3) Fetch scan details & obtain status + history_id
      status, history_id = get_scan_details()
      while status == 'running':
        print ('scan not ready')
        time.sleep(30)
        status, history_id = get_scan_details()
      print status
      print history_id

      # (4) Request report
      res = post_request(url+"scans/"+str(scan_id)+"/export?history_id="+str(history_id), {"format": "nessus"})
      scan = json.loads(res)
      print scan
      file_number = scan["file"]
      print file_number

      # (5) Get report status
      status = get_report_status(file_number)
      while status == 'loading':
        print ('report not ready')
        print status
        time.sleep(30)
        status = get_report_status(file_number)
      print status

      # (6) Export report
      f = open('opt/stackstorm/scan_results/nessus/nessus_scan.xml', 'w+')
      xml = get_request(url+"scans/"+str(scan_id)+"/export/"+str(file_number)+"/download", '')
      f.write(xml)
      f.close
