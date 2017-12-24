import sys
import re

# grab DefectDojo container IP
network_file = open("/opt/stackstorm/common/networks.txt", "r")
data = network_file.readlines()

DD_IP = ''
for line in data:
    if re.search('DD_IP', line):
        DD_IP = re.sub('DD_IP=', '', line)
DD_IP = DD_IP.replace('\n', '')
network_file.close()

print(DD_IP)

# grab DefectDojo API Key
apikey_file = open("/opt/stackstorm/common/api_keys.txt", "r")
data = apikey_file.readlines()
api_key = ''
for line in data:
    if re.search('DD_APIKEY', line):
        api_key = re.sub('DD_APIKEY=', '', line)
api_key = api_key.replace('\n', '')
apikey_file.close()

print(api_key)
