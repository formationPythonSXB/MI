import requests
import json

class Infra:
    
    def __init__(self, urlRacine):
        self.urlRacine = urlRacine
        
    def list(self):
        r = requests.get(self.urlRacine + "/machines")

        if r.status_code != 200:
            raise Exception(r.text)
        
        jsonMachines = json.loads(r.text)
        print (jsonMachines)
        machines = []
        for machine in jsonMachines:
            machines.append(machine["name"])
            
        return machines
    
    def get(self,nom):
        r = requests.get(self.urlRacine + "/machines/" + nom)

        if r.status_code != 200:
            raise Exception(r.text)
        
        jsonMachines = json.loads(r.text)
        return jsonMachines
    
    def create(self, name,owner,os,ram):
        
        create_request = { 
            "name": name,
            "os": os,
            "owner": owner,
            "ram": ram
        }
        
        r = requests.post(self.urlRacine + "/machines", json.dumps(create_request))
        
        if r.status_code != 200:
            raise Exception(r.text)
    
    def delete(self,nom):
        r = requests.delete(self.urlRacine + "/machines/" + nom)
        
        if r.status_code != 200:
            raise Exception(r.text)
    
    def start(self,nom):
        
        if infra.get(nom)["state"] == "down" :

            r = requests.post(self.urlRacine + "/machines/" + nom + "/start")
            
            if r.status_code != 200:
                raise Exception(r.text)
            
        
    def stop(self,nom):
        
        if infra.get(nom)["state"] == "up" :
        
            r = requests.post(self.urlRacine + "/machines/" + nom + "/stop")
            
            if r.status_code != 200:
                raise Exception(r.text)
        
    def restart(self,nom):
        
        self.stop(nom)
        self.start(nom)
        
    
infra = Infra("http://127.0.0.1:5000")

print(infra.list())
print(infra.get("phoenix"))

#infra.create(name="apiMI", owner="alex", os="linuxmint", ram=3.5)
#infra.delete("apiMI2")

infra.start("phoenix")