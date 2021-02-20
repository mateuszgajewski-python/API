import requests
import webbrowser
from pprint import pprint

r = requests.get("https://api.thecatapi.com/v1/breeds")

cats = r.json()

catsWithId =    {
                    cat["name"] : cat["id"]
                    for cat in cats
                }

def wypiszListeRas(breeds = catsWithId):
    for breed in breeds:
        print(breed)

while(1):
    podanyKotek = str(input("Podaj nazwe kotka lub wyslij '?'"))
    if(podanyKotek == '?'):
        wypiszListeRas()
    else:
        r2 = requests.get("https://api.thecatapi.com/v1/images/search?breed_ids=" + catsWithId[podanyKotek])
        pythonCode = r2.json()
        for dictionary in pythonCode:
            webbrowser.open_new_tab(dictionary["url"])
        
            


