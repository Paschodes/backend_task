import requests

URL = "http://[::]:8000/task.html"

user_params = {
    "slackUsername": "Paschodes",
    "backend": True,
    "age": 24,
    "bio": "I am an aspiring backend developer, I love everything tech"
}

response = requests.get(url=URL, json=user_params)
response.raise_for_status()
print(response.text)