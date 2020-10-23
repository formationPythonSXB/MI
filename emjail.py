def genererModele (prenom,dest) :
    
    modele="""Bonjour {prenom} !Voici en pièce jointe les billets pour votre voyage en train vers {destination}."""
    
    with open("/home/osboxes/python/billet_" + prenom + ".txt", "w") as f :
        f.write(modele.replace("{prenom}",prenom).replace("{destination}",dest))
    

genererModele ("Ivan", "Butten")