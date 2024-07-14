'''
Consumo Médio: Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima o consumo médio em km/l.
'''

litros_de_combustivel = float(input('Informe a quantidade de litros de combustível consumidos: '))
distância_percorrida = float (input('Agora informe a distancia percorrida em quilometros: '))
consumo_medio = distância_percorrida / litros_de_combustivel
print(f'O seu Consumo Médio é: {consumo_medio:.2f} km/l')


# consumo médio (km/l) = distância percorrida (km) / litros de combustível consumidos.