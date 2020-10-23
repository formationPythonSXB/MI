from random import randint

def affichAllumettes(nbAlum) :
    print ('|'*nbAlum)
    
def choisirNombre (tour,nbAlum) :    
    if tour%2+1 == 1 :
        try :
            choix=int(input("Joueur - Combien t'en veux ? (1,2,3)\n"))
        except :
            print("Format nombre incorrect - Le tour passe")
            return
    
        if choix>=1 and choix<=3 and nbAlum-choix>0 : return choix
        else : print("Choix incorrect- Le tour passe")
        
    else :
        if nbAlum >= 4 : choix = randint (1,3)
        else : choix = randint (1,nbAlum-1)
        
        print ("L'ordinateur choisit " + str(choix) + " allumettes")
        return choix
    
def partieAllumettes () :
    
    nbAlum = randint (10,30)
    tour=0
        
    while nbAlum > 1 :
    
        affichAllumettes(nbAlum)
        choix = choisirNombre(tour,nbAlum)
    
        if choix is not None :
            nbAlum -= choix
            if nbAlum != 1 : tour += 1
        else : tour+=1
    
    if tour%2+1 == 1 : print ("Vainqueur : Joueur")
    else : print ("Vainqueur : Ordinateur")
    
partieAllumettes()