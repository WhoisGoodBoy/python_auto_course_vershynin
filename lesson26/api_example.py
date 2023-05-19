import requests


response_example = requests.get('https://randomuser.me/api/')
assert response_example.status_code == 200
print(response_example.json())
