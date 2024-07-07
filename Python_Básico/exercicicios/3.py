'''
Conversão de Unidades: Faça um programa que peça a quantidade de quilômetros, e transforme em metros, centímetros e milímetros.
'''

# 1 quilômetro é igual a 1.000 metros. 
# 1 quilômetro é igual a 100.000 centímetros (pois 1 metro é igual a 100 centímetros e 1 quilômetro é igual a 1.000 metros)
# 1 quilômetro é igual a 1.000.000 milímetros (pois 1 metro é igual a 1.000 milímetros e 1 quilômetro é igual a 1.000 metros).
quilometros = float(input('Informe os Quilometros: '))
conversao_em_metros = quilometros * 1000
conversao_em_centimetros = quilometros * 100000
conversao_em_milimetros = quilometros * 1000000
print(f'O Resultado em Metros é: {conversao_em_metros}, já em Centimetros é: {conversao_em_centimetros} e finalizando, em Milimetros é {conversao_em_milimetros}')