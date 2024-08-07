'''
# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.

# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança", "propriedades", "encapsulamento" e "classe abstrata".

'''

from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self._nome = nome
        self._telefone = telefone
        self._renda_mensal = renda_mensal

    @property
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self._telefone

    @property
    def renda_mensal(self):
        return self._renda_mensal

    @abstractmethod
    def cheque_especial(self):
        pass

class ClienteMulher(Cliente):
    def cheque_especial(self):
        return self._renda_mensal

class ClienteHomem(Cliente):
    def cheque_especial(self):
        return 0

class ContaCorrente:
    def __init__(self, clientes):
        self.clientes = clientes
        self.saldo = 0
        self.operacoes = []

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(f'Depósito de R$ {valor:.2f}')

    def saque(self, valor):
        total_cheque_especial = sum(cliente.cheque_especial() for cliente in self.clientes)
        if self.saldo - valor >= -total_cheque_especial:
            self.saldo -= valor
            self.operacoes.append(f'Saque de R$ {valor:.2f}')
        else:
            print('Saldo insuficiente')

    def extrato(self):
        print(f'Conta de {", ".join(cliente.nome for cliente in self.clientes)}')
        print(f'Saldo: R$ {self.saldo:.2f}')
        print('Operações:')
        for op in self.operacoes:
            print(f' - {op}')

# Testando o sistema
cliente1 = ClienteMulher('Maria', '9999-9999', 1000)
cliente2 = ClienteHomem('João', '8888-8888', 2000)
conta = ContaCorrente([cliente1, cliente2])

conta.deposito(500)
conta.saque(1200)
conta.extrato()
conta.saque(20)