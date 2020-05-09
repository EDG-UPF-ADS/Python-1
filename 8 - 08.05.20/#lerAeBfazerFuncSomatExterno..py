#lerAeBfazerFuncSomatExterno.
def somatorio(x):
    somat=0
    for i in range(1,x):
        somat+=i
    return(somat)
a=int(input('Digite A: '))
b=int(input('Digite B: '))
if(a%2==0):
    ret=somatorio(a)
    print(f'A par B indif. O Somatório entre 1 e {a} é {ret}')
if(a%2!=0 and b%2==0):
    ret=somatorio(b)
    print(f'A impar B par. O Somatório entre 1 e {b} é {ret}')
if(a%2!=0 and b%2!=0):
    soma=a+b
    ret=somatorio(soma)
    print(f'A e B impar. O Somatório entre 1 e {soma} é {ret}')