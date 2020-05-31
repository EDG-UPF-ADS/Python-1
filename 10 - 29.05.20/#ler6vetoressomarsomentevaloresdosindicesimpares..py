#ler6vetoressomarsomentevaloresdosindicesimpares. 
x=[0]*6
acum=0
for i in range(6):
    x[i]=int(input(f'Digite o Valor de X{i}: '))
for i in range(6):
    if(i%2==1):
        acum+=x[i]
print(f'O Somatório é {acum}')