#ler o nome de 4 alunos e suas notas
#informar qual aluno possui a maior nota

notas = []
nomes = []
nota_maior = float(0)
for i in range (4):
    nomes_alunos = str(input("Informe o nome do aluno"))
    nomes.append(nomes_alunos)
    notas_alunos = float(input("informe a nota do aluno"))
    notas.append(notas_alunos)
    
    if notas[i] > nota_maior:
        nota_maior = notas_alunos
        aluno_com_nota_maior = nomes_alunos
        
print("A nota maior foi: ", {nota_maior})
print("Aluno: ", {aluno_com_nota_maior})
