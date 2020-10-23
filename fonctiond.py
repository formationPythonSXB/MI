def annee_naissance (age):
    return 2019-age;

def centrer(chaine,longueur):
    blank = int(((longueur-2)-len(chaine))/2)
    mod = (longueur-len(chaine)) % 2
    return ("|" + " " * blank + chaine + " " * (blank+mod) + "|")   
    
def encadrer(chaine,longueur):
    return "#"*longueur + "\n" + centrer(chaine,longueur) + "\n" + "#"*longueur;
    
print(annee_naissance(29),"\n")
print(centrer("Python",21),"\n")
print(encadrer("Pythoyyyyyyn",21))