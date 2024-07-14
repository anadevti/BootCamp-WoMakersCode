'''
Operações Matemáticas: 
Faça um programa que peça dois números e realize as principais operações: soma, subtração, multiplicação e divisão.
'''

for pergunta in range(2):
  pergunta = int(input('Digite Dois números: '))
resultado1 =  (pergunta + pergunta)
resultado2 =  (pergunta - pergunta)
resultado3 =  (pergunta * pergunta)
resultado4 =  (pergunta / pergunta)
print (f'A soma é: {resultado1}, Em Subtração é: {resultado2}, Na multiplicação é: {resultado3}, E na divisão é: {resultado4}')