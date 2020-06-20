#Prova4.MatrizW[3][4].InserirCompactadoVetorU[12]TodosParesLinhasIndiceImparMatriz.
#FinalPreencherRestantesVetorSeuíndice.
W=[[0 for i in range(4)]for i in range(3)] #3linhas4colunas.
for l in range(3):
    for c in range(4):
        W[l][c]=int(input(f'Digite Valores de W{l}{c}: '))
U=[0]*12
indic=0
for l in range(3):
    for c in range(4):
        if(l%2!=0):
            if(W[l][c]%2==0):
                U[indic]=W[l][c]
                indic+=1
for i in range(indic,12):
    U[i]=i
for i in range(12):
    print(f'O Vetor Final Posição {i} é {U[i]}')