'''

Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.

'''

dicionario_compras = {'play': 50, 'tv': '20', 'fogao': 30, 'geladeira': 'não disponível'}

soma = 0
for valor in dicionario_compras.values():
    if isinstance(valor, int) or isinstance(valor, float):
        soma += valor
    elif isinstance(valor, str) and valor.isdigit():
        soma += int(valor)
    # Se o valor não é numérico e não pode ser convertido, ele é ignorado

print(soma)
