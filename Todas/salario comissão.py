sal_fix=int(input('Insira o Salário Fixo em R$ '))
ven=int(input('Insira o valor das Vendas em R$ '))
com=ven*0.05
sal_tot=sal_fix+com
print('\nO Salário Fixo é R$ %.0f'%sal_fix)
print('As Comissões são R$ %.0f'%com)
print('Salário Total é R$ %.0f'%sal_tot)