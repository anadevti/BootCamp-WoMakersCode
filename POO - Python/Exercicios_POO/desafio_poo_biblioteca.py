'''
Vamos criar um sistema orientado a objetos para representar um
sistema de biblioteca seguindo os requisitos abaixo:
1. Cada livro pode ter um ou mais autores.
2. A biblioteca controla apenas o nome, o telefone e a nacionalidade
de cada usuário. - OK
3. Cada livro tem um título, editora, uma lista de gêneros aos quais
pertence e uma lista de exemplares disponíveis.
4. Quando um exemplar é emprestado, ele é removido da lista de
exemplares disponíveis.
5. Alguns livros podem ter um número máximo de renovações
permitidas.
6. A biblioteca mantém um registro de todos os empréstimos
realizados, incluindo detalhes como data de empréstimo, data de
devolução e estado do exemplar (por exemplo, emprestado ou
devolvido).
Para modelar o sistema, utilize obrigatoriamente os conceitos de classe,
herança, propriedade, encapsulamento e classe abstrata.
'''


'''
Classes:

Livro
Autor - OK
Usuario
Exemplar
Emprestimo
Biblioteca



Propriedades:

Livro: título, editora, lista de gêneros, lista de exemplares disponíveis, número máximo de renovações (para alguns livros)
Autor: nome, nacionalidade - OK
Usuario: nome, telefone, nacionalidade
Exemplar: identificador único, estado (disponível, emprestado)
Emprestimo: data de empréstimo, data de devolução, estado do exemplar
Biblioteca: lista de livros, lista de usuários, registro de empréstimos

'''

from abc import ABC, abstractclassmethod

class Pessoa(ABC):
    def __init__(self, nome, nacionalidade, telefone):  # A biblioteca controla apenas o nome, o telefone e a nacionalidade de cada usuário.
        self.__nome = nome
        self.__nacionalidade = nacionalidade
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @property
    def nacionalidade(self):
        return self.__nacionalidade

    @property
    def telefone(self):
        return self.__telefone


class Usuario(Pessoa):
    def __init__(self, nome, nacionalidade, telefone):
        super().__init__(nome, nacionalidade, telefone) # Chamando o construtor da classe mãe

class Autor(Pessoa):
    def __init__(self, nome, nacionalidade):
        super().__init__(nome, nacionalidade) # Chamando o construtor da classe mãe