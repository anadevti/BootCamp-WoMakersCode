from datetime import datetime
import math

'''
basico para entender datetime
'''

ano_primeira_medalha = 1996
categoria_medalha = ' Volei de praia'
tipo_medalha = 'ouro'

ano_atual = datetime.now().year

mensagem = (f'nos jogos {categoria_medalha} a dupla feminina ganhou a medalha de {tipo_medalha} '
            f'em {ano_primeira_medalha}')

print(mensagem)



'''
usando math
'''
print(round(math.pi,5))