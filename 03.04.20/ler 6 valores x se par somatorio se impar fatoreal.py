cont=0
while (cont<6):
    x=int(input('Digite o Valor de X: '))
    if(x%2==0):
        acum=0
        for i in range(2,x):
            if(i%2!=0):
                acum=acum+i
        print(f'Somatório: {acum}')
    else:
        f=1
        for i in range(1,x+1):
            f=f*i
        print(f'Fatorial é {f}')
    cont+=1
print('Programa Finalizado')
    