import json

with open("/home/osboxes/python/tpflask/infra.json","r") as f :
        jsonContenu = json.load(f)
        
machines = []
for machine in jsonContenu : machines.append(machine)

print(machines)