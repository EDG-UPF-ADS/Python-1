# FUAQ ler 5 valores para x. verificar cada X se é par ou impar. 
# se PAR calcular e mostrar o somatório dos impares entre 1 e x cada vez.
# se X impar calcular e mostrar tabuada de 1 até 10 de x. 
contx=0
ximpar=0
xpar=0
while (contx<5):
    contx=contx+1
    x=int(input('Insira um Numero p/ X '))
    if(x%2==0):
        for i in range(2,x):
            ximpar=ximpar+x
    if(x%2==1):
        for i in range (1,x):
            print('A Tabuada do',x,'é',x*i)
print(xpar)
print(ximpar)