#TEMAlêV[8].ler5valoresparaXnãoévetor.VerificarparacadaXlidosevalorestánovetorVounão.Seestivermensagem“Esta”.Senãomensagem“Não está”.Nofinal,mostrarquantosXestavamnovetor.
v=[0]*8
valor=int
posic=int
acum=int
acum=0
for i in range(8):
    v[i]=int(input(f'Digite o Valor de v{i+1}: '))
for i in range(5):
    x=int(input(f'Digite o Valor de X: '))
    valor=0
    posic=0
    for j in range(8):
        if (x==v[j]):
            valor=x
            posic=j
            acum+=1
    if(valor==0 and posic==0):
        print(f'Não Esta no Vetor')
    else:
        print(f'O Valor {valor} esta no Vetor V{posic+1}')
print(f'O Total de Vezes Que X esta no Vetor é {acum}.')
        