# lerXverifSExEnumeroPERFEITOseFORmostrarEperfeito2
perf=0
x=int(input('Digite o X: '))
for i in range(1,x):
    if(x%i==0):
        perf+=i
if(perf==x):
    print(perf)