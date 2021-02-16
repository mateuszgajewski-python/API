import requests
from pprint import pprint
import json

downloadJSON = requests.get("https://cat-fact.herokuapp.com/facts/random?amount=5")

myJsonCode =  downloadJSON.text #weź tekst i zapisz do zmiennej

myPythonCode = json.loads(myJsonCode) #załadujJson aby rozkodowac

cats = myPythonCode
   

for cat in cats:
    print(cat['text'])


