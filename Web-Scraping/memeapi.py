import requests
import random
import webbrowser
request=requests.get("https://api.imgflip.com/get_memes")
jsonfile=request.json()
number=random.randrange(0,len(jsonfile["data"]["memes"]))
webbrowser.open(jsonfile["data"]["memes"][number]["url"])