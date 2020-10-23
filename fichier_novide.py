def fic_nolignevide() :
    
    with open("/etc/resolv.conf","r") as f :
        contenu = f.readlines()
        
    lignesNonVides = []
    
    for ligne in contenu :
        if ligne.strip() != "" and not ligne.strip().startswith("#") :
            lignesNonVides.append(ligne)
        
    return lignesNonVides
    
print(fic_nolignevide())