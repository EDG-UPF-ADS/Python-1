# fuaq ler 5 valores x. se somatório entre 1 e x for maior que 100,
# ler valor pra Y e trocar valores entre X e y. se não maior que 100, mostrar
# a tabuada de 1 até 10 de x.
som=0
tab=0
for i in range(1,6):
    print(f'{i} Execução')
    x=int(input('Insira o Numero X: '))
    som=0
    for j in range(2,x): #pois o 1 e o 8 não entram no somatório.
        som+=x
    if (som>100):
        y=int(input('Insira o Numero Y: '))
        temp=x
        x=y
        y=temp
        print(f'A Variável X é {x} e a Y é {y}')
    else:
        for l in range(1,11):
            tab=x*l
            print(f'Numero {x} Multiplicado por {l} é {tab}')