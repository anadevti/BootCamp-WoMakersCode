'''
6. Vamos construir um jogo de forca.
O programa escolherá
aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
secreta será representada por espaços em branco, um para cada letra
da palavra.
O jogador terá um número limitado de 6 tentativas.
Em cada
tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
na palavra secreta, ela será revelada nas posições correspondentes. Se
a letra não estiver na palavra, uma mensagem de erro deverá ser
informada. Após um número máximo de erros, o jogador perde. O jogo
continua até que o jogador adivinhe a palavra ou exceda o número
máximo de tentativas.
Dica: Você precisará importar uma biblioteca para resolver esse
exercício

'''
from random import choice

palavras_secretas = ["python", "programacao", "computador", "algoritmo", "dados"]
palavra_secreta = choice(palavras_secretas)

letras_acertadas = ["_" for letra in palavra_secreta]

tentativas = 6
while tentativas > 0 and "_" in letras_acertadas:
    print("Palavra:", *letras_acertadas)
    chute = input("Digite uma letra: ").lower()

    if chute in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == chute:
                letras_acertadas[i] = chute
    else:
        tentativas -= 1
        print("Letra incorreta!")

    print(f"Você tem {tentativas} tentativas restantes.")

# Verificar se o jogador ganhou ou perdeu
if "_" not in letras_acertadas:
    print("Parabéns! Você acertou a palavra:", palavra_secreta)
else:
    print("Você perdeu! A palavra era:", palavra_secreta)

