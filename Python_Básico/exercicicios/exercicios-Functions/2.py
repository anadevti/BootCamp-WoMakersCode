'''
Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721.
'''

def reverse(number):
    revertido =  int(str(number)[::-1])
    return revertido

resultado = reverse(127)
print(resultado)
