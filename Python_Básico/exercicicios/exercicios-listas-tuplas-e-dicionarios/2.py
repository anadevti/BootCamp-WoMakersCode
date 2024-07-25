'''
 Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0.


'''


'''
quebrando em pequenas partes:

 -  coletar quatro notas para cada um dos cinco alunos. ok 
 -  calcular a média dessas notas e armazenar essa média em uma lista
 

'''

notas_todos_alunos = []
alunos_media_alta = 0  # Contador para alunos com média >= 7.0

for aluno in range(1, 6): # Loop para iterar sobre os 5 alunos
    notas_aluno = []  # Lista para armazenar as notas de um único aluno, conforme o user vá adicionando

    for nota in range(1, 5):  # Loop para iterar sobre as 4 notas de cada aluno
        nota_atual = (input(f"Digite a nota {nota} do aluno {aluno}: "))
        notas_aluno.append(float(nota_atual))

    # Calcula a média das notas do aluno
    media = sum(notas_aluno) / 4
    if media >= 7.0:
        alunos_media_alta += 1

    # Adiciona as notas do aluno atual à lista de todos os alunos
    notas_todos_alunos.append(notas_aluno)

# Exibe as notas de todos os alunos e a média
for i, notas_aluno in enumerate(notas_todos_alunos, start=1):
    media = sum(notas_aluno) / 4
    print(f"Notas do aluno {i}: {notas_aluno}, Média: {media:.2f}")

# Imprime o número de alunos com média maior ou igual a 7.0
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_media_alta}")

