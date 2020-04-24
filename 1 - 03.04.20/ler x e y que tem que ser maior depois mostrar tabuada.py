# ler valores X e Y. constir que Y receba maior que X.
# após mostrar tabuada de 1 a 10
# de cada um dos inteiros entre x e y.
x=int(input('Insira o Valor de X: '))
y=x-1
while(y<x):
    y=int(input('Insira o Valor de Y: '))
for i in range (x+1,y):
    for c in range (1,11):
        tab=c*i       
        print(f'Tabuada do {i} x {c} é {tab}')