import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, json={"blog_id": 123 })
print(get_response.json())

