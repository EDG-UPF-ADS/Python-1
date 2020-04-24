# FUAQ lê valores para as variáveis A, B, C e D. Encontrar e mostrar o maior valor dentre as 4 variáveis.
a=int(input('Valor de A: '))
b=int(input('Valor de B: '))
c=int(input('Valor de C: '))
d=int(input('Valor de D: '))
if(a>b and a>c and a>d):
    print('O Valor de A é o Maior, sendo:',a)
if(b>a and b>c and b>d):
    print('O Valor de B é o Maior, sendo:',b)
if(c>a and c>b and c>d):
    print('O Valor de C é o Maior, sendo:',c)
if(d>a and d>b and d>c):
    print('O Valor de D é o Maior, sendo:',d)