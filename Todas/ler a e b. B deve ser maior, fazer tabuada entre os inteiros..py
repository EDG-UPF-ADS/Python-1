# valores a e b. b sempre maior que a.
# mostrar tabuada de 1 a 10 dos pares inteiros
# entre A e B.
a=int(input('Digite o Valor de A: '))
b=a-1
while(b<a):
    b=int(input('Digite o Valor de B: '))
for i in range(a,b+1):
    if(i%2==0):
        for j in range(1,11):
            tab=j*i
            print(f'A Tabuada dos Pares entre {a} e {b} é {j} X {i} = {tab}')