import requests

endpoint = "http://localhost:8000/api/"
get_response = requests.post(endpoint,json={
    "title":"this is post request",
    "content":"helllo again",
})

print(get_response.json())