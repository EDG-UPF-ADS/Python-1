#Prova2.v[10].EncontrarMostrar:
#(a) o maior valor e sua posição e (b) a média dos valores pares existentes nos elementos de índice ímpar.
v=[0]*10
maior=0
mediapar=0
somatpar=0
qtdpar=0
for i in range(10):
    v[i]=int(input(f'Digite Valores de V{i}: '))
    if(i==0):
        maior=v[i]
        pos=i
    if(maior<v[i]):
        maior=v[i]
        pos=i
    if(i%2!=0):
        if(v[i]%2==0 and v[i]!=0):
            somatpar+=v[i]
            qtdpar+=1
print(f'O Maior Valor Digitado Foi {maior} na posição {pos} do Vetor')
if(qtdpar!=0):
    mediapar=somatpar/qtdpar
    print(f'A Média dos {qtdpar} Numero Pares Digitados nos Indices Impares é {mediapar}')
else:
    print('Não Foram Digitados Números Pares nos Indices Impares')