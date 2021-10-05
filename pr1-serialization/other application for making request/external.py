"""
This file is used to make API request to the API we have created in mysite project 
"""
import requests

URL = 'http://127.0.0.1:8000/list/'

response = requests.get(URL)

print(response.json())