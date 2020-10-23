class Carte:
    
    def __init__(self,valeur,couleur):
        
        valeurs = [1,2,3,4,5,6,7,8,9,10,'J','Q','K']
        couleurs = ["Carreau","Trefle","Pique","Coeur"]
        
        if valeur not in valeurs or couleur not in couleurs : raise Exception("Donnees incorrectes")
        else :
            self.valeur=valeur
            self.couleur=couleur
        
    @property
    def points(self):
        if self.valeur == 'K': return 13
        elif self.valeur == 'Q': return 12
        elif self.valeur == 'J': return 11
        else: return self.valeur
        
    def __repr__(self):
        return (str(self.valeur) + " de " + self.couleur)
    