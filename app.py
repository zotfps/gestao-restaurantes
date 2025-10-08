import os

restaurantes = []

def exibir_menu():
    """Exibe o nome e o logotipo estilizado do programa na tela."""
    print("""
    ░██████╗░███████╗░██████╗████████╗░█████╗░░█████╗░
    ██╔════╝░██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
    ██║░░██╗░█████╗░░╚█████╗░░░░██║░░░███████║██║░░██║
    ██║░░╚██╗██╔══╝░░░╚═══██╗░░░██║░░░██╔══██║██║░░██║
    ╚██████╔╝███████╗██████╔╝░░░██║░░░██║░░██║╚█████╔╝
    ░╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░

    ██████╗░███████╗░██████╗████████╗░█████╗░██╗░░░██╗██████╗░░█████╗░███╗░░██╗████████╗███████╗░██████╗
    ██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██║░░░██║██╔══██╗██╔══██╗████╗░██║╚══██╔══╝██╔════╝██╔════╝
    ██████╔╝█████╗░░╚█████╗░░░░██║░░░███████║██║░░░██║██████╔╝███████║██╔██╗██║░░░██║░░░█████╗░░╚█████╗░
    ██╔══██╗██╔══╝░░░╚═══██╗░░░██║░░░██╔══██║██║░░░██║██╔══██╗██╔══██║██║╚████║░░░██║░░░██╔══╝░░░╚═══██╗
    ██║░░██║███████╗██████╔╝░░░██║░░░██║░░██║╚██████╔╝██║░░██║██║░░██║██║░╚███║░░░██║░░░███████╗██████╔╝
    ╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═════╝░
    """)

def exibir_opcoes():
    """Mostra as opções disponíveis no menu principal do aplicativo."""
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Alternar Estado do Restaurante")
    print("4. Deletar Restaurante")
    print("5. Sair")

def finalizar_programa():
    """Exibe uma mensagem de encerramento e finaliza a execução do programa."""
    print("\nFinalizando o programa...\n")

def mostrar_titulo(titulo):
    """Limpa o terminal e exibe um título formatado com linhas acima e abaixo."""
    os.system('cls' if os.name == 'nt' else 'clear')
    linha = '=' * len(titulo)
    print(linha)
    print(titulo)
    print(linha)
    print("")

def retornar_menu():
    """Aguarda uma tecla e retorna o usuário ao menu principal."""
    input("\nPressione uma tecla para voltar ao menu...")
    main()

def alternar_estado_restaurante():
    """Ativa ou desativa o status de um restaurante com base no nome informado pelo usuário."""
    mostrar_titulo("Alternar estado do Restaurante")
    print("\nRestaurantes Cadastrados:\n")

    lista_mostrar()

    nome_restaurante = input("\nNome do Restaurante a ser ativado ou desativado: ")
    for restaurante in restaurantes:
        if restaurante['nome'].lower() == nome_restaurante.lower():
            restaurante['ativo'] = not restaurante['ativo']
            print(f"Restaurante {nome_restaurante} foi ativado com sucesso!"
                  if restaurante['ativo']
                  else f"Restaurante {nome_restaurante} foi desativado com sucesso!")
            return retornar_menu()
    print(f"Restaurante {nome_restaurante} não encontrado.")
    retornar_menu()

def cadastrar_restaurante():
    """Cadastra um novo restaurante, solicitando nome e categoria, e adiciona-o à lista global."""
    mostrar_titulo("Cadastrar Restaurante")
    nome_restaurante = input("Nome do Restaurante: ")
    if nome_restaurante.strip() == "" or nome_restaurante.isnumeric():
        print("Nome inválido.")
        return retornar_menu()
    categoria = input("Categoria do Restaurante: ")
    if categoria.strip() == "" or categoria.isnumeric():
        print("Categoria inválida.")
        return retornar_menu()
    novo_restaurante = {
        'nome': nome_restaurante,
        'categoria': categoria,
        'ativo': False
    }
    restaurantes.append(novo_restaurante)
    print(f"Restaurante {nome_restaurante} foi cadastrado com sucesso!")
    retornar_menu()

def opcao_invalida():
    """Informa ao usuário que a opção escolhida é inválida e retorna ao menu principal."""
    input("Opção inválida. Digite uma tecla para continuar...")
    retornar_menu()

def lista_mostrar():
    """Mostra todos os restaurantes cadastrados formatados em colunas."""
    print(f'{"Nome do restaurante".ljust(27)} | {"Categoria".ljust(20)} | Status\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f"- {nome_restaurante.ljust(25)} | {categoria.ljust(20)} | {ativo}")

def listar_restaurantes():
    """Exibe todos os restaurantes cadastrados com suas respectivas categorias e status."""
    mostrar_titulo("Lista de Restaurantes")
    lista_mostrar()
    retornar_menu()

def deletar_restaurante():
    """Remove um restaurante da lista com base no nome informado pelo usuário."""
    mostrar_titulo("Deletar Restaurante")
    print("\nRestaurantes Cadastrados: \n")

    lista_mostrar()
    nome_restaurante = input("\nNome do Restaurante: ")

    for restaurante in restaurantes:
        if restaurante['nome'].lower() == nome_restaurante.lower():
            restaurantes.remove(restaurante)
            print(f"Restaurante {nome_restaurante} foi deletado com sucesso!")
            break
    else:
        print(f"Restaurante {nome_restaurante} não encontrado.")
    retornar_menu()

def menu_opcoes():
    """Lê a escolha do usuário e direciona para a função correspondente do menu."""
    try:
        escolha_opcao = int(input("Escolha uma opção: "))
        if escolha_opcao == 1:
            cadastrar_restaurante()
        elif escolha_opcao == 2:
            listar_restaurantes()
        elif escolha_opcao == 3:
            alternar_estado_restaurante()
        elif escolha_opcao == 4:
            deletar_restaurante()
        elif escolha_opcao == 5:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    """Função principal do programa. Exibe o menu inicial e controla o fluxo da aplicação."""
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_menu()
    exibir_opcoes()
    menu_opcoes()

if __name__ == "__main__":
    main()