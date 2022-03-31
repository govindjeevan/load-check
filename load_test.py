import requests
import ast
import os
import time

IFFTT_KEY = os.environ.get('IFFTT_KEY')
URL =  os.environ.get('URL')
HEADERS = os.environ.get('HEADERS')
headers = ast.literal_eval(HEADERS)

for i in range(5):
    resp = requests.get(URL, headers=headers)

    if resp.status_code==503 or "organization" in str(resp.content) or "organisation" in str(resp.content):
        requests.get("https://maker.ifttt.com/trigger/VisaLoad/with/key/"+IFFTT_KEY)
        break
        
    print("Executed ", resp.status_code)
    time.sleep(5)
    

