# ler salario e linhas codificador durante mes. OK.
# salario + comissão. 10% se for =<20.000. OK
# se for >20.0000 até <50.0000 ganha 15%. OK
# se for >=50.000 ganha 20% do salário. OK
# salario liq calculado bruto + comissão. OK
# imposto 27% salfixo + 50% comissão. OK
# mostrar comissão, bruto, imposto e liquido.
salfix=float(input('Insira Salário Fixo: '))
linhas=float(input('Insira as Linhas Programadas '))
if(linhas<=20000):
    comlinha=salfix*0.1
if(linhas>20000 and linhas<50000):
    comlinha=salfix*0.15
if(linhas>=50000):
    comlinha=salfix*0.2
salliq=salfix+comlinha
salliqimp=comlinha/2
imposto=(salfix+salliqimp)*0.27
salfinal=salfix-imposto
print('A Comissão é de R$ ',comlinha)
print('O Salário Bruto é de R$ ',salfix)
print('O Imposto é de R$ ',imposto)
print('O Valor Liquido é de R$ ',salfinal)