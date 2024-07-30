'''
Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21
'''

dinheiro_usuario = float(input('Qual a quantidade de dinheiro que você possui em sua carteira? '))

conversoes = {
    "Dólar Americano": 4.91,
    "Peso Argentino": 0.02,
    "Dólar Australiano": 3.18,
    "Dólar Canadense": 3.64,
    "Franco Suiço": 0.42,
    "Euro": 5.36,
    "Libra Esterlina": 6.21
}

for moedas, valor_conversao in conversoes.items():
    quantidade = dinheiro_usuario / valor_conversao
    print(f"Você pode comprar {quantidade:.2f} de {moedas}")

'''
No Python, o método .items() é usado com dicionários para retornar uma visão dos pares de chave e valor do dicionário como uma lista de tuplas.
'''