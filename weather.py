import requests

url = "https://wttr.in/{}"
payload = {"lang": "ru",
           "m" : "",
           "T" : "",
           "n" : "",
           "q" : ""}
cities = ["chehov",
          "moscow",
          "saint-petersburg"]

for city in cities:
    response = requests.get(url.format(city), params=payload)
    response.raise_for_status()
    print(response.text)