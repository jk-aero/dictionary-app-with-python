import requests
response = requests.get("https://api.urbandictionary.com/v0/random")
api_data=response.json()['list'][3]
print(api_data)

