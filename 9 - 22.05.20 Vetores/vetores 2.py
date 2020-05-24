# laços A e B e C.
A=[0]*3
B=[0]*3
C=[0]*6
for i in range(3):
    A[i]=(input(f'Digite o Valor de A{i+1}: '))
for i in range(3):
    B[i]=(input(f'Digite o Valor de B{i+1}: '))
for i in range(3):
    C[i]=A[i]
for i in range(3,6):
    C[i]=B[i-3]
for i in range (6):
    print(f'o C{i+1} vale {C[i]}')        