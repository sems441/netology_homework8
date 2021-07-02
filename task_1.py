import requests

token = "2619421814940190"
uri = "https://superheroapi.com/api/2619421814940190/"
names = {"Hulk": 0, "Captain America": 0, "Thanos": 0}
ids = []
power_stats = "/powerstats"
search_name = "/search/"
for name in names.keys():
    url = uri + search_name + name
    name_response = requests.get(url=url)
    id_character = name_response.json()["results"][0]["id"]
    ids.append(id_character)
for id_search in ids:
    url = uri + id_search + power_stats
    response = requests.get(url)
    name = response.json().get("name")
    value = response.json().get("intelligence")
    names[name] = value
for name, intelligence in names.items():
    print(f"у {name} интеллект равен {intelligence}")
