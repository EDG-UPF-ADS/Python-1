#lerV10.encontraremostrarmenorvaloreposicao.
#mediadosvalorespares.
v=[0]*10
mnr=0
pos=0
med=0
par=0
for i in range(10):
    v[i]=int(input(f'Digite Valores de V{i}: '))
    if(i==0):
        mnr=v[i]
        pos=i
    if(v[i]%2==0):
        med+=v[i]
        par+=1
    if(mnr>v[i]):
        mnr=v[i]
        pos=i
print(f'O Menor Valor Digitado Foi {mnr} na posição {pos} do Vetor')
if(par!=0):
    med=med/par
    print(f'A Média dos {par} Pares Digitados é {med}')
else:
    print('Não Foram Digitados Pares')