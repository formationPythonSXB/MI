def demander_nombre_pair() :
    try:
        nb = int(input("Entrer un nombre pair : "))
    except: raise Exception("Format nombre incorrect")
    
    if nb % 2 != 0 : raise Exception ("Nombre non pair")
    return nb
    
res = demander_nombre_pair()
if res is not None : print(res)