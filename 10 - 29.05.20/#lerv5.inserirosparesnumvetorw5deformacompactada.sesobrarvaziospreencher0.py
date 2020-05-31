#lerv5.inserirosparesnumvetorw5deformacompactada.sesobrarvaziospreenchercomindice.
v=[0]*5
w=[0]*5
j=0
for i in range(5):
    v[i]=int(input(f'Digite o Valor de V{i}: '))
for i in range(5):
    if(v[i]%2==0 and v[i]!=0):
        w[j]=v[i]
        j+=1
for j in range (j, 5):
    w[j]=j
for i in range(5):
    print(f'V é {v[i]} e W é {w[i]}')
