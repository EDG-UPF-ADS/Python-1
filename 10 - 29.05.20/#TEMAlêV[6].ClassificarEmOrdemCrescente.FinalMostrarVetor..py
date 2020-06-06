#TEMAlêV[6].ClassificarEmOrdemCrescente.FinalMostrarVetor.
#ESTA ERRADA. NAO CONSEGUI TERMINAR. FALTOU TEMPO. 
v=[0]*4
v1=int
v2=int
v3=int
v4=int
for i in range(4):
    v[i]=int(input(f'Digite o Valor de V{i}: '))
    if(i==0):
        v1=v4=v[i]
    if(v1>v[i]):
        v1=v[i]
    if(v[i]>v1 and v[i]<v4):
        v2=v[i]
    if(v4<v[i]):
        v4=v[i]
#for i in range(4):
#    if(v[i]>v1 and v[i]<v3):
#        v2=v[i]
#    if(v[i]<v4 and v[i]>v2):
#        v3=v[i]
print(f'Valores em Ordem: {v1}, {v2}, {v3}, {v4}')