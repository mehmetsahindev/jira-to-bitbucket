import requests
import json


def login():
    url = "http://localhost:8080/JIRA/rest/auth/1/session"

    payload = '{"username": "admin","password": "123456"}'
    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.text
    except:
        print("Error")


print(login())
