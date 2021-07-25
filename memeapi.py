import requests
import random
import webbrowser
requests=requests.get("http://api.imgflip.com/get_memes")

memes=requests.json()

num=random.randint(0,len(memes["data"]["memes"]))
webbrowser.open(memes["data"]["memes"][num]["url"])