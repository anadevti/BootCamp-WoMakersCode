class Atletas:
  def __init__(self, nome, pais, modalidade, data_nascimento):
    self.nome = nome
    self.pais = pais
    self.modalidade = modalidade
    self.data_nascimento = data_nascimento


  @property
  def nome(self):
    return self._nome

  @nome.setter
  def nome(self, valor):
    if isinstance(valor, str):
      self._nome = valor
    else:
      raise ValueError("O nome deve ser uma string.")


  @property
  def modalidade(self):
    return self._modalidade

  @modalidade.setter
  def modalidade(self, valor):
    if isinstance(valor, str):
      self._modalidade = valor
    else:
      raise ValueError("A modalidade deve ser uma string.")


  @property
  def data_nascimento(self):
    return self._data_nascimento

  @data_nascimento.setter
  def data_nascimento(self, valor):
    if isinstance(valor, str):
      self._data_nascimento = valor
    else:
      raise ValueError("A data de nascimento deve ser uma string.")

  @property
  def pais(self):
    return self._pais


  @pais.setter
  def pais(self, valor):
    lista_paises_permitidos = ['brasil', 'eua', 'japão', 'frança']
    if valor.lower() in lista_paises_permitidos:
      self._pais = valor
    else:
      raise ValueError("O país deve ser um dos seguintes: Brasil, EUA, Japão ou França.")

  def __str__(self):
    return f"Nome: {self.nome}, Pais: {self.pais}, Data de Nascimento: {self.data_nascimento}, Modalidade: {self.modalidade}"

class Participantes(Atletas):
  def __init__(self, nome, pais, modalidade, data_nascimento, evento, medalha):
    super().__init__(nome, pais, modalidade, data_nascimento)
    self.evento = evento
    self.medalha = medalha


  @property
  def evento(self):
    return self._evento

  @evento.setter
  def evento(self, valor):
    if valor.lower() in ['100m rasos', 'aalto em distância', 'natação', 'ginastica']:
      self._evento = valor
    else:
      raise ValueError("O evento deve ser um dos seguintes: 100m rasos, Salto em distância ou Natação.")

  @property
  def medalha(self):
    return self._medalha

  @medalha.setter
  def medalha(self, valor):
    if isinstance(valor, str):
      if valor.lower() in ['ouro', 'prata', 'bronze', 'nenhuma']:
        self._medalha = valor
      else:
        raise ValueError("A medalha dever possuir um dos seguintes valores: Ouro, Prata, Bronze ou Nenhuma")
    else:
      raise ValueError("A medalha deve ser uma string.")


  def __str__(self):
    return super().__str__() + f", Evento:{self.evento}, Medalha: {self.medalha}"

atleta1 = Atletas("Maria", "Brasil", "Natação", "12/12/1990")
atleta2 = Atletas("João", "EUA", "100m rasos", "12/12/1990")
print(atleta1)
print(atleta2)