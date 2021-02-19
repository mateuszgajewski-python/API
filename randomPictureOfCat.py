import requests
import webbrowser

r = requests.get("https://aws.random.cat/meow")

zdjecieKotka = r.json()

webbrowser.open_new_tab(zdjecieKotka["file"])
