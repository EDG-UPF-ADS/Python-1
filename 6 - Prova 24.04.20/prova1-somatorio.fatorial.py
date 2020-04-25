# ler X até digitado 0. pra X par calc somat impares entre 1 x.
# para cada x impar, calcular e mostrar fatoreal de X.
x=1
somimp=0
while(x!=0):
    x=int(input('Digite o Valor de X: '))
    if(x==0):
        break
    if(x%2==0):
        for i in range(2,x):
            if(i%2!=0):
                somimp+=i
        print(f'O Somatório de {x} é {somimp}')
    else:
        fatx=1
        for j in range(1,x+1):
            fatx=fatx*j
        print(f'O Fatorial de {x} é {fatx}')
print(f'Você Saiu do Sistema')