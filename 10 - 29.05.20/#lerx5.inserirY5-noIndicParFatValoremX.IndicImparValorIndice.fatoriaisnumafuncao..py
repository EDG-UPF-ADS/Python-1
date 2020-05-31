#lerx5.inserirY5-noIndicParFatValoremX.IndicImparValorIndice.fatoriaisnumafuncao.
def fatorial(nro):
    f=1
    for i in range(1,nro+1):
        f=f*i
    return(f)
x=[0]*5
y=[0]*5
for i in range(5):
    x[i]=int(input(f'Digite o Valor de X{i}: '))
for j in range(5):
    if(j%2==0):
        y[j]=fatorial(x[j])
    else:
        y[j]=j
for i in range(5):
    print(f'X é {x[i]} e Y é {y[i]}')