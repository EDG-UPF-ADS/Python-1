# LERvalKate0consisSEMnegKcadaKparSOMATimp1eK
# provavelmente com ERRO. 
k=-1
while(k!=0):
    while(k<0):
        k=int(input('Digite o Valor de K '))
    if(k%2==0):
        som=0
        for i in range(2,k):
            if(i%2!=0):
                som+=i
        print(f'O Somatório é {som}')
    k=-1