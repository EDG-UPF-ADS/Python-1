y=90
primo=0
while(primo<3):
    cont=0
    for i in range (1,y+1):
        if(y%i==0):
            cont=cont+1
    if(cont==2):
        print(y,"e primo")
        primo+=1
    y+=1