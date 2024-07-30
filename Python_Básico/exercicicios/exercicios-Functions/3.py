'''
Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função.

Extra: Crie uma terceira, que é um menu para o usuário escolher a
opção desejada, onde esse menu chama a função de conversão
correta.

'''

def celsius_para_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (9/5) * (fahrenheit - 32)
    return celsius

def mostrar_menu():
    print('Escolha uma Opção: ')
    print('"1. Converter Celsius para Fahrenheit"')
    print('"2. Converter Fahrenheit para Celsius"')
    print('"3. SAIR"')
    opcao = int(input('Escolha: '))
    return opcao

while True:
    opcao = mostrar_menu()
    if opcao == 1:
        input('Digite a temperatura em celsius: ')
        resultado = celsius_para_fahrenheit(opcao)
        print(f'Temperatura em Fahrenheit: {resultado}')
        celsius = celsius_para_fahrenheit(opcao)

    elif opcao == 2:
        input('Digite a temperatura em Fahrenheit: ')
        resultado = fahrenheit_para_celsius(opcao)
        print(f'Temperatura em Celsius: {resultado}')
        celsius = fahrenheit_para_celsius(opcao)

    elif opcao == 3:
        print('Saindo...')
    break

else:
    print('Escolha Invalida. Tente novamente')
