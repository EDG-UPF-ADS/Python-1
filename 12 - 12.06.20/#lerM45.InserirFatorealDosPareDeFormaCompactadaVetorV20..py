#lerM45.InserirFatorealDosPareDeFormaCompactadaVetorV20.
#seRestarElemVaziosVetorPreencherCom0.
#CalculoFatorialNumaFunção.
def fatorial(nro):
    f=1
    for i in range(1,nro+1):
        f=f*i
    return(f)
m=[[0 for i in range(5)]for i in range(4)] #4 linhas 5 colunas.
v=[0]*20
acum=0
for l in range(4):
    for c in range(5):
        m[l][c]=int(input(f'Digite Valores de M{l}{c}: '))
        if(m[l][c]%2==0):
            v[acum]=fatorial(m[l][c])
            acum+=1
for i in range(acum, 20):
    v[i]=0
for j in range(20):
    print(f'O valor do vetor v{j} é {v[j]}')