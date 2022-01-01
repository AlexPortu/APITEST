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
IDSesion = re.search(r'Identifier":(.\d+)', string1).group(1)

# POST NUMBER 2

url2 = "http://pruebasapi.grandvalira.com/api/WebDataSearch/Search"

payload2 = '{\r\n  \"IDSession\": %s,\r\n  \"StartDate\": \"2022-04-01\",\r\n  \"EndDate\": \"2022-04-01\",\r\n  \"IDServiceType\": 9,\r\n  \"IDClientType\": 1,\r\n  /*\"Occupations\": [\r\n      {\r\n          \"Type\": \"ADL\",\r\n          \"Age\": 35\r\n      },\r\n      {\r\n          \"Type\": \"ADL\",\r\n          \"Age\": 34\r\n      }\r\n  ]*/\r\n  //\"Products\": [45795],\r\n  //\"ProductTypes\": [34]\r\n}'%(IDSesion)
header2 = {
  'License': 'gvr04Rin',
  'User': 'api',
  'Password': 'j93nlv8fr',
  'NoCache': '0',
  'Debug': '0',
  'Content-Type': 'application/json'
}

response2 = requests.request("POST", url2, headers=header2, data=payload2)
IDBusqueda = re.search(r'Identifier":(.\d+)', response2.text).group(1)
