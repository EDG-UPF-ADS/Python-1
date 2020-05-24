#lerV5.lerXverficarseXestanovetor.Sesimmostraraposiçao.senãomostrarnãoesta.
V=[0]*5
for i in range(5):
    V[i]=int(input(f'Digite o Valor de V{i+1}: '))
x=int(input(f'Digite o Valor de X: '))
status=0
for i in range(5):
    if(x==V[i]):
        status=1
        print(f'o X que é "{V[i]}" esta presente no Vetor V{[i+1]}.')
if(status==0):
    print('X não esta no Vetor')