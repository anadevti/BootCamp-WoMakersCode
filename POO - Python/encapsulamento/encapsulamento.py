# encapsulamento

class Pessoa:
    def __init__(self, nome, profissao, identidade):
        self._nome = nome # protected
        self.profissao = profissao # public
        self.__identidade = identidade # private

    def __str__(self):
        return f'Nome: {self._nome}, Profissão: {self.profissao}, Identidade: {self.__identidade}'

pessoa_1 = Pessoa('Maria', 'Engenheira', 123456)
print(pessoa_1)