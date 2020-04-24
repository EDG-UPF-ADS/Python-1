# FUAQ lê valores para três variáveis X, Y e Z.
# Inicialmente, trocar os valores entre Y e Z.
# Logo após, a variável X deve receber o resultado
# da multiplicação do valor do próprio X pelo valor inicial de Z.
# No final, mostrar as três variáveis lidas.

x=int(input('Digite o Valor de X '))
y=int(input('Digite o Valor de Y '))
z=int(input('Digite o Valor de Z '))
yorig=y
y=z
z=yorig
x=x*y
print('O Valor de X Trocado é',x)
print('O Valor de Y Trocado é',y)
print('O Valor de Z Trocado é',z)