import requests
import ast
import os
import time

IFFTT_KEY = os.environ.get('IFFTT_KEY')
URL =  os.environ.get('URL')
HEADERS = os.environ.get('HEADERS')
headers = ast.literal_eval(str(HEADERS))

for i in range(5):
    resp = requests.get(URL, headers=headers)

    if resp.status_code==503:
        requests.get("https://maker.ifttt.com/trigger/VisaLoad/with/key/"+IFFTT_KEY)
        break
        
    print("Executed ", i)
    time.sleep(5)
    

