from cercle import Cercle
from cylindre import Cylindre

c1 = Cercle(5,(3,1))
c2 = Cercle(5,(33,1))
print("Aire : " , c1.aire())
print(c1.intersect(c2))

c3 = Cylindre(3,4,(1,2,3))
c4 = Cylindre(3,4,(1,2,3))
print(c3.intersect(c4))