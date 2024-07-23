'''
Criar um programa em Python que solicite três números ao usuário, utilize estruturas condicionais para determinar o maior entre eles e apresente o resultado.

'''

numero_1 = int (input('Digite o primeiro numero '))
numero_2 = int (input('Digite o segundo numero '))
numero_3 = int (input('Digite o terceiro numero '))

if numero_1 > numero_2 and numero_2 > numero_3:
    print(f'O maior número é: {numero_1}')
elif numero_2 > numero_3:
    print(f'O maior número é {numero_2}')

else:
    print(f'O maior número é {numero_3} ')