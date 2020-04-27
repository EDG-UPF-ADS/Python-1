k=-1
while(k!=0):
    while(k<0):
        k=int(input('Insira K: '))
    if(k!=0):
        if(k%2==0):
            acum=0
            for i in range(2,k):
                if(i%2!=0):
                    acum=acum+i
            print(acum)
        k=-1 
