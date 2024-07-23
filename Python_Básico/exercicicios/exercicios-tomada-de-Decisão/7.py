'''
Desenvolver um programa que solicite a idade do usuário e identifique se ele é uma criança, um adolescente, adulto ou idoso.
'''

idade = int(input('Digite sua idade: '))

if idade < 12:
    print('Você é considerado uma criança')
elif idade < 18:
    print('Você é considerado adolescente')
elif idade < 50:
    print('Você é considerado adulto')
else:
    print('Você é considerado idoso')
