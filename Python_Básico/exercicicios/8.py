'''
Calorias Queimadas: Solicite ao usuário o número de horas de exercício físico por semana. Calcule o total de calorias queimadas em um mês, considerando uma média de 5 calorias por minuto de exercício.
'''

# precisamos converter as horas de exercício físico por semana para minutos. ok
# Multiplicar o número de horas por 60 (já que cada hora tem 60 minutos). ok
# Multiplicar o número de minutos de exercício por semana pelo valor médio de calorias queimadas por minuto (5 calorias).
# Para encontrar o total de calorias queimadas em um mês, multiplicar o valor semanal por 4 (considerando que um mês tem aproximadamente 4 semanas).

calorias_queimadas = float(input('Quantas horas de exercício físico você faz por semana? : '))
convertendo_horas_em_minutos = calorias_queimadas * 60
calorias_por_semana = convertendo_horas_em_minutos * 5
calorias_por_mes = calorias_por_semana * 4
print(f'As calorias queimadas por mês são: {calorias_por_mes}')