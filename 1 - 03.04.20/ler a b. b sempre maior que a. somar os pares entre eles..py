# ler a e b. consistir para que B seja maior que A. Após, mostrar a soma dos pares entre A e B.
soma=0
a=int(input('Insira o Valor de A: '))
b=a-1
while(a>=b):
    b=int(input('Insira o Valor de B: '))
for i in range(a,b):
    if(i%2==0):
        soma+=i
print(f'Os Pares Entre {a} e {b} somam {soma}')