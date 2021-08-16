import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json/'

response = urlopen(url)

data = json.loads(response)

ip = data['ip']
org = org = data['org']
cid = data['city']
pais = data['country']
regiao = data['region']

print("Detalhes do IP externo")
print("IP: {4}\nRegiao: {1}\nPais: {2}\nCidade: {3}\nOrg: {0}".format(org,regiao, pais, cid, ip))
