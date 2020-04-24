# ler 5 val x. veric cada x par ou impar. se par mostrar somatório
# dos impares existentes entre 1 e x. se ímpar, mostrar tabuada
# de 1 até 10.
tab=0
for i in range(1,6):
    som=0
    print(f'{i} Execução')
    x=int(input('Insira o Numero X: '))
    if (x%2==0):
        for j in range(1,x):
            if (j%2!=0):
                som+=j
        print(f'Somatório é {som}')
    else:
        for l in range(1,11):
            tab=x*l
            print(f'Numero {x} Multiplicado por {l} é {tab}')