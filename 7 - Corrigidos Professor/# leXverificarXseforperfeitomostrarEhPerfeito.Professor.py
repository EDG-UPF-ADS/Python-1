acum=0
x=int(input('Insira X: '))
for i in range(1,x):
    if(x%i==0):
        acum=acum+i
if(acum==x):
    print('Eh perfeito')
else:
    print('Não eh perfeito') 