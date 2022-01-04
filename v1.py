import requests
import json
import re
import time
from datetime import timedelta
from datetime import date
import ast
url = "http://pruebasapi.grandvalira.com/api/WebDataSession/Session?License=gvr04Rin&User=api&Password=j93nlv8fr&NoCache=0&Debug=0"
dic_1D = {}
dic_2D = {}
dic_3D = {}
dic_4D = {}
dic_5D = {}
dic_6D = {}
dic_7D = {}

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
rango = 15
def crear_json(rango, diccionario, dias):
  for i in range(rango):
    now = date.fromisoformat('2022-04-01')
    tomorrow = now + timedelta(days=i)
    tomorrow2 = now + timedelta(days=i+(dias-1))
    next_date = str(tomorrow)
    next_date2 =str(tomorrow2)
    payload2 = '{\r\n  \"IDSession\": %s,\r\n  \"StartDate\": \"%s",\r\n  \"EndDate\": \"%s",\r\n  \"IDServiceType\": 9,\r\n  \"IDClientType\": 1,\r\n  /*\"Occupations\": [\r\n      {\r\n          \"Type\": \"ADL\",\r\n          \"Age\": 35\r\n      },\r\n      {\r\n          \"Type\": \"ADL\",\r\n          \"Age\": 34\r\n      }\r\n  ]*/\r\n  //\"Products\": [45795],\r\n  //\"ProductTypes\": [34]\r\n}'%(IDSesion, next_date, next_date2)
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
    print(IDBusqueda)

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
    print(response3)

    dic25 = {}


    formated_dic = datos_str.replace('null', 'False')
    formated_dic2 = formated_dic.replace('"', '\'')
    formated_dic3 = formated_dic2.replace('true', 'True')
    formated_dic4 = formated_dic3.replace('false', 'False')
    formated_dic5 = ast.literal_eval(formated_dic4)
    with open('v5.py', 'w', encoding='utf8') as f:
        f.write(formated_dic4)
    x = formated_dic5['Products'][next((i for i, item in enumerate(formated_dic5['Products']) if item['ProductCode'] == f'{dias}OA'), None)]['Concepts'][0]['AvailableQuota']
    y = formated_dic5['Products'][next((i for i, item in enumerate(formated_dic5['Products']) if item['ProductCode'] == f'{dias}OA'), None)]['Concepts'][0]['Concept']
    z = formated_dic5['Products'][next((i for i, item in enumerate(formated_dic5['Products']) if item['ProductCode'] == f'{dias}OA'), None)]['Concepts'][0]['Details'][0]['Price']
    m = formated_dic5['Products'][next((i for i, item in enumerate(formated_dic5['Products']) if item['ProductCode'] == f'{dias}OA'), None)]['Concepts'][0]['Details'][0]['OriginalPrice']
    n = formated_dic5['Products'][next((i for i, item in enumerate(formated_dic5['Products']) if item['ProductCode'] == f'{dias}OA'), None)]['ProductCode']
    y1 = y.replace('Í', 'I')
    y2 = ''.join(y1)
    dic25.update({'CUPO':x})
    dic25.update({'CONCEPTO': y2})
    dic25.update({'PRECIO': z})
    dic25.update({'PRECIO INICIAL': m})
    dic25.update({'COD PRODUCTO': n})

    print(dic25)
    
    diccionario.update({next_date: dic25})
    dic25 = {}

  print(diccionario)
  with open(f'try_json_{dias}D.json', 'w', encoding='utf-8') as f:
    json.dump(diccionario, f, indent=4)

crear_json(rango=rango, diccionario=dic_1D, dias=1)
crear_json(rango=rango-1, diccionario=dic_2D, dias=2)
crear_json(rango=rango-2, diccionario=dic_3D, dias=3)
crear_json(rango=rango-3, diccionario=dic_4D, dias=4)
crear_json(rango=rango-4, diccionario=dic_5D, dias=5)
crear_json(rango=rango-5, diccionario=dic_6D, dias=6)
crear_json(rango=rango-6, diccionario=dic_7D, dias=7)
