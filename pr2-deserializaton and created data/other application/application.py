import requests
import json


"""
This application is responsible for making request to send data to backend
"""

#URL where we want to send data
URL = 'http://127.0.0.1:8000/'

#data which we want to send to backend
data = {
    'name':'Ali joyia',
    'reg_no':2018030,
    'faculty':'CS',
}

#converting python object to json data
json_data = json.dumps(data)

response = requests.post(url=URL, data=json_data)
print(response.json())