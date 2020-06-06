# matriz 1 somatório 2 linha que e a linha1.
# calcular mostrar somátório valores da 2 linha. 
m=[[0 for i in range(4)]for i in range(3)]
acum=0
for l in range(3):
    for c in range(4):
        m[l][c]=int(input(f'Digite Valores:{l}{c} '))
for i in range(3):
  acum+=m[1][i]
print(acum)