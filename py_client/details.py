import requests

endpoint = "http://localhost:8000/api/blogs/3/" 

get_response = requests.get(endpoint) 
print(get_response.json())