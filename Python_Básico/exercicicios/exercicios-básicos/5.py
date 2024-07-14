'''
Tempo de Viagem: Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de avião, carro e ônibus, levando em consideração:

Avião = 600 km/h
Carro = 100 km/h
Ônibus = 80 km/h
'''

distancia = int(input('Qual a distância total do percurso em quilômetros?: '))

tempo_aviao = distancia / 600
tempo_carro = distancia / 100
tempo_onibus = distancia / 80

print(f'De avião levaria {tempo_aviao:.2f} horas, de carro seria {tempo_carro:.2f} horas e de ônibus {tempo_onibus:.2f} horas.')

#tempo de viagem (horas) = distância (km) / velocidade (km/h)