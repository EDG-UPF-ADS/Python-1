# aposta 150/ganho*80/3,5% criadores/40hipodromo/1.45%seguro/10%descontado.
pganho=150*80
taxhip=40
assoc=pganho*0.035
segcav=pganho*0.0145
premliq1=pganho-assoc-segcav-taxhip
premliq2=premliq1*0.1
premliq3=pganho-taxhip-assoc-segcav-premliq2
print('Premio Bruto Foi De R$: ',pganho)
print('Associação dos Criadores de Cavalo R$: %.0f'%assoc)
print('Taxa do Hipódromo de R$: ',taxhip)
print('Seguro do Cavalo R$: ',segcav)
print('10%% Sobre o Premio Bruto e Descontos R$: %.2f'%premliq2)
print('Base de Cálculo do Imposto R$: %.2f'%premliq1)
print('Total Liquido de R$: ',premliq3)

