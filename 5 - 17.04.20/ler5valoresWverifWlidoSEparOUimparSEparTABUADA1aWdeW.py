# ler5valoresWverifWlidoSEparOUimparSEparTABUADA1aWdeW
# seIMPARfatorialDEw
fat=0
for i in range(1,6):
    print(f'{i} Execução')
    w=int(input('Insira o Numero W: '))
    if (w%2==0):
        for j in range(1,w+1):
            tab=w*j
            print(f'Numero {w} Multiplicado por {j} é {tab}')
    else:
        fat=0
        for l in range(1,w):
            fat=w*l
        print(f'O Fatorial de {w} é {fat}')