from flask import Flask,jsonify,request
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world !'

@app.route('/machines')
def list_machines():
    
    with open("/home/osboxes/python/tpflask/infra.json","r") as f :
        jsonContenu = json.load(f)
      
    machines = []
    for machine in jsonContenu : machines.append(machine)
    return jsonify(machines)

@app.route('/machines/<name>')
def get(name):
    
    machine = getMachine(name)
    
    if machine is None : return "Cette machine n'existe pas", 404
    else: return jsonify(machine)
    
@app.route('/machines', methods=['POST'])
def create():
    
    try :
        postMachine = json.loads(request.data)
        assert isinstance(postMachine, dict)
    except : return "Format Json Incorrect", 406
    
    try :
        name = postMachine["name"]
        owner = postMachine["owner"]
        os = postMachine["os"]
        ram =  postMachine["ram"]  
    except : return "Les champs requis ne sont pas renseignés", 406
    
    try :
        str(postMachine["name"])
        str(postMachine["owner"])
        str(postMachine["os"])
        int(postMachine["ram"])
    except : return "Formats champs invalides", 406
     
    machines = []
    with open("/home/osboxes/python/tpflask/infra.json","r") as fr :
        jsonContenu = json.load(fr)
        for machine in jsonContenu :
            if machine["name"] != postMachine["name"] : machines.append(machine)
            else : return "Machine deja existante - ajout impossible", 406
        
    machines.append(postMachine)
    
    with open("/home/osboxes/python/tpflask/infra.json","w") as fw :
        json.dump(machines,fw)
        
    return "Ajout effectué", 200
    
@app.route('/machines/<name>', methods=['DELETE'])
def delete(name):
    
    with open("/home/osboxes/python/tpflask/infra.json","r") as fr :
        jsonContenu = json.load(fr)
      
    machines = []
    exist = False
    for machine in jsonContenu :
        if machine["name"] != name : machines.append(machine)
        else : exist = True
        
    if not exist : return "Machine non existante - rien à supprimer", 406
    
    with open("/home/osboxes/python/tpflask/infra.json","w") as fw :
        json.dump(machines,fw)
    
    return "Suppression effectuée", 200
    
@app.route('/machines/<name>/<action>', methods=['POST'])
def changeState(name,action):
    
    if action not in ["start","stop","restart"] :
        return "Type d'opération invalide", 406
    elif action == "start" : rep = start(name)[1]
    elif action == "stop" :
        return "Suppression effectuée", 200

def getMachine(name) :
    with open("/home/osboxes/python/tpflask/infra.json","r") as f :
        jsonContenu = json.load(f)
      
    machines = []
    for machine in jsonContenu :
        if machine["name"] == name : machines.append(machine)
    
    if len(machines) == 0 : return None
    else : return machines[0]

def start(name) :
    
    machineToChange = getMachine(name)
    
    if machineToChange is None : return "Cette machine n'existe pas", 404
    else:
        if machineToChange["state"] == "up" :
            return "Machine deja demarree", 404
        else :
            with open("/home/osboxes/python/tpflask/infra.json","r") as fr :
                jsonContenu = json.load(fr)
            machines=[]
            for machine in jsonContenu :
                if machine["name"] != machineToChange["name"] : machines.append(machine)
                else :
                    machine["state"]="up"
                    machines.append(machine)
                    
def stop(name):
    
    machines = getMachine(name)
    
    if len(machines) == 0 : return "Cette machine n'existe pas", 404
    else:
        if machines[0]["state"] == "down" :
            return "Machine deja arretee", 404
        else : return "Machine pas arretee", 404
    
    