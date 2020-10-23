from carte import Carte
from paquet import Paquet

c1 = Carte('J',"Trefle")

p = Paquet()

p.couper()
for carte in p.cartes: print(carte)

print("Carte : " + str(p.piocher()))

print(p.distribuer(2,3))




