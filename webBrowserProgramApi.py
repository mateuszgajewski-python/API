import requests
import json
import pprint
import webbrowser



params = {
    "fromdate": 1612656000,
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
            
        
        
