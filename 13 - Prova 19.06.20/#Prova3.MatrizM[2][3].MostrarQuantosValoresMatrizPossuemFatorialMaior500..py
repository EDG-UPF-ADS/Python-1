#Prova3.MatrizM[2][3].MostrarQuantosValoresMatrizPossuemFatorialMaior500.
m=[[0 for i in range(3)]for i in range(2)] #2linhas3colunas.
for l in range(2):
    for c in range(3):
        m[l][c]=int(input(f'Digite Valores de M{l}{c}: '))
acum=0
for l in range(2):
    for c in range(3):
        f=1
        for i in range(1,m[l][c]+1):
            f=f*i
        if(f>500):
            acum+=1
if(acum!=0):
    print(f'A Quantidade Encontrada foi {acum} De Valores de Fatorial Maiores que 500 ')
else:
    print('Não Foram Encontrados Valores com Fatorial Acima de 500')