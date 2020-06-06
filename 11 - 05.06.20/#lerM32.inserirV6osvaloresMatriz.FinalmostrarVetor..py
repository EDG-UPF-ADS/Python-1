#lerM32.inserirV6osvaloresMatriz.FinalmostrarVetor.
m=[[0 for i in range(3)]for i in range(2)]
for l in range(2):
    for c in range(3):
        m[l][c]=int(input(f'Digite Valores {l}{c}: '))
v=[0]*6
indic=0
for l in range(2):
    for c in range(3):
        v[indic]=m[l][c]
        indic+=1
for i in range(6):
    print(f'O Vetor Completo é {v[i]}')

            