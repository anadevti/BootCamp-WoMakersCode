'''
Tratamentos de erros

'''

def divisao(a, b):
    try: # tentar
        resultado = a/b
        print(resultado)
    except ZeroDivisionError:
        print("Erro!! Impossivel dividir um valor por zero")
    except TypeError as e: # a variavel e, funciona para trazer os detalhes do erro!
        print(f'Erro: O tipo do dado informado está incorreto!\n Detalhes: {e}')
    else:
        print('Sem excessoes')



#divisao(10,2)
#divisao(10,0)
divisao(10, "Womakerscode")