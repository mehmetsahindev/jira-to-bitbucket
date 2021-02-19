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


def getSessionID():
    session = json.loads(login())
    return session["session"]["value"]


def getProjects(JSESSIONID):
    url = "http://localhost:8080/JIRA/rest/api/2/project"

    headers = {
        'Cookie': 'JSESSIONID='+JSESSIONID
    }

    response = requests.request("GET", url, headers=headers)

    return response.text


print(getProjects(getSessionID()))
