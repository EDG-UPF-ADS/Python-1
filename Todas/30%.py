y=int(input('Digite o Número Desejado:'))
print('Você Digitou',y)
p1=int(input('Digite a Porcentagem Desejada:'))
print('Você Digitou',p1)
p2=int(input('Digite a Porcentagem da Porcentagem Desejada:'))
print('Você Digitou',p2)
totporcent=(p1 *0.1)*p2*0.1
print('Porcentagem total de',totporcent,'%')
calc2=totporcent*0.01
print('O algorítmo da porcentagem total é',calc2)
calc=y*calc2
if(calc>(y*0.5)):
    print('Os',totporcent,'% do Número Equivale a ',calc,' e são MAIORES que sua metade')
else:
    print('Os',totporcent,'% do Número Equivale a ',calc,' e são MENORES que sua metade')
if(calc==(y*0.5)):
    print('Os',totporcent,'% do Número Equivale a ',calc,' e equivale a METADE')
