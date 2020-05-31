#lerY5vetorescalcularemostraramediadospares
y=[0]*5
acum=0
pares=0
for i in range(5):
    y[i]=int(input(f'Digite o Valor de Y{i}: '))
for i in range(5):
    if(y[i]%2==0):
        acum+=y[i]
        pares+=1
media=acum/pares
print(f'O Somatório dos {pares} vezes que par foi digitado é {acum}, e a média foi {media}')