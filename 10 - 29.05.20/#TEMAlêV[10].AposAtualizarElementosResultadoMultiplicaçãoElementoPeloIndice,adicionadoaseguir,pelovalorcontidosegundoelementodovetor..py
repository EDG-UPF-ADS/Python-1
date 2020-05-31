#TEMAlêV[10].AposAtualizarElementosResultadoMultiplicaçãoElementoPeloIndice,adicionadoaseguir,pelovalorcontidosegundoelementodovetor.
v=[0]*10
v1=int
for i in range(10):
    v[i]=int(input(f'Digite o Valor de V{i}: '))
    if(i==1):
        v1=v[i]
for i in range(10):
    v[i]=(v[i]*i)+v1
    print(f'O Valor Atualizado de V{i} é {v[i]}')
    