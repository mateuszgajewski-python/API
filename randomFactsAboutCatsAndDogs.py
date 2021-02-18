import requests
from pprint import pprint
import json

def piec_faktow(animal):          

    params ={

        "amount": 5,
        "typ" : animal
            

        }


    downloadJSON = requests.get("https://cat-fact.herokuapp.com/facts/random", params)

    myJsonCode =  downloadJSON.text #weź tekst i zapisz do zmiennej

    myPythonCode = json.loads(myJsonCode) #załadujJson aby rozkodowac

    animals = myPythonCode
           

    for animal in animals:
        print(animal['text'])


while(1):

    ch = int(input("Wybierz:\n1 - piec faktow o kotach\n2 - piec faktow o psach"))

    if(ch == 1):
        piec_faktow("cat")
    elif(ch == 2):
        piec_faktow("dog")
            
