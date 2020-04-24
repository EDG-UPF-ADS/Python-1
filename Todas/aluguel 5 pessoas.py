# divisões: joão 50% / pedro 25% / maria 10% / luiza 10%  / valmor 5%
aluguel=float(input('Digite o Valor do Aluguel em R$: '))
joao=aluguel*0.5
pedro=aluguel*0.25
maria=aluguel*0.1
valmor=aluguel*0.05
luiza=maria
total=joao+pedro+maria+valmor+luiza
print('\nA Parte do João é de R$: %.0f'%joao)
print('A Parte do Pedro é de R$: %.0f'%pedro)
print('A Parte do Valmor é de R$: %.0f'%valmor)
print('A Parte da Maria é de R$: %.0f'%maria)
print('A Parte da Luiza é de R$: %.0f'%luiza)
print('\nSomatório Total Igual á R$: %.0f'%total)