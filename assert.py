def centrer(chaine,longueur):
    blank = int(((longueur-2)-len(chaine))/2)
    mod = (longueur-len(chaine)) % 2
    return ("|" + " " * blank + chaine + " " * (blank+mod) + "|")   
    
def encadrer(chaine,longueur):
    assert isinstance(longueur,int), "Longueur doit etre un entier"
    assert longueur >= -1, "Nombre incorrect"
    assert isinstance(chaine,str), "Chaine doit etre une chaine"
    
    return "#"*longueur + "\n" + centrer(chaine,longueur) + "\n" + "#"*longueur;


print(encadrer(5,12))