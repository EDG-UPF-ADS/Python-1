# FUAQ quantidade indeterminada de valores variável Y até que seja digitado 0 (zero).
# Quando zero, encerrar a leitura e calcular e mostrar a média dos valores pares de Y.
# Utilizar o comando while.
medpares=0
acum=0
y=1
while(y>0):
         y=int(input('Digite O Valor de Y '))
         if(y%2==0 and y!=0):
             acum=acum+1
             medpares=medpares+y
medpares=medpares/acum
print('A Quantidade Par Digitada foi',acum,'e a Média dos Pares foi de',medpares)
