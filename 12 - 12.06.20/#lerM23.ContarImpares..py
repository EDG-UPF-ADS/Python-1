#lerM23.ContarImpares.
m=[[0 for i in range(3)]for i in range(2)]
imp=0
for l in range(2):
    for c in range(3):
        m[l][c]=int(input(f'Digite Valores de M{l}{c}: '))
for l in range(2):
    for c in range(3):
        if(m[l][c]%2==1):
            imp+=1
if(imp!=0):
    print(f'Foram Digitados {imp} Numeros Impares na Matriz')
else:
    print(f'Não Houveram Impares Digitados')
