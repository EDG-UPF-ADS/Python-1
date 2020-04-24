nome=str(input('Digite o Nome do Aluno: '))
n1=float(input('Digite a Primeira Nota: '))
n2=float(input('Digite a Segunda Nota: '))
med=(n1+n2)/2
if(med>=9.0):
    print('O Aluno',nome,'foi aprovado com Media: ',med)
else:
    print('O Aluno',nome,'foi reprovado com Media: ',med)