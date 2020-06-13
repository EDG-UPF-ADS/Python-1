#temasomatoriodiagonalprincipal.
x=[[0 for i in range(4)] for i in range(4)]
for l in range (4):
    for c in range (4):
        x[l][c]=int(input('Digite o Valor da Matriz: '))
diagprinc=0
for i in range (4):
    diagprinc+=x[i][i]
print(f'O somatorio deu:{diagprinc}') 