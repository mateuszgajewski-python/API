import requests
from pprint import pprint

rok = int(input("Podaj rok max.2049 "))

print()

params = {
    "api_key" : "6bbc4d3ea6a89acefc35ab7cf109c25378062b68",
    "country" : "pl",
    "year" : rok
    }

r = requests.get("https://calendarific.com/api/v2/holidays", params)
pythonCode = r.json()
for primarykey in pythonCode["response"]["holidays"]:
    print(primarykey["name"], primarykey["date"]["iso"])
    print()

stop = int(input())

