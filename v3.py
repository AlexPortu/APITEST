import json
import requests
import ast
from v2 import datos_str

dic25 = {}


formated_dic = datos_str.replace('null', 'False')
formated_dic2 = formated_dic.replace('"', '\'')
formated_dic3 = formated_dic2.replace('true', 'True')
formated_dic4 = formated_dic3.replace('false', 'False')
formated_dic5 = ast.literal_eval(formated_dic4)
with open('v5.py', 'w', encoding='utf8') as f:
    f.write(formated_dic4)
x = formated_dic5['Products'][0]['Concepts'][0]['AvailableQuota']
y = formated_dic5['Products'][0]['Concepts'][0]['Concept']
z = formated_dic5['Products'][0]['Concepts'][0]['Details'][0]['Price']
m = formated_dic5['Products'][0]['Concepts'][0]['Details'][0]['OriginalPrice']
n = formated_dic5['Products'][0]['ProductCode']

dic25.update({'CUPO':x})
dic25.update({'CONCEPTO': y})
dic25.update({'PRECIO': z})
dic25.update({'PRECIO INICIAL': m})
dic25.update({'COD PRODUCTO': n})

print(dic25)

