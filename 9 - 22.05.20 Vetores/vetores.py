# começamos vetores.
A=[0]*3
B=[0]*3
C=[0]*3
for i in range(3):
    A[i]=(input(f'Digite o Valor de A{i+1}: '))
    B[i]=(input(f'Digite o Valor de B{i+1}: '))
for i in range(3):
    C[i]=A[i]-B[i]
for i in range (3):
    print(f'o C vale {C[i]}')        