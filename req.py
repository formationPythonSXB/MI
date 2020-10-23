import requests
import json

def getAppByLevel (level) :

    r = requests.get("https://app.yunohost.org/apps.json", timeout=30)
    jsonContenu = json.loads(r.text)
            
    for app in jsonContenu :
        if jsonContenu[app]["level"] == level : print (app)
        
def getAppByStatus (state) :

    r = requests.get("https://app.yunohost.org/apps.json", timeout=30)
    jsonContenu = json.loads(r.text)
    
    for nomApp, propApp in jsonContenu.items() :
            if propApp["state"] == state : 
    
    with open("notWork.json","w") as fw :
        for nomApp, propApp in jsonContenu.items() :
            if propApp["state"] == state : json.dump(jsonContenu[nomApp],fw)

getAppByStatus("notworking")


