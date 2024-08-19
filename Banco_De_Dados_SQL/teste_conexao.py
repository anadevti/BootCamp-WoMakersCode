import sqlite3

conexao = sqlite3.connect('banco') # cria o banco de dados e faz a conexão
cursor = conexao.cursor() # cursor é o objeto que permite interagir com o banco


cursor.execute('')

conexao.commit() # salva as alterações no banco e envia
conexao.close() # fecha a conexão com o banco e evita conflitos