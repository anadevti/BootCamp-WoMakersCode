'''

Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome.

'''


def main():
    contatos = {}

    while True:
        print("\nOpções:")
        print("1. Adicionar contato")
        print("2. Procurar contato")
        print("3. Sair")
        opcao = input("Escolha uma opção (1, 2, 3): ")

        if opcao == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            contatos[nome] = telefone  # Adiciona ou atualiza o contato
            print(f"Contato '{nome}' adicionado com sucesso.")

        elif opcao == '2':
            nome = input("Digite o nome do contato que deseja procurar: ")
            if nome in contatos:
                print(f"Telefone de {nome}: {contatos[nome]}")
            else:
                print("Contato não encontrado.")

        elif opcao == '3':
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
