# FUAQ le um valor para uma variavel X. calcular e mostrar o somatório dos numeros inteiros existentes entre 1 e x.
# utilizar comando for. inteiros entre 1 e 7 são 2 3 4 5 6 pois é ENTRE. 
# ler valor pra X depois criar um for que vá de 2 até 6 e vai acumulando os valores e depois mostra o resultado. com o 7 tem que dar 20.
num=int(input('Insira um Numero Inteiro: '))
cont=0
for i in range (2,num):
    cont=cont+i
print(cont)