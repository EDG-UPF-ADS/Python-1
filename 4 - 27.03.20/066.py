# 066 - varios numeros inteiros teclado. para quando digitar 999.
# mostre quandos digitados e qual a soma desconsiderando a FLAG.
acum=0
som=0
while True:
    n=int(input('Digite um Numero '))
    if(n==999):
        break
    som+=n
    acum+=1
print(f'Foram Digitados {acum} Números e o Somatório foi de {som}') 