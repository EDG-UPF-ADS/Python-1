# ler 3 variáveis A B C.
# se a soma menor 100 ou maior 200 trocar A e B.
# se não, trocar A e C.
# no final mostrar as 3 variáveis lidas.
a=int(input('Digite o Valor de A '))
b=int(input('Digite o Valor de B '))
c=int(input('Digite o Valor de C '))
soma=a+b+c

if(soma<100 or soma>200):
    aorig=a
    borig=b
    a=b
    b=aorig
else:
    aorig=a
    corig=c
    a=c
    c=aorig
print('A Variável A é',a)
print('A Variável B é',b)
print('A Variável C é',c)