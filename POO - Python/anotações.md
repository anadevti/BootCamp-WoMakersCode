# Começando!
![img.png](img.png)

## Modulos e Namespaces:
- O que são modulos?
  - são locais onde iremos definir nomes de variaveis e funções que vai ficar visivel para todo o meu sistema
  - é espaço para declaração de nomes (ai que bem o namespace)
  - Basicamente vamos reutilizar isso em outros arquivos python
  
- boas praticas:
  - ao importar algo de outro arquivo, devemos ESPECIFICAR o que queremos reutilizar, importar tudo usando * não é
  uma boa. Exemplo:
  ![img_1.png](img_1.png)

    
## Pacotes
- coleção de modulos que foi disponibilizado de forma pub (lib)
- Pip


## Escopos de variaveis
- ![img_4.png](img_4.png)

## classes e objetos
- ![img_5.png](img_5.png)
- ![img_6.png](img_6.png)
- ![img_7.png](img_7.png)
- ![img_8.png](img_8.png)
- ![img_9.png](img_9.png)

 ## Diferença de função para método:
    - Função: é algo que faz algo
     - Método: é associado diretamente a uma classe e ele tem que atuar sobre um objeto
     - O primeiro parametro de um método é sempre o self (o self representa o objeto que eu estou atuando)

- Um pouco mais sobre o self: 
  - ![img_10.png](img_10.png)

# Modelagem de um sistema orientado a objetos
- ![img_11.png](img_11.png)
- ![img_12.png](img_12.png)
  - Modelagm é o processo de identificar os atores, os dados necessarios e o tipo de interação que está ocorrendo
  para criar um sistema é necessario conhecer suas regras de negocio.

- Exemplo:
  - ![img_13.png](img_13.png)
  - ![img_14.png](img_14.png)
  - Modelagem Final:
    - ![img_19.png](img_19.png)
    - ![img_17.png](img_17.png)
    
# Encapsulamento
 - encapsulamento é o ato de proteger os atributos de uma classe, ou seja, não permitir que eles sejam acessados diretamente de fora da classe
 - ![img_20.png](img_20.png)

# Propriedades
 - nos dão acesso a um atributo de uma classe, mas com a possibilidade de definir regras para o acesso (_, __)
 - ![img_21.png](img_21.png)


# Herança e MIxins
- Herança é um conceito comum em todas as linguagens que possuem POO
- com a herança, uma classe pode herdar os métodos e atributos de outra classe
- ![img_22.png](img_22.png)
- ![img_23.png](img_23.png)
- Herança multipla (mixins): 
  - uma classe pode herdar de multiplas classes
  - ![img_24.png](img_24.png)

# classes abstratas
- é considerada uma classe modelo para criar outras classes
  - possuem a declaração mas não tem a implementação
  - não tem como instanciar uma classe abstrata, conseguimos instanciar
  a classe filha, mas não a base.
  - ![img_25.png](img_25.png)

# duck typing
- é um estilo de programação que não se importa com a classe do objeto, mas sim com os métodos que o objeto possui
- o python é dinamico, então ele não se importa com o tipo do objeto, mas sim com o que ele faz

# erros e exceções
- tipos de erros:
  - erros de sintaxe
  - erros de exceção:
    - acontecem durante a execução do programa, linha a linha
    - try e except
## Lidando com erros e exceções
- O primeiro passo é debugar o código, podemos utilizar o print para ver onde está o erro (não recomendado)