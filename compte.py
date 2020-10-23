def compte_lettres (chaine) :
    
    dico={}
    
    for c in chaine :
        if c in dico : dico[c]+=1
        else : dico[c]=1
        
    return dico
    
print(compte_lettres("hello"))
print(compte_lettres("Lorem ipsum fhfhh azaa"))