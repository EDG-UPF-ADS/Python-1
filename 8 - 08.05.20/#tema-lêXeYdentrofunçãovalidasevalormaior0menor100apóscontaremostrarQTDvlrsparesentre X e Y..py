#tema-lêXeYdentrofunçãovalidasevalormaior0menor100apóscontaremostrarQTDvlrsparesentre X e Y.
def validax(a):
    while(a<0 or a>100):
        a=int(input('Digite o Valor de X Novamente: '))
    return(a)
def validay(b):
    while(b<0 or b>100):
        b=int(input('Digite o Valor de Y Novamente: '))
    return(b)
contpar=0;
x=int(input('Digite o Valor de X: '))
y=int(input('Digite o Valor de Y: '))
valx=validax(x)
valy=validay(y)
for i in range (valx,valy):
    if(i%2==0):
        contpar+=1
print(f'A Quantidade de Numeros Pares Entre {valx} e {valy} é {contpar}')
    