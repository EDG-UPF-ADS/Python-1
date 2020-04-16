# FUAQ qtd indeterminada valores X. Quando for digitado o décimo valor PAR para X,
# encerrar a leitura e calcular e mostrar a média dos valores ímpares digitados para X.
soma=0
contpar=0
contimpar=0
while(contpar<10):
    x=int(input('Digite o Valor de X: '))
    if(x%2==0):
        contpar+=1
    else:
        contimpar+=1
        soma+=x
soma=soma/contimpar
print(f'A Média dos Numeros Ímpares foi de {soma}')