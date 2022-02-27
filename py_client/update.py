import requests

endpoint = "http://localhost:8000/api/blogs/1/update/"
data = {
    "title":"This data is updated from update view",
}

get_response = requests.put(endpoint,json=data)

print(get_response.json())