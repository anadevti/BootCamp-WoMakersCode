class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
        self._tipo = 'Pessoa'

    def falar_oi(self):
        print(f'Ola! meu nome é {self.__nome}')

    def falar_tipo(self):
        print(f'Meu tipo é {self._tipo}')

pessoa = Pessoa('Maria')
pessoa.falar_oi()
pessoa.falar_tipo()
print()

class Estudante(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome)
        self.curso = curso
        self._tipo = 'Estudante'

    def falar_oi(self):
        print(f'Ola! meu nome é {self.__nome} e minha matricula é {self.curso}')