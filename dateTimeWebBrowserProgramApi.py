import requests
import json
import pprint
import webbrowser
from datetime import datetime, timedelta

time7daysAgo = timedelta(days=5)
print(time7daysAgo)


timeNow = datetime.today()
print(timeNow)

searchTime = timeNow - time7daysAgo
print(searchTime)


print(timeNow.timestamp())
print(searchTime.timestamp())
print(timeNow.timestamp() - searchTime.timestamp())






params = {
    "fromdate": int(searchTime.timestamp()),
    "order": "desc",
    "min": 5,
    "sort":"votes",
    "tagged":"python",
    "site":"stackoverflow"
    }


r = requests.get("https://api.stackexchange.com/2.2/questions", params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("niepoprawny format")
else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])
            
        
        

