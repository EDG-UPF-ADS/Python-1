#testeprofessor-primeiroexerDEF
def fatorial(nro):
    h=1
    for i in range(1,nro+1):
        f=f*i
    return(f)
def somatorio(val):
    acum=0
    for i in range (2,val):
        acum=acum+i
    return(acum)
x=int(input('Digite Valor de X: '))
if(x%2==0):
    res=fatorial(x)
    print(f'O Fatorial de {x} é {res}')
else:
    sol=somatorio(x)
    print(f'O Somatório entre 1 e {x} é {sol}')