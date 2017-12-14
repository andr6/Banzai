import MySQLdb as db
import time
import requests, json
import re

HOST = "localhost"
PORT = 3306
USER = "root"
PASSWORD = "Cu3zehoh7eegoogohdoh1the"
DB = "dojodb"

url = "https://172.21.0.5/api/v1/webhooks/banzaihook"
key = "M2EwOTg1NWFiZDc4ODUyODgxNDk5NDQzYTRiZGIxMzNiOTUwMmNjYmI1YTJmNjRiOTc0YzdmYjZlZDAwMGJkNA"
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
