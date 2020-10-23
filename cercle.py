from math import pi
from math import sqrt

class Cercle:
    
    def __init__(self,rayon,centre):
        self.rayon=rayon
        self.centre=centre
        
    def aire(self):
             return  (pi*self.rayon)**2
            
    def intersect(self,c2):
        if sqrt( (c2.centre[0]-self.centre[0])**2 - (c2.centre[1]-self.centre[1])**2 ) < (self.rayon + c2.rayon):
            return True
        else: return False

