#calcularmostrarsomavaloresterceiracoluna.
w=[[0 for i in range(4)]for i in range(2)]
acum=0
for l in range(2):
    for c in range(4):
        w[l][c]=int(input(f'Digite Valores {l}{c}: '))
for i in range(2):
  acum+=w[i][2]
print(acum)