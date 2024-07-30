'''
Manipulando arquivos:
'''

file = 'arquivo.txt' # abertura de arquivo
arquivo_leitura = open(file, "r") #abertura somente para leitura
arquivo_escrito = open(file, "w") # abertura para escrita

arquivo_escrito.write("Texto a ser escrito!!")
#arquivo_escrito.close()
arquivo_binario = open(file, "wb") # abertura de arquivos binarios

# Leitura:

#leitura = arquivo_escrito.read()
#arquivo_leitura.close()