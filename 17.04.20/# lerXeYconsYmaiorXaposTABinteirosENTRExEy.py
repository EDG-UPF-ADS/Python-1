# lerXeYconsYmaiorXaposTABinteirosENTRExEy
x=int(input('Insira o Numero X: '))
y=x-1
while(y<=x):
    y=int(input('Insira o Numero Y: '))
for i in range(x+1,y):
    for j in range(1,11):
        tab=j*x #mostrar a tabuada dos valores inteiros entre x e y?
    print(f'Numero {j} Multiplicado por {x} é {tab}')
    for l in range(1,11):
        tab=l*y #mostrar a tabuada dos valores inteiros entre x e y?
    print(f'Numero {l} Multiplicado por {y} é {tab}')