'''
Construtores:
'''

class MinhaClasse:
    def __init__(self):
        print(f'Minha Classe 1: chamou o construtor padrão')

class MinhaClasse2:
    pass # não faz nada


# construtor parametrizado
class MinhaClasse3:
    def __init__(self, nome, idade):
        print(f'Minha Classe 3: chamou o construtor parametrizado com nome {nome} e idade {idade}')

objeto1 = MinhaClasse()
objeto2 = MinhaClasse2()
objeto3 = MinhaClasse3('João', 30)

'''
Destutores:
'''

class MinhaClasseDestruir: # é raro o uso  de destrutores em Python
    def __init__(self, nome):
        self.nome = nome
        print(f'Minha Classe Destruir: chamou o construtor parametrizado com nome {nome}')

    def __del__(self):
        print(f'Minha Classe Destruir: chamou o destrutor com nome {self.nome}')

print('começou a execução do programa')
objeto_destruir = MinhaClasseDestruir('objeto1')
print ('vai deletar o objeto')
exit()