import requests
import json

URL = 'http://127.0.0.1:8000/crud/'

#This method is used to get data with or withour id
def getData():
    r = requests.get(url=URL)
    print(r)
    if r is not None:
        print(r.json())
        print(r.status_code)

# getData()

#####################################################################################

def postData():
    data = {
        'name':'Mohib 2',
        'reg_no':213,
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL,data=json_data,headers={'Content-Type':'application/json'})
    print(r.status_code)
    print(r.json())


# postData()

