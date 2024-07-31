'''
1. Crie uma classe que modele o objeto "carro". OK
2. Um carro tem os seguintes atributos: ligado, cor, modelo,
velocidade. OK
3. Um carro tem os seguintes comportamentos: liga, desliga, acelera,
desacelera. OK
4. Crie uma instância da classe carro. OK
5. Faça o carro "andar" utilizando os métodos da sua classe. OK
6. Faça o carro "parar" utilizando os métodos da sua classe. OK
'''

class Carro:
    def __init__(self):
        self.ligado = False
        self.cor = 'Branco'
        self.modelo = 'Fusca'
        self.velocidade = 0

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def acelerar(self):
        if self.ligado:
            self.velocidade += 10

    def desacelerar(self):
        if self.ligado:
            self.velocidade -= 10

    def __str__(self) -> str:
        return f'Carro - ligado {self.ligado}, Andando na velocidade {self.velocidade}'

HB20 = Carro()
HB20.ligar()
HB20.acelerar()
print(HB20)

HB20.desacelerar()
HB20.desligar()
print(HB20)