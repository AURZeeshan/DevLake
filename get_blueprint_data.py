import requests
import pandas as pd
import json


devlake_url = "http://54.236.25.78:4000/api/"
blueprints_endpoint = "blueprints"



# Make API call to get blueprints with ID 3
response = requests.get(f"{devlake_url}{blueprints_endpoint}")
if response.status_code == 200:
    blueprints_data = response.json()
    # with open("file.json", 'w') as json_file:
    #     json.dump(blueprints_data, json_file)
    print("Data from step 1:")
else:
    print("Error: Could not get the data from the API. Status code:", response.status_code)


repo_name = blueprints_data["blueprints"]
print("Repo name from step 2:")




for name in blueprints_data["blueprints"]:
    github_token = ""  # Replace with your GitHub personal access token
    github_repo = "DevLake"  # Replace with your GitHub repository name
    issue_title = f"{name['name']}"  # Use the extracted repository name

    # GitHub API endpoint for creating an issue
    github_api_url = f"https://api.github.com/repos/AURZeeshan/{github_repo}/issues"

    # Request headers with authentication token
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github.v3+json",
    }

    # Request payload for creating the issue
    payload = {
        "title": issue_title,
        "body": "This is a new issue created programmatically.",
    }

    # Make API call to create a new issue
    response = requests.post(github_api_url, headers=headers, json=payload)

    # Print the response status and data
    print("GitHub API Response:")
    print(f"Status Code: {response.status_code}")
    print(response.json())



