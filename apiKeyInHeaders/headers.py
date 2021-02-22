import requests
import authentical

r = requests.get('https://api.thecatapi.com/v1/favourites', headers = authentical.headers)

print(r.text)
