#lerM44.CriarVetorSL4Elem.ContenhaSomaValoresLinhas.
m=[[0 for i in range(4)]for i in range(4)]
sl=[0]*4
soma=0
acum=0
for l in range(4):
    soma=0
    for c in range(4):
        m[l][c]=int(input(f'Digite Valores de M{l}{c}: '))
        soma+=m[l][c]
    sl[acum]=soma
    acum+=1
for j in range(4):
    print(f'O vetor SL{j} é {sl[j]}')