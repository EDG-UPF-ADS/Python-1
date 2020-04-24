# FUAQ lê valores para 3 variáveis A, B e C. Mostrar os valores em ordem crescente.
a=int(input('Digite o Valor de A: '))
b=int(input('Digite o Valor de B: '))
c=int(input('Digite o Valor de C: '))
if(a>b and a>c):
    if(b>c):
        print('O Valor de A é: ',a)
        print('O Valor de B é: ',b)
        print('O Valor de C é: ',c)
    else:
        print('O Valor de A é: ',a)
        print('O Valor de C é: ',c)
        print('O Valor de B é: ',b)
if(b>a and b>c):
    if(a>c):
        print('O Valor de B é: ',b)
        print('O Valor de A é: ',a)
        print('O Valor de C é: ',c)
    else:
        print('O Valor de B é: ',b)
        print('O Valor de C é: ',c)
        print('O Valor de A é: ',a)
if(c>a and c>b):
    if(a>b):
        print('O Valor de C é: ',c)
        print('O Valor de A é: ',a)
        print('O Valor de B é: ',b)
    else:
        print('O Valor de C é: ',c)
        print('O Valor de B é: ',b)
        print('O Valor de A é: ',a)