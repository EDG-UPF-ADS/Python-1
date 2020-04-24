x=int(input('Digite o Valor de X '))
y=int(input('Digite o Valor de Y '))

if(x>y):
    xorig=x
    x=y
    y=xorig
if(x==y):
    soma=y*0.45
    print('O Valor de 45% de Y é ',soma)
if(x<y):
    z=int(input('Insira o Valor de Z '))
    soma=x+y+z
    print('A Soma XYZ é',soma)
