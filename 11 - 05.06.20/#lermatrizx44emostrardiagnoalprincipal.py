#lermatrizx44emostrardiagnoalprincipal
x=[[0 for i in range(4)]for i in range(4)]
diagprinc=0
for l in range(4):
    for c in range(4):
        x[l][c]=int(input(f'Digite Valores {l}{c}: '))
for l in range(4):
    for c in range(4):
        if(l==c):
            diagprinc+=x[l][c]
print(diagprinc)