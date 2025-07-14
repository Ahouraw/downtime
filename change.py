import requests

response = requests.get("https://td.com")

if response.status_code == 200:
    print("Request was successful!")
else:
    print(f"Request failed with status code: {response.status_code}")
