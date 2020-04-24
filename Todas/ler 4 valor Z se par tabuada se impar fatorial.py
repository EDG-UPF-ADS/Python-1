# ler 4 valores Z verificar par ou impar.
# se par mostrar tabuada 1 até 10 de z.
# se impar mostrar fatoreal de z.
for i in range(4):
    z=int(input('Digite o Valor de Z: '))
    if(z%2==0):
        for t in range(1,11):
            tab=z*t
            print(f'Tabuada de {z} vezes {t} é igual á {tab}')
    else:
        f=1
        for c in range(1,z+1):
            f=f*c
        print(f'O Fatoreal é {f}')
print('Logaritmo Finalizado')
                