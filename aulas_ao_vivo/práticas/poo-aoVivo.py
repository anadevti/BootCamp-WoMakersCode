class Animals:

    """
    Essa classe representa um animal

    """
    def __init__(self, species: str, age: int, height: float): # método construtor
        self._species = species
        self.__age = age
        self._height = height

    def __str__(self) -> str: # método mágico, serve para retornar uma string,e  ai pra printar é só chamar o objeto dentro do print!
        return f'Animal - species {self._species}, age {self.__age}, height {self._height}'

    def eat(self):
        self.__age

def eat():
    pass

animal = Animals('Dog', 2, 0.5)
print(animal)

'''
encapsulamento

_ protected
__ private
'''
'''
metodos setters e getters

o setter é um método que permite alterar o valor de um atributo privado
o getter é um método que permite acessar (get) o valor de um atributo privado

'''

# setter
def set_species(self, species: str):
    self._species = species

# getter
def get_species(self):
    return self._species


'''
Herança
'''

class Mammiferous(Animals):
    def __init__(self, species: str, age: int, height: float, hair_color: str):
        super().__init__(species, age, height)
        self.hair_color = hair_color

    def __str__(self) -> str:
        return f'Mammiferous - species {self._species}, age {self._age}, height {self._height}, hair_color {self.hair_color}'