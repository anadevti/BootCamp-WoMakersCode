import sqlite3

conexao = sqlite3.connect('banco') # cria o banco de dados e faz a conexão
cursor = conexao.cursor() # cursor é o objeto que permite interagir com o banco


#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100))') # cria a tabela usuarios

#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100))')

#cursor.execute(('ALTER TABLE usuarios RENAME TO usuario')) # renomeia a tabela usuarios para usuario
#cursor.execute('ALTER TABLE usuarios ADD COLUMN telefoni INT') # adiciona a coluna telefone na tabela usuario
#cursor.execute('ALTER TABLE usuarios RENAME COLUMN telefoni TO telefone') # renomeia a coluna telefoni para telefone)

#cursor.execute('DROP TABLE produtos') # deleta toda a estrutura da tabela produtos

cursor.execute('INSERT INTO gerente (id, nome, endereco, email) VALUES (1, "João", "Rua 1", "ana@gmail.com")') # insere um registro na tabela usuario
#cursor.execute('INSERT INTO usuarios (id, nome, endereco, email, telefone) VALUES (2, "aninha", "Rua 2", "ana@gmail.com",22332334 )') # insere um registro na tabela usuario
#cursor.execute('INSERT INTO usuarios (id, nome, endereco, email, telefone) VALUES (3, "ana", "Rua 3", "ana@gmail.com",22232234 )') # insere um registro na tabela usuario
#cursor.execute('INSERT INTO usuarios (id, nome, endereco, email, telefone) VALUES (4, "gabriel", "Rua 4", "ana@gmail.com",22662334 )') # insere um registro na tabela usuario

#cursor.execute('DELETE FROM usuarios WHERE id = 1') # deleta o registro com id 4 da tabela usuario
#cursor.execute('UPDATE usuarios SET endereco="minas gerais" WHERE nome = "aninha"') # atualiza o registro com id 2 da tabela usuario


# ORDER BY e DESC, ASC:
#visu = cursor.execute('SELECT * FROM usuarios ORDER BY nome ASC') # seleciona todos os registros da tabela usuario


#LIMIT e DISTINCT:
#visu = cursor.execute('SELECT DISTINCT nome FROM usuarios LIMIT 2') # seleciona todos os registros da tabela usuario e limita a 2 registros


# Join's:

#cursor.execute('CREATE TABLE gerente(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100))') # cria a tabela usuarios

# INNER JOIN:

# GROUP BY (agrupar informações) e HAVING (UTILIZADO PARA FILTRAR OS REGISTROS AGRUPADOS):
#visu = cursor.execute('SELECT * FROM usuarios LEFT JOIN gerente ON usuarios.id = gerente.id')

# SUB QUERY:
visu = cursor.execute('SELECT * FROM usuarios WHERE nome IN (SELECT nome FROM gerente)')


for usuarios in visu:
    print(usuarios) # imprime o resultado da consulta




conexao.commit() # salva as alterações no banco e envia
conexao.close() # fecha a conexão com o banco e evita conflitos