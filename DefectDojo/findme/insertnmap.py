import MySQLdb as db

# DefectDojo endpoint
HOST = "localhost"
PORT = 3306

# MySQL db credentials
USER = "root"
PASSWORD = "Cu3zehoh7eegoogohdoh1the"
DB = "dojodb"

try:
  # fetch new Test data
  connection = db.Connection(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB)
  dbhandler = connection.cursor()
  dbhandler.execute("INSERT INTO dojo_test_type VALUES (14, 'Nmap Scan');")
  connection.commit()

except Exception as e:
  print e

finally:
  connection.close()
