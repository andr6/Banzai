import MySQLdb as db
import time

HOST = "localhost"
PORT = 3306
USER = "root"
PASSWORD = "Cu3zehoh7eegoogohdoh1the"
DB = "dojodb"

try:
  connection = db.Connection(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB)
    
  prev = 0

#  while 1:  
  
  dbhandler = connection.cursor()
  dbhandler.execute("SELECT T.id as testid, E.id as engagementid, TT.name as testname FROM dojo_test_type TT, dojo_engagement E, dojo_test T WHERE T.engagement_id = E.id and T.test_type_id = TT.id;")
  result = dbhandler.fetchall()

  #######################################################################
  #                                                                     #
  # Prev records the last recorded test ID, and will only run scans for #
  # tests with id that exceeds the last recorded id.                    #
  #                                                                     #
  #######################################################################

  for num in range(prev, len(result)):
    print result[num]
    prev = num+1
    
#  time.sleep(5)

except Exception as e:
  print e

finally:
  connection.close()
