def plus_grand(tab) :
    
    for i in range(len(tab)) :
        if i==0 or tab[i] > grand : grand = tab[i]
        
    return grand

def plus_petit(tab) :
    
    for i in range(len(tab)) :
        if i==0 or tab[i] < petit : petit = tab[i]
        
    return petit

def plus_long(tab) :
    
    for i in range(len(tab)) :
        if i==0 or len(tab[i]) > tailleMax :
            tailleMax = len(tab[i])
            iLong = i
            
    return tab[iLong]

def somme(tab) :
    
    somme = 0
    for i in range(len(tab)) : somme+=tab[i]
    return somme

def sommeRecu(tab) :
    if len(tab) == 0 : return 0
    else : return tab[0] + sommeRecu(tab[1:])

assert plus_grand([5,9,12,6,-1,4]) == 12
assert plus_petit([5,9,12,6,-1,4]) == -1
assert plus_long(["Paris","Amsterdam","Londres"]) == "Amsterdam"
assert somme([3,4,5]) == 12

print (sommeRecu([3,4,5,8]))