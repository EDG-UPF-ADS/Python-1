#TEMAlêvaloresvetorW6.ApósEncontrarMostrarMaiorValorEposiçãoVetor.
W=[0]*6
for i in range(6):
    W[i]=int(input(f'Insira o Valor de W{i+1}: '))
m=W[0]
p=0
for i in range (1,6):
    if (W[i]>m):
        m=W[i]
        p=i
print (f'Maior é {m} na posicao {p+1}')