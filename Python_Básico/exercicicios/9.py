'''
Mensagem Amigável: Faça um programa que utilize 4 variáveis como preferir e no final printe uma mensagem amigável utilizando as variáveis criadas. Exemplos de variáveis: nome, idade, lugar, profissão.

Exemplo de retorno: "Olá Maria, prazer te conhecer. Sou de São Paulo também e estou migrando de área." (Lembrando que para o retorno vamos usar print com as variáveis criadas e este texto é somente um exemplo, utilize a criatividade).
'''

nome = str(input('Qual o seu nome? ')).capitalize()
idade = int(input('Qual a sua idade? '))
lugar = str(input('Qual o seu lugar favorito? ')).capitalize()
profissao = str(input('Qual sua profissão?')).capitalize()

print(f'Olá {nome}, prazer lhe conhecer! sua idade é {idade} anos! vi aqui que o seu lugar favorito é {lugar} e sua profissão é {profissao}! ')
