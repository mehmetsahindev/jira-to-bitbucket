import requests
import json


with open('./config.json') as config_file:
    config = json.load(config_file)


def getProjects():
    url = "http://localhost:8080/JIRA/rest/api/2/project"

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers, auth=(
        config["login"]["jira"]["username"], config["login"]["jira"]["password"]))

    return response.text
