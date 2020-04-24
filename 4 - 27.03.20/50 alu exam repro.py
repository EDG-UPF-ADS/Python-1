# FUAQ lê duas notas calcula média para cada aluno de uma turma com 50 alunos.
# Final mostrar quantos alunos ficaram em exame (média maior ou igual a 3,0 e menor que 7,0)
aluexam=0
alurepro=0
med=0
alu=0
for i in range (50):
    alu=alu+1
    print('Insira a Nota do Aluno ',alu)
    n1=int(input('Insira a N1: '))
    n2=int(input('Insira a N2: '))
    med=(n1+n2)/2
    if(med>=3 and med<7):
        aluexam=aluexam+1
    if(med<3):
        alurepro=alurepro+1
print('A quantidade de Reprovados foi ',alurepro,'e em exame ',aluexam)
