#TEMAlêvetorW20.TrocarValor1ElementoCom11ºElemento2ºcom12ºaté10ºcom20º.NofinalmostrarvetorW.
w=[0]*20
for i in range (20):
    w[i]=int(input(f'Digite Valores para o Vetor W{i+1}: '))
for i in range (10):
    x=w[i]
    w[i]=w[i+10]
    w[i+10]=x
for i in range (20):
 print(w[i])