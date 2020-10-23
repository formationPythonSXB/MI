def nomFichier (chemin) :
    tab = chemin.split('/')
    return tab[len(tab)-1].split('.')[0]
    
print (nomFichier ("/usr/bin/toto.py"))