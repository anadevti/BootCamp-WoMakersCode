'''

Implemente um programa que classifique um aluno com base em sua pontuação em um exame.
 O programa deverá solicitar uma nota de 0 a 10.

 Se a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é reprovado
'''


pontuacao = int(input("🔴 Digite uma nota entre zero e dez: "))
if pontuacao >= 7:
    print("voce foi aprovado 🥳 ")
else:
    print("voce foi reprovado 😭 ")