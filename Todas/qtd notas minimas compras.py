# FUAQ lê o valor de compra de um produto. Calcular e mostrar a quantidade mínima de notas com que a compra pode ser paga,
# sabendo-se que o comprador dispõe apenas de notas de R$ 100, R$ 50, R$ 10 e R$ 1.
print('='*30)
print("{:^30}".format("CAIXA ELETRÔNICO"))
print('='*30)
saq=int(input('Insira o Valor a Ser Calculado: '))
vlrorig=saq
if(saq<1 or saq==0):
    print('Valor inválido!')
if(saq>100):
    n100=int(saq/100)
    n100vlr=n100*100
    saq=saq%100
    print('Notas de 100 =',n100,'totalizando R$',n100vlr)
if(saq>50):
    n50=int(saq/50)
    n50vlr=n50*50
    saq=saq%50
    print('Notas de 50  = ',n50,'totalizando R$',n50vlr)
if(saq>20):
    n20=int(saq/20)
    n20vlr=n20*20
    saq=saq%20
    print('Notas de 20  = ',n20,'totalizando R$',n20vlr)
if(saq>10):
    n10=int(saq/10)
    n10vlr=n10*10
    saq=saq%10
    print('Notas de 10  = ',n10,'totalizando R$',n10vlr)
if(saq>1):
    n1=int(saq/1)
    n1vlr=n1*1
    saq=saq%1
    print('Moedas de 1  = ',n1,'totalizando R$',n1vlr)
print('O Valor Original do Saque foi de ',vlrorig)