# FUAQ le um valor para vairável Y. calcular e mostrar o fatorial de Y. 
# fatorial é multiplicação até chegar no numero. 5 é 1*2*3*4*5=120.
num=int(input('Insira um Numero p/ Fatoreal: '))
cont=1
for n in range(1,num+1):
    cont=cont*n
    print(cont)