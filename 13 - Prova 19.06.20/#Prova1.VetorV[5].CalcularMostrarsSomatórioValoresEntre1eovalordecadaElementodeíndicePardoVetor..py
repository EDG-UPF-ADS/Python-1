#Prova1.VetorV[5].CalcularMostrarsSomatórioValoresEntre1eovalordecadaElementodeíndicePardoVetor.
#CálculoSomatórioRealizadoFunção.ResultadoMostradoProgramaPrincipal.
def somatorio(nro):
    s=0
    for i in range(2,nro):
        s+=i
    return(s)
v=[0]*5
somat=int
acum=0
for i in range(5):
    v[i]=int(input(f'Digite Valores de V{i}: '))
for i in range(5):
    if(i%2==0 and i!=0):
        somat=somatorio(v[i])
        print(f'O Somatório do Indice {i} sendo o Valor {v[i]} é {somat}')