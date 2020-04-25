# ler 2 notas, calcule mostre media de cada aluno para 30 alunos.
# final mostrar media semestral mais alta, e a média geral. 
medg=0
for i in range(1,31):
    print('ALUNO',i)
    n1=int(input('nota1 '))
    n2=int(input('nota2 '))
    med=(n1+n2)/2
    print(f'A Média do Aluno {i} é {med}\n')
    medg+=med
    if(i==1):
        maior=med
    if(med>maior):
        maior=med
mgeral=medg/i
print(f'A Média Geral é {mgeral}')
print(f'A Maior Média Individual foi {maior}')