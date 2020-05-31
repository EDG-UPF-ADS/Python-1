#lerx5.mediadosimpar.mediadospares.quantidadede5.
x=[0]*5
acumpar=0
acumimpar=0
pares=0
impares=0
qtd5=0
for i in range(5):
    x[i]=int(input(f'Digite o Valor de X{i}: '))
for i in range(5):
    if(i%2==1): # aqui testa pra indice impar 
        acumimpar+=x[i] #acumula o valor da variavel no indice impar
        impares+=1 # acumula a quantidade de indices impares
    if(x[i]%2==0): # testa pra variavel par
        acumpar+=x[i] # acumula o valor das variaveis pares
        pares+=1 # acumula a quantidade de variaveis pares
    if(x[i]==5): # verifica se a variavel é 5.
        qtd5+=1 # acumula a quantidade de variaveis 5
mediaindimpar=acumimpar/impares
mediapar=acumpar/pares
print(f'O Somatório dos {pares} vezes que par foi digitado é {acumpar}, e a média foi {mediapar}')
print(f'A Média dos Valores nos Indices Impares é {mediaindimpar}')
print(f'A Quantidade Digitada do Número 5 foi {qtd5}')