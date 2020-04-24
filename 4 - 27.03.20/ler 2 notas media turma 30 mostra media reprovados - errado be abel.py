# FUAQ lê as duas notas e calcula a média de cada aluno de uma turma com 30 alunos. No final,
#calcular e mostrar a média das médias das notas dos alunos que reprovaram,
# ou seja, que ficaram com a média das notas menor que 3,0. Utilizar o comando ‘while’
acum=0
a=1
med2=0
while(a<=3):
    print("aluno",a)
    n1=int(input('Digite O Valor de n1 '))
    n2=int(input('Digite O Valor de n2 '))
    med1=(n1+n2)/2
    a=a+1
    if(med1<3):
        acum=acum+1
        med2=med2+med1
result=med2/acum
print("os alunos reporvados são:",acum, "e a media é: ",result)