def annee_naissance (age):
    if isinstance(age,int) and age>=0 and age<=130 : return 2019-age
    
def centrer(chaine,longueur):
    if longueur != -1 :
        blank = int(((longueur-2)-len(chaine))/2)
        mod = (longueur-len(chaine)) % 2
        return ("|" + " " * blank + chaine + " " * (blank+mod) + "|")
    else : return "| " + chaine + " |"

def encadrer(chaine,longueur):
    if longueur == -1 : return "#"*(len(chaine)+4) + "\n" + centrer(chaine,longueur) + "\n" + "#"*(len(chaine)+4);
    else : return "#"*longueur + "\n" + centrer(chaine,longueur) + "\n" + "#"*longueur;

age = int(input("Quel age as-tu ?"))
annee = annee_naissance(age)
if annee is not None : print (annee)

print(encadrer("Python",-1))