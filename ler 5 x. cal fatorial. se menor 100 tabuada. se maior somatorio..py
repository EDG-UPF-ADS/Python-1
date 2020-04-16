# ler 5 valores pra x. calcualr para cada x sem fatorial.
# se fatorial menor ou igual a 100, mostrar a tabuada de
# 1 até x de x. se fatorial maior que 100, calcular os numeros
# inteiros entre 1 e x.
fat=0
som=0
for i in range(5):
    x=int(input('Insira o Valor de X: '))
    f=1
    fat=0
    for c in range(1,x+1):
        f=f*c
        fat+=f
    if(fat<=100):
        for j in range(1,x+1):
            tab=j*x
            print(f'A Tabuada de {x} x {j} é {tab}')
    else:
        for l in range(1,x+1):
            som+=l
            print(f'O Somatório é {som}')
    
    