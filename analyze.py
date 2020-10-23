from models import App
import nuke_and_reinit as reinit
import time
import json
        
def getAppsFromLevel_BDD(level):
              
    apps_from_level = App.query().filter(App.niveau >= level).all()
        
    print ("Applications de niveau", level, "ou supérieur : \n")
    
    if len(apps_from_level)==0: print("Aucune application trouvée")
    else:
        print(len(apps_from_level),"application(s) trouvée(s)\n")
        
def getAppsFromLevel_File(level):
    
    with open("/home/osboxes/python/apps.json","r") as f :
            jsonContenu = json.load(f)
            
    cptApp = 0
    print ("Applications de niveau", level, "ou supérieur : \n")
            
    for app in jsonContenu :
        if jsonContenu[app]["level"] == "?" : l = 0
        else: l = jsonContenu[app]["level"]
        
        if l >= level : cptApp += 1
        
    print(cptApp,"application(s) trouvée(s)\n")
        
def getTempsExecution(level,typeLoad):

    start_time = time.time()
    
    if typeLoad == "BDD" : getAppsFromLevel_BDD(level)
    elif typeLoad == "File" : getAppsFromLevel_File(level)
    
    print (typeLoad, '- Total time : ', time.time()-start_time ,"\n")
        
 
reinit.loadDatas()
getTempsExecution(1,"BDD")
getTempsExecution(1,"File")
