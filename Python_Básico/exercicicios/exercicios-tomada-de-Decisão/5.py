'''
Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas.


link que me baseei sob validação das medidas:
https://brasilescola.uol.com.br/matematica/triangulo.htm#:~:text=Os%20principais%20elementos%20dessa%20figura,da%20altura%20dividido%20por%20dois.
'''

# Solicitação dos comprimentos dos lados do triângulo
lado_1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado_2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado_3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

# Verificação adicional se os lados formam um triângulo válido
if (lado_1 + lado_2 > lado_3) and (lado_1 + lado_3 > lado_2) and (lado_2 + lado_3 > lado_1):

    # Classificação do triângulo
    if lado_1 == lado_2 == lado_3:
        print("Este triângulo é equilátero.")
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        print("Este triângulo é isósceles.")
    else:
        print("Este triângulo é escaleno.")
else:
    print("Os comprimentos fornecidos não formam um triângulo válido.")
