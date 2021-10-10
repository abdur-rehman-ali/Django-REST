import requests
import json

URL = 'http://127.0.0.1:8000/crud/'

#This method is used to get data with or withour id
def getData(id=None):
    data = {
        'id':id,
    }
    json_data = json.dumps(data)
    r = requests.get(url=URL,data=json_data,headers={'Content-Type':'application/json'})
    print(r.json())
    print(r.status_code)

# getData(2)

#####################################################################################

def postData():
    data = {
        'name':'Rimaan',
        'reg_no':20180,
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL,data=json_data,headers={'Content-Type':'application/json'})
    print(r.status_code)
    print(r.json())


# postData()

#####################################################################################
def updateData():
    data = {
        'id':6,
        'name':'Joyia',
        
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL,data=json_data,headers={'Content-Type':'application/json'})
    print(r.status_code)
    print(r.json())

# updateData()

#####################################################################################
def deleteData(id):
    data = {
        'id':id,
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL,data=json_data,headers={'Content-Type':'application/json'})
    print(r.status_code)
    print(r.json())

# deleteData(4)