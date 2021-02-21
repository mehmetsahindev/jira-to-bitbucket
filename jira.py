import requests
import json
import os.path

# Get config.json file path
config_file = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'config.json')

# Get Jira username and password
# and set auth for requests
with open(config_file) as config_file:
    config = json.load(config_file)
    auth = (config["jira"]["username"], config["jira"]["password"])


# Get projects from Jira
def getProjects():
    url = "http://localhost:8080/JIRA/rest/api/2/project?expand=description"

    try:
        # GET request to retrieve projects
        response = requests.get(url, auth=auth)

        # Return HTTP error, if exist
        response.raise_for_status()

        # Check, is there any project in Jira
        if len(json.loads(response.text)) == 0:
            raise SystemExit("There is no project in Jira")

        # Return response in json format
        return json.loads(response.text)

    except requests.exceptions.RequestException as err:
        # Raise error and exit, if any exception exist
        raise SystemExit(err)
