'''
1. O programa abaixo deve calcular a média dos valores digitados
pelo usuário.
No entanto, ele não está funcionando bem. Você pode
consertá-lo?
'''


def calcular_media(valores):
    if not valores:
        return 0
    return sum(valores) / len(valores)

valores = []
while True:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor: ')
    if valor.lower() == 'ok':
        break
    try:
        valores.append(float(valor))
    except ValueError:
        print("Por favor, insira um número válido.")

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {:.2f}'.format(valores, media))