import requests
import json

from v1 import IDBusqueda, IDSesion

url3 = "http://pruebasapi.grandvalira.com/api/WebDataAvailability/Availability"

payload3 = '{\r\n    \"IDSession\": %s,\r\n    \"IDSearch\": %s,\r\n    \"ReturnImages\": false,\r\n    \"ReturnAlternativeAvailabilities\": true,\r\n    \"Filters\": {\r\n        /*\"IDProduct\": [45788]\r\n        \"IDCities\": [8323],\r\n        \"IDProductTypes\": [34],\r\n        \"IDProductSubtypes\": []*/\r\n    }\r\n}' %(IDSesion, IDBusqueda)
headers3 = {
  'License': 'gvr04Rin',
  'User': 'api',
  'Password': 'j93nlv8fr',
  'NoCache': '0',
  'Debug': '0',
  'Content-Type': 'application/json'
}

response3 = requests.request("POST", url3, headers=headers3, data=payload3)
datos_str = response3.text
print(datos_str)
