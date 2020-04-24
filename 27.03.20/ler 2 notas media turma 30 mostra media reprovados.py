# FUAQ lê duas notas e calcula a média de cada aluno de uma turma com 30 alunos.
# Calcular e mostrar a média das médias das notas dos alunos que reprovaram.
# Ou seja, que ficaram com a média das notas menor que 3,0. Utilizar o comando ‘while’
acum=0
a=1
medrep=0
while(a<=3):
    print("aluno",a)
    n1=int(input('Digite O Valor de n1 '))
    n2=int(input('Digite O Valor de n2 '))
    med=(n1+n2)/2
    a=a+1
    if(med<3):
        acum=acum+1
        medrep=medrep+med
if(acum>0):
    result=medrep/acum
    print(f"Os Reprovados são: {acum} e a media é: {result}")
else:
    print('Não Houveram Alunos Reprovados') 