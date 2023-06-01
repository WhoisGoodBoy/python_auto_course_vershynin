import requests
import json

create_product_url = 'https://api.restful-api.dev/objects'

product_headers = {
    "content-type": "application/json"
}
product_json = json.dumps({
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
})

#post_a_product = requests.post(create_product_url, data=product_json, headers=product_headers)
#print(post_a_product.json())
with requests.Session() as s:
   view_a_product = s.get('https://api.restful-api.dev/objects/ff80818188764f13018877cc2d380190')
   print(view_a_product.content)

try:
   req = requests.get('https://www.google.com/notesdrt')
   req.raise_for_status()
except requests.exceptions.HTTPError as err:
   assert err.response.status_code == 404