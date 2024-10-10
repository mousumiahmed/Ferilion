Api key access and Auth details:

https://support.zerodha.com/category/trading-and-markets/kite-web-and-mobile/kite-api/articles/how-do-i-sign-up-for-kite-connect

Documentation -

https://kite.trade/docs/connect/v3/

Free Api - 

https://jsonplaceholder.typicode.com/

python rest methods call - 

pip install requests

Get:

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

# Print the response content (as text)
print(response.text)

# Print the response content (as JSON)
print(response.json())

Post:

import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

response = requests.post(url, json=data)

# Print the response content (as JSON)
print(response.json())



Put:

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
data = {
    "id": 1,
    "title": "updated title",
    "body": "updated body",
    "userId": 1
}

response = requests.put(url, json=data)

# Print the response content (as JSON)
print(response.json())



Delete :

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.delete(url)

# Print the status code (204 indicates success without content)
print(response.status_code)



### GET Request with Authentication Header

```
import requests

# Define the URL for the request
url = "https://api.example.com/data"

# Define the headers with the authentication token
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

# Make the GET request with the authentication header
response = requests.get(url, headers=headers)

# Print the response content (as JSON)
print(response.json())

```







https://stackoverflow.com/questions/2289712/where-do-i-find-api-key-and-api-secret-for-facebook

https://developers.facebook.com/docs/pages-api/search-pages

