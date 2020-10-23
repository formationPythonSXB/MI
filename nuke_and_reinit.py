from mydb import db
from models import App
import json
import requests

def reinit_all() :
    db.drop_all()
    db.create_all()
    
def loadDatas() :
    
    reinit_all()
    
    with open("/home/osboxes/python/apps.json","r") as f :
        jsonContenu = json.load(f)
       
    for app in jsonContenu :
        if jsonContenu[app]["level"] != "?" : level = jsonContenu[app]["level"]
        else : level = 0
            
        db.session.add( App(nom=app,niveau=level,etat=jsonContenu[app]["state"]) )

    db.session.commit()