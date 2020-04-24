# FUAQ le salario fixo e valor de vendas mes.
# 5% se vendeu + 20mil. senão 2%
sal=float(input('Digite o Salário '))
ven=float(input('Digite as Vendas '))
if(ven>20000):
    com=ven
    com2=(com*0.05)
else:
    com=ven
    com2=com*0.02
tot=com2+sal
print('O Salário total com é de ',tot)
print('A Comissão foi de ',com2)