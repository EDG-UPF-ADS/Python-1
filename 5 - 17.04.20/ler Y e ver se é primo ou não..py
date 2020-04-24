# FUAQ ler Y. Se Y é número primo. Se for, mostrar a mensagem “Eh Primo”.
# e se não for mostrar a mensagem “Nao eh primo”.
div=0
y=int(input('Insira o Numero a Ser Testado: '))
for num in range(1,y):
    if (y%num==0):
        div+=1
if (div>1):
    print(f'O Numero {y} Não é Primo, Pois Existem {div} Divisores')
else:
    print(f'O Numero {y} é Primo')