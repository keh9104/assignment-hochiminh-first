import requests

GOOGLE_MAPS_API_URL = "https://maps.googleapis.com/maps/api/geocode/json"

params = {"address": "ho chi minh", "key": ""}

req = requests.get(GOOGLE_MAPS_API_URL, params=params)
print(req.url)

res = req.json()['request']
location = res[0]['geometry']['location']
print(location['lat'], location['lng'])
