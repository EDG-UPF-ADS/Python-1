#lerMeNcalcMmultNnumaFuncResultProgrPrincip
def calculo(x,y): # recebeu m e n na sequencia. 
    mult=x*y
    return(mult)
m=int(input('Digite M: ')) # 1 - programa começa aqui... 
n=int(input('Digite N: ')) # 2 - ler aqui depois
ret=calculo(m,n) # 3 - passa lá pra cima M vira x e N vira y 
print(f'O Resultado de {m}*{n} é {ret}')
