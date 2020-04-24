# FUAQ lê 5 valores para uma variável X.
# Mostrar a média dos valores ímpares digitados para X.
# Utilizar o comando for
medimp=0
acum=0
for i in range(5):
    x=int(input('Digite O Valor de X '))
    if(x%2!=0):
        acum=acum+1
        medimp=medimp+x
if(acum>0):
    medimp=medimp/acum
    print('A Quantidade Impar Digitada foi',acum,'e a Média foi de',medimp)
else:
    print('Não Foram Digitados Numeros Impares')