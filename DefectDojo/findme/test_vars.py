import re
import sys

# grab StackStorm container IP
network_file = open("/opt/django-DefectDojo/common/networks.txt", "r")
data = network_file.readlines()
ip = ''
for line in data:
  if re.search('SS_IP', line):
    ip = re.sub('SS_IP=', '', line)
ip = ip.replace("\n", "")
network_file.close()

print(ip)

# grab StackStorm instance API_KEY
apikey_file = open("/opt/django-DefectDojo/common/api_keys.txt", "r")
data = apikey_file.readlines()
key = ''
for line in data:
  if re.search('SS_APIKEY', line):
    key = re.sub('SS_APIKEY=', '', line)
key = key.replace("\n", "")
apikey_file.close()

print(key)
