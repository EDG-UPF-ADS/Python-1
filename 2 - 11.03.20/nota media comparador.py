n1=float(input('Nota da Primeira Prova '))
n2=float(input('Nota da Segunda Prova '))
med=(n1+n2)/2
if(med>=7.0):
    print('Aprovado com Nota ',med)
if(med>=3.0 and med<7.0):
    print('Em Exame por ter',med)
if(med<3.0):
    print('Reprovado por ter',med)

