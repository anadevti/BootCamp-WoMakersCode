'''

Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''

# Inicializa a variável nota com um valor inválido para entrar no loop
nota = -1

# Loop que continua até que uma nota válida seja fornecida
while nota < 0 or nota > 10:
    nota = int(input("Digite uma nota entre zero e dez: "))
    if nota < 0 or nota > 10:
        print("Valor inválido, por favor digite um número entre zero e dez.")

# Quando a nota é válida, o loop termina e uma mensagem de confirmação é exibida
print("A nota é válida!")
