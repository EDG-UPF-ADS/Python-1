# FUAQ ler valor para Z. calcular e mostrar o somatório
# dos valores pares entre 1 e z.
z=int(input('Insira um Numero p/ Somatório: '))
acum=0
for i in range(2,z):
    if(i%2==0):
        acum=acum+i
print(acum)