qtd_h=int(input('Quantidade de Horas:'))
vlr_h=int(input('Valor das Horas:'))
slr_bruto=qtd_h*vlr_h
imposto=(slr_bruto*0.27)
slr_liquido=slr_bruto-imposto
print('\nO Salário Bruto é de R$ %.0f'%slr_bruto)
print('O Salário Líquido é de R$ %.0f'%slr_liquido)
print('O Valor do Imposto é de R$ %.0f'%imposto)