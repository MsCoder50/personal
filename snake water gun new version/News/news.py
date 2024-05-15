import requests

data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=ac0e01159d50401ba90f548828d484b6").json()

