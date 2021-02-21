import jira
import bitbucket

# Get projects from Jira
jira_projects = jira.getProjects()
# Get projects from Bitbucket
bitbucket_projects = bitbucket.getProjects()

# For counting updated projects
updated_projects_count = 0

# Loop all jira porjects
for jira_project in jira_projects:
    p_name = jira_project["name"]
    p_key = jira_project["key"]
    p_desc = jira_project["description"]

    # Check if jira project exist in Bitbucket.
    # if not exist, add to Bitbucket
    if bitbucket.isPorjectExist(p_key, p_name, bitbucket_projects["values"]) == False:
        bitbucket.addProject(p_key, p_name, p_desc)
        updated_projects_count += 1


# Print results
results = """ 
*-------------*-------------*
Jira projects count   : {}
Updated projects count: {}
*-------------*-------------*
 """.format(len(jira_projects), updated_projects_count)

print(results)
