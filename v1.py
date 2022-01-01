import requests
import json
import re

url = "http://pruebasapi.grandvalira.com/api/WebDataSession/Session?License=gvr04Rin&User=api&Password=j93nlv8fr&NoCache=0&Debug=0"

payload = json.dumps({
  "IDLanguage": 1,
  "IDCurrency": 1,
  "IDSalesChannel": 21
})
headers = {
  'License': 'gvr04Rin',
  'User': 'api',
  'Password': 'j93nlv8fr',
  'NoCache': '0',
  'Debug': '0',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)
string1 = response.text
string2 = re.search(r'Identifier":(.\d+)', string1).group(1)

