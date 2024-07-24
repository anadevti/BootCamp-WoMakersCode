'''
Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime.

As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""


O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
""Assassino"".
Caso contrário,ele será classificado como""Inocente"".


'''



perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]
contagem_sim = 0

for pergunta in perguntas:
    resposta = input(pergunta + ' (sim/não): ').strip().lower()   # strip() remove espaços extras, lower() converte para minúsculo

    if resposta == 'sim':
        contagem_sim += 1

# Avaliação com base na contagem de 'sim'
if contagem_sim == 5:
    classificacao = "Assassino"
elif contagem_sim >= 3:
    classificacao = "Cúmplice"
elif contagem_sim == 2:
    classificacao = "Suspeita"
else:
    classificacao = "Inocente"

print(classificacao)
