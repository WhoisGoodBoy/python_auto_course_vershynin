import requests
headers = {
    "ContentType": "application/json"
}


response_example = requests.get('https://swapi.dev/api/people/5', headers=headers)
api_json_ex = response_example.json()
print(response_example.json())