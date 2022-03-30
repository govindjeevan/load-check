import requests
from requests.structures import CaseInsensitiveDict
import ast
import os

IFFTT_KEY = os.environ.get('IFFTT_KEY')
URL =  os.environ.get('URL')
HEADERS = os.environ.get('HEADERS')
print(HEADERS)
headers = ast.literal_eval(str(HEADERS))

resp = requests.get(URL, headers=headers)

if resp.status_code==503:
    requests.get("https://maker.ifttt.com/trigger/VisaLoad/with/key/"+IFFTT_KEY)

print("Executed")
