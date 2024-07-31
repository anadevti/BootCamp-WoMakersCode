class Televisao: # convenção para nomes de classes: PascalCasing
    def __init__(self): # método construtor
        '''
        Definindo o tipo Televisão
        '''
        self.ligada = False
        self.canal = 3
        self.canal_min = 1
        self.canal_max = 99
        self.volume = 30
        self.volume_min = 0
        self.volume_max = 100


    '''
    Métodos da classe Televisão
    '''
    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def mudar_canal_para_cima(self):
        if not self.ligada:
            return

        if self.canal < self.canal_max:
            self.canal += 1

    def mudar_canal_para_baixo(self):
        if not self.ligada:
            return

        if self.canal > self.canal_min:
            self.canal += 1

    def aumentar_volume(self):
        if not self.ligada:
            return

        if self.volume < self.volume_max:
            self.volume += 10

    def diminuir_volume(self):
        if not self.ligada:
            return

        if self.volume > self.volume_min:
            self.volume -= 10

    def __str__(self) -> str:
        return f'Televisão - ligada {self.ligada}, canal {self.canal}, volume {self.volume}'

# Criando instancias da classe Televisao
tv_sala = Televisao()
tv_quarto = Televisao()

tv_sala.ligar()
print("Tv da sala ligada:", tv_sala.ligada)
print("Tv do Quarto está ligad a:", tv_quarto.ligada)

for _ in range(3):
    tv_sala.aumentar_volume()

print("Volume da Tv da sala:", tv_sala.volume)
print("Volume da Tv do Quarto:", tv_quarto.volume)
print()

print(tv_sala)
print(tv_quarto)