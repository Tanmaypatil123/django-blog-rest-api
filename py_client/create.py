import requests

endpoint = "http://localhost:8000/api/blogs/" 

data = {
    'title':"This is created from view",
    "content":"hello again from view"
}

get_response = requests.post(endpoint,json=data)

print(get_response.json())