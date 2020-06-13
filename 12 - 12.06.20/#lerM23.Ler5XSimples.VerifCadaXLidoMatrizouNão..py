#lerM23.Ler5XSimples.VerifCadaXLidoMatrizouNao.
#SeSimMostrarLeC.SenãoNãoEstanaMatriz.
#NoFinalMostrarQuantidadedeXnaMatriz.
m=[[0 for i in range(3)]for i in range(2)]
acum=0
for l in range(2):
    for c in range(3):
        m[l][c]=int(input(f'Digite Valores de M{l}{c}: '))
for i in range(5):
    x=int(input('Digite o Valor do X: '))
    for l in range(2):
        for c in range(3):
            if(m[l][c]==x):
                print(f'O Valor foi Encontrado em {l=} e {c=}')
                acum+=1
if(acum!=0):
    print(f'O Valor foi Encontrado {acum} vezes.')
else:
    print(f'O Valor Não Foi Encontrado')