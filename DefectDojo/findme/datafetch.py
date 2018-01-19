import MySQLdb as db
import time
import requests, json
import re
import os

# DefectDojo endpoint
HOST = "localhost"
PORT = 3306

# MySQL db credentials
USER = "root"
PASSWORD = "Cu3zehoh7eegoogohdoh1the"
DB = "dojodb"

# StackStorm ip and apikey
ip = None
key = None

# grab StackStorm container IP
network_file = open("/opt/django-DefectDojo/common/networks.txt", "r")
data = network_file.readlines()
for line in data:
  if re.search('SS_IP', line):
    ip = re.sub('SS_IP=', '', line)
ip = ip.replace("\n","")
network_file.close()

# grab StackStorm instance API_KEY
apikey_file = open("/opt/django-DefectDojo/common/api_keys.txt", "r")
data = apikey_file.readlines()
for line in data:
  if re.search('SS_APIKEY', line):
    key = re.sub('SS_APIKEY=', '', line)
key = key.replace("\n","")
apikey_file.close()

headers = {"St2-Api-Key": key, "Content-Type": "application/json"}

# include exception handling here if 'ip' or 'key' == None

try:
    
  prev = 0

  while 1:  
  
    connection = db.Connection(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB)
    dbhandler = connection.cursor()
    dbhandler.execute("SELECT T.id as testid, E.test_strategy as testurl, TT.name as testname FROM dojo_test_type TT, dojo_engagement E, dojo_test T WHERE T.engagement_id = E.id and T.test_type_id = TT.id;")
    result = dbhandler.fetchall()

    #########################################################################
    #                                                                       #
    # 'prev' records the last recorded test ID, and will only run scans for #
    # tests with id that exceeds the last recorded id.                      #
    #                                                                       #
    #########################################################################

    for num in range(prev, len(result)):
      testid = result[num][0]
      testid = str(testid)
      print("TEST ID = {}".format(testid))
      testurl = result[num][1]
      # remove http prefix - need implementation to remove https prefix too
      testname = result[num][2]
      prev = num+1

      # remove 'http://' if nmap scan
      if testname == 'Nmap Scan':
        print("Scan = Nmap Scan")
        testurl = re.sub(r"http://", "", testurl)
        trigger = 'banzaihook'
      # keep 'http://' for others
      elif testname == 'Burp Scan':
        print("Scan = Burp Scan")
        trigger = 'burphook'
      elif testname == 'Nessus Scan':
        print("Scan = Nessus Scan")
        trigger = 'nessushook'

      payload = {'testid': testid, 'url': testurl, 'scantype': testname}
      print("PAYLOAD = \n {}".format(payload))

      url = "https://" + ip + "/api/v1/webhooks/" + trigger
      r = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
      print(r.text)

      time.sleep(2)

    time.sleep(5)

except Exception as e:
  print e

finally:
  connection.close()
