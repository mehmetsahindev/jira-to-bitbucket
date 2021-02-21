import requests
import json
import os.path

# Get config.json file path
config_file = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'config.json')

# Get Bitbucket username and password
# and set auth for requests
with open(config_file) as config_file:
    config = json.load(config_file)
    auth = (config["bitbucket"]["username"], config["bitbucket"]["password"])


# Add project to Bitbucket
def addProject(key, name, description):
    url = "http://localhost:7990/Bitbucket/rest/api/1.0/projects"

    # Set project in json format
    json_data = {}
    json_data["key"] = key
    json_data["name"] = name
    json_data["description"] = description
    data = json.dumps(json_data)

    headers = {
        'Content-Type': "application/json"
    }

    try:
        # POST request to add project
        response = requests.post(url, auth=auth, headers=headers, data=data)

        # Return HTTP error, if exist
        response.raise_for_status()

        # Print success message with project name and key
        print("The project successfully added to Bitbucket. Name: " +
              name + ", Key: " + key)
    except requests.exceptions.RequestException as err:
        # Raise error and exit, if any exception exist
        raise SystemExit(err)


# Get projects from Bitbucket
def getProjects():
    url = "http://localhost:7990/Bitbucket/rest/api/1.0/projects"

    try:
        response = requests.get(url, auth=auth)

        # Return HTTP error, if exist
        response.raise_for_status()

        # Return response in json format
        return json.loads(response.text)

    except requests.exceptions.RequestException as err:
        # Raise error and exit, if any exception exist
        raise SystemExit(err)


# Check if project exist in Bitbucket
def isPorjectExist(key, name, projects):
    for project in projects:
        if project["name"] == name and project["key"] == key:
            return True

    return False
