# ler 6 valores X.
# encontrar e mostrar o maior valor de x.
m=-999
for i in range(6):
    x=int(input('Digite o Valor de X: '))
    if (m<x):
        m=x
if (m==0):
    print('Não Foram Digitados Valores Válidos')
else:
    print(f'O Maior Valor foi {m}')