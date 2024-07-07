'''
Cálculo de Idade: Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual.
'''
from datetime import datetime

# Obter o ano atual
ano_atual = datetime.now().year

pergunta = int(input('Informe seu Ano de Nascimento: '))
calculo = ano_atual - pergunta
print(f'Sua Idade é: {calculo}')