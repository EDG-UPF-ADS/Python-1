#tema-lêXeYdentrofunçãovalidasevalormaior0menor100apóscontaremostrarQTDvlrsparesentre X e Y.
def valida(a):
    while(a<0 or a>100):
        a=int(input('Digite o Valor Novamente: '))
    return(a)
contpar=0;
x=int(input('Digite o Valor de X: '))
y=int(input('Digite o Valor de Y: '))
valx=valida(x)
valy=valida(y)
for i in range (valx,valy):
    if(i%2==0):
        contpar+=1
print(f'A Quantidade de Numeros Pares Entre {valx} e {valy} é {contpar}')