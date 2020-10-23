def liste_users() :
    
    with open("/etc/passwd","r") as f :
        contenu = f.readlines()
        
    users = []
    
    for ligne in contenu :
        ligneSplit = ligne.split(":")
        if ligneSplit[len(ligneSplit)-1].strip() == "/bin/bash" : users.append(ligneSplit[0])
        
    return users
    
print(liste_users())