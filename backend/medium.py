import requests

url = "https://api.medium.com/v1/users/5303d74c64f66366f00cb9b2a94f3251bf5/publications"
# r = requests.get(url)
url = "https://api.medium.com/v1/me"
url = "https://api.medium.com/v1/users/17d139d19d4e7318b2ae3afaf08cf842c86cf0a0712e95d7ab98b3729dfd5e8e6/publications"
# set the request parameters
headers = {
    "Authorization": "Bearer " + "2a39f0bf21e1af08ec6a2071bd23a07aea6cc2c7646ec8240cf35b3af3225960c"
}

# send the HTTP request
response = requests.get(url, headers=headers)

# print the response content
print(response.json())
