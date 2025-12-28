import requests

BASE = "http://localhost:5000/"

response = requests.get(BASE + "helloworld")
response = requests.post(BASE + "video/1", json = {"name": "video1", "views" : 10,  "likes" : 7})
print(response.json())
