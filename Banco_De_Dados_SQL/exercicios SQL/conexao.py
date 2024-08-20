import sqlite3

conexao = sqlite3.connect('banco') # cria o banco de dados e faz a conexão
cursor = conexao.cursor() # cursor é o objeto que permite interagir com o banco

#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))') # criando a tabela alunos

'''
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "Gustavo", "Rua piiririroro", "gustav@gmail.com")') # insere um registro na tabela alunos
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "Lito", "Rua imagine", "lit@gmail.com")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "Paula", "Rua amd", "paula@gmail.com")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "Ana", "Rua da intel", "ana@gmail.com")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "Kateryne", "Rua piaaririroro", "kate@gmail.com")')
'''

'''
cursor.execute('SELECT * FROM alunos') # seleciona todos os registros da tabela alunos
cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20') # seleciona o nome e a idade dos alunos com mais de 20 anos
cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome ASC') # seleciona os alunos do curso de "Engenharia" em ordem alfabética
cursor.execute('SELECT COUNT(*) FROM alunos') # conta o número total de alunos na tabela

cursor.execute('UPDATE alunos SET idade = 21 WHERE nome = "Gustavo"') # atualiza a idade do aluno com nome Gustavo
cursor.execute('DELETE FROM alunos WHERE id = 1') # deleta o aluno com id 1

'''

#cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)') # criando a tabela clientes
'''
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (1, "Gustavo", 21, 1000.00)') # insere um registro na tabela clientes
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (2, "Lito", 22, 2000.00)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (3, "Paula", 23, 3000.00)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (4, "Ana", 24, 4000.00)')
'''
cursor.execute('FROM clientes (saldo) ') # calcula o saldo medio dos clientes

visu = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 20') # seleciona o nome e a idade dos clientes com mais de 20 anos

for usuarios in visu:
    print(usuarios) # imprime o resultado da consulta

conexao.commit() # salva as alterações no banco e envia
conexao.close() # fecha a conexão com o banco e evita conflitos


