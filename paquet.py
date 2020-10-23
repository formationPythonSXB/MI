from carte import Carte
import random

class Paquet:
    
    def __init__(self):
        valeurs = [1,2,3,4,5,6,7,8,9,10,'J','Q','K']
        couleurs = ["Carreau","Trefle","Pique","Coeur"]
        
        self.cartes = []
                
        for couleur in couleurs:
            for valeur in valeurs:
                self.cartes.append(Carte(valeur,couleur))
                
    def melanger(self):
        random.shuffle(self.cartes)
        
    def couper(self):
        indice_coupe = random.randint(0,51)
        
        self.cartes += self.cartes[0:indice_coupe]
        
        for i in range(0,indice_coupe):
            self.cartes.remove(self.cartes[0])
            
    def piocher(self):
        carte = self.cartes[0]
        self.cartes.remove(self.cartes[0])
        return carte
    
    def distribuer(self,joueurs,cartes):
            
        mains = {}
        
        for i in range(cartes):          
            for j in range(joueurs):
                if i==0 : mains["Joueur " + str(j+1)]={}
                mains["Joueur " + str(j+1)]["Carte " + str(i+1)]=self.piocher()
            
        return mains

