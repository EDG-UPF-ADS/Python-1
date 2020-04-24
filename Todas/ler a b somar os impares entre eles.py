# ler a e b. após calcular e mostrar a soma dos impares entre A e B.
soma=0
a=int(input('Digite o Valor de A: '))
b=int(input('Digite o Valor de B: '))
for i in range(a+1,b):
    if(i%2!=0):
        soma+=i
print(f'A Soma dos Inteiros Ímpares Entre {a} e {b} é de {soma}')
