def soma(num_1, num_2): # definição da função soma
  calculo = num_1 + num_2
  print(f'O Resultado da soma é: {calculo}')

def subtracao(num_1, num_2):
  sub = num_1 - num_2
  print(f'O resultado da subtração é {sub}')
#  multiplicacao() # função sendo chamada dentro de uma outra função
def multiplicacao(num_1, num_2):
  mult =num_1 * num_2
  print(f'O resultado da multiplicação é: {mult}')

# chamada da função
#soma()
#subtracao()
#multiplicacao()

'''
treinando funções com parametros:
'''

num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))
soma(num_1, num_2)
subtracao(num_1, num_2)
multiplicacao(num_1, num_2)

'''
Manipulando arquivos:
'''

file = 'arquivo.txt' # abertura de arquivo
arquivo_leitura = open(file, "r") #abertura somente para leitura
arquivo_escrito = open(file, "w") # abertura para escrita
arquivo_escrito.write("Texto a ser escrito")
arquivo_binario = open(file, "wb") # abertura de arquivos binarios

