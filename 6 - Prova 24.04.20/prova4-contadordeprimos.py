# descobrir os 3 numeros primos acima de 90.
y=90
primo=0
while(primo<3):
    div=0
    for i in range(1,y+1):
        if(y%i==0):
            div+=1
    if(div==2):
        print(f'Numero Primo é {y}')
        primo+=1
    y+1