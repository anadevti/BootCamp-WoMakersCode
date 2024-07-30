'''
5. Crie uma função chamada contar_vogais que recebe uma string
como parâmetro.
Implemente a lógica para contar o número de vogais
na string e retorne o total de vogais.

Solicite ao usuário para inserir uma
frase e utilize a função para contar as vogais
'''

def contar_vogais(string):
    vogais = 0
    for letra in string:
        if letra in "aeiouAEIOU":
            vogais += 1
    return vogais

frase = input("Digite uma frase: ")
total_vogais = contar_vogais(frase)
print("A frase possui", total_vogais, "vogais.")
