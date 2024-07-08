'''
Índice de Massa Corporal (IMC): Solicite ao usuário o peso em kg e a altura em metros. Calcule e imprima o IMC usando a fórmula: IMC = peso / (altura x altura).
'''

# IMC = peso / (altura x altura).


peso = float(input('Qual o Seu peso em Kg? : '))
altura = float(input('Qual a sua Altura em Metros? : '))
IMC = peso / (altura * altura)
print(f'O seu Indice De Massa Corporal é: {IMC}')