def fibo():
    n1=0
    n2=1
    
    yield 0
    
    while n2 < 500 :
        yield n2
        temp = n1
        n1=n2
        n2=n2+temp
        
for nb in fibo() : print(nb)