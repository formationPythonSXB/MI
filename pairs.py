def pairs (liste) :
    for i in range(len(liste)) : print (liste[i])
    
    return [ e for e in liste if e % 2 == 0 ]
    

print (pairs([5,2,22,35,46,98,77,4]))