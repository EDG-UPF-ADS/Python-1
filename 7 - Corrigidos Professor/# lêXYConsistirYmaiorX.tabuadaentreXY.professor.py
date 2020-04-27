x=int(input('Insira X: '))
y=x-1
while(y<=x):
    y=int(input('Insira Y: '))
for i in range (x+1,y):
    for j in range(1,11):
        t=j*i
        print(t)