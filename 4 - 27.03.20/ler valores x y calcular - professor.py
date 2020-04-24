cont=0
while(cont<5):
         cont=cont+1
         x=int(input('Digite um valor: '))
         if(x%2==0):
             acum=0
             for i in range(2,x):
                 if(i%2!=0):
                     acum=acum+i
                     print('O somatório dos valores ímpares entre 1 e ',x,' eh: ', acum)
        else:
            # X impar faz tabuada
            for i in range(1,11):
                t=i*x
                print('Tabuada de ',x,'*',i,'=',t)