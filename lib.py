import json

def getAppByLevel (level) :

    with open("/home/osboxes/python/apps.json","r") as f :
            jsonContenu = json.load(f)
            
    for app in jsonContenu :
        if jsonContenu[app]["level"] == level : print (app)
        
def getAppByStatus (state) :

    with open("/home/osboxes/python/apps.json","r") as f :
            jsonContenu = json.load(f)
            
    for app in jsonContenu :
        if jsonContenu[app]["state"] == state : print (app)

getAppByLevel(5)

getAppByStatus("notworking")