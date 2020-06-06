#lermatrizM23.lerXverificaseestaMatriz.seSIMmostrarLeC.senão"NaoEsta". 
m=[[0 for i in range(3)]for i in range(2)]
for l in range(2):
    for c in range(3):
        m[l][c]=int(input(f'Digite Valores {l}{c}: '))
xmatriz=0
x=int(input('Insira Valor de X: '))
for l in range(2):
    for c in range(3):
        if(x==m[l][c]):
            print(f'X Esta na Posição {l}{c} da Matriz')
            xmatriz=1
if(xmatriz==0):
    print(f'O Valor {x} Não Esta na Matriz')