import MySQLdb as db
import time
import requests, json
import re
import os

HOST = "localhost"
PORT = 3306
USER = "root"
PASSWORD = "Cu3zehoh7eegoogohdoh1the"
DB = "dojodb"

# grab StackStorm container IP
network_file = open("/opt/django-DefectDojo/common/networks.txt", "r")
data = network_file.readlines()
ip = ''
for line in data:
  if re.search('SS_IP', line):
    ip = re.sub('SS_IP=', '', line)
ip = ip.replace("\n","")
network_file.close()

# grab StackStorm instance API_KEY
apikey_file = open("/opt/django-DefectDojo/common/api_keys.txt", "r")
data = apikey_file.readlines()
key = ''
for line in data:
  if re.search('SS_APIKEY', line):
    key = re.sub('SS_APIKEY=', '', line)
key = key.replace("\n","")
apikey_file.close()

url = "https://" + ip + "/api/v1/webhooks/banzaihook"
#key = "YWEwY2ViMzE3MWQ1NzUyMDMxODIyMDZlOGMxZWEzZGZiODhiN2Y1M2RjNTIzZjE0MzViMjMwYTczMjNkYTRmYQ"
headers = {"St2-Api-Key": key, "Content-Type": "application/json"}

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
      testurl = result[num][1]
      testurl = re.sub(r"http://", "", testurl)
      testname = result[num][2]
      prev = num+1
      print(testurl)

      payload = {'testid': testid, 'url': testurl}

      r = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
      print(r.text)

      time.sleep(2)

    time.sleep(5)

except Exception as e:
  print e

finally:
  connection.close()
