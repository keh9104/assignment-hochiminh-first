import requests
import webbrowser

search = "korean"
queryString = {'q': search}
searchEngine = 'https://www.google.com/search'
r = requests.get(searchEngine, params=queryString)

print(r.url)
webbrowser.open(r.url)
