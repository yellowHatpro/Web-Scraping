import requests
import random
import  webbrowser

while True:
    
    query=input("Enter the search query: ")
    request_url = f"https://api.unsplash.com/search/photos?query={query}&client_id=6fa91622109e859b1c40218a5dead99f7262cf4f698b1e2cb89dd18fc5824d15"
    request=requests.get(request_url)
    data=request.json()
    if len(data["results"])<=1:
        print("No results found")
        exit=input("Do you want to exit?(y/n)")
        if exit=="y":
            break
        else:
            continue
    number=random.randint(0,len(data["results"])-1)    
    dwnld=input("Do you want to download the picture or open it in browser?(y/n)")
    if dwnld=="y":
        webbrowser.open(data["results"][number]["links"]["download"])

    else:    
       
        webbrowser.open(data["results"][number]["urls"]["full"])
        exit=input("Do you want to exit?(y/n)")
        if exit=="y":
            break