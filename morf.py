import json
from urllib.request import urlopen
name = input("Enter your name: ")
myKey = "place Your Key Here"
url = "http://gender-api.com/get?key="
url = url +myKey +f"&name={name}"
response = urlopen(url)
decoded = response.read().decode("utf-8")
data = json.loads(decoded)
print("Gender: " + data['gender'])