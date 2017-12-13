import requests

url = "http://172.18.0.5/api/v1/webhooks/" 
key = "NWNjMDc2ODVlM2RlMmUxZWY5NjZlNGYzMGI2ZTdjMDdiNDZjYWQ5NWQxZWRmOWQ2NzU0Nzk4N2JkMmExODYzYg"
headers = {'St2-Api-Key': key, 'Content-Type': 'application/json'}

#payload = {}

response = requests.get(url, headers=headers, verify=False)
print(response.content)
