def carre():
    
    i=1
    
    while (i**2) <= 200 :
        yield i**2
        i+=1
        
for nb in carre() : print(nb)