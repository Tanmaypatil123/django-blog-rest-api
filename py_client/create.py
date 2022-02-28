import requests

endpoint = "http://localhost:8000/api/blogs/" 
token="4f6585597cc7ae716e1e718ad72810901242fd04"

headers = {
    "Authorization": f"Bearer {token}"
}

data = {
    'title':"This is created from view",
    "content":"hello again from view"
}

get_response = requests.post(endpoint,json=data,headers=headers)

print(get_response.json())