# ler10vetores.trocavalordosindices.sótrocaquandoindicepar.
K=[0]*10
aux=int
for i in range(10):
    K[i]=(input(f'Digite o Valor de K{i+1}: '))
for i in range(10):
    if(i%2==0):
        aux=K[i]
        K[i]=K[i+1]
    else:
        K[i]=aux
for i in range (10):
    print(f'o K{i+1} vale {K[i]}')        
