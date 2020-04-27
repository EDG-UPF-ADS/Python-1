for i in range(5):
    w=int(input('Digite Valor do W: '))
    if(w%2==0):
        for j in range(1,w+1):
            t=w*j
            print(t)
    else:
        f=1
        for j in range(1,w+1):
            f=f*j
        print(f)
