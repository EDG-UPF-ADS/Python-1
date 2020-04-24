# ler indet x. ate 0. sem poder aceitar negativos.
# final mostrar a media  dos resultados dos fatoriais
# dos valores pares digitados de x.
acum=0
cont=0
x=-1
while(x!=0):
    x=int(input('Digite o Valor de X: '))
    if(x<0):
        input('Valor Negativo - Inválido')
    else:
        if(x%2==0 and x!=0):
            f=1
            for i in range(1,x+1):
                f=f*i
            acum+=f
            cont+=1
media=acum/cont
print(f'A Média foi de {media}')