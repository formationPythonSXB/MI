from random import randint

nb = randint (1,100000)

choix = int(input ("Saisir nombre : "))
essais=1

while choix != nb :
    if choix < nb : print("Plus grand")
    elif choix > nb : print("Plus petit")
    essais+=1
    choix = int(input ("Saisir nombre : "))

print ("Gagne : " , choix, " - Essais : " , essais)