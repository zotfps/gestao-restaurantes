from cadastro.carregardados import carregar_dados

def lista_mostrar():
    escolha = int(input("1 - Mostrar todos restaurantes\n"
                    "2 - Mostrar Restaurante escolhido\n" \
                    "3 - Mostrar Restaurante por categoria\n"
                    "\nDigite a opção: "))
    restaurantes = carregar_dados()
    
    if escolha == 1:
        for item in restaurantes:
            ativo = 'ativado' if item['ativo'] else 'desativado'
            if item in restaurantes:
                print(f"- {item['nome'].ljust(25)} | {item['categoria'].ljust(20)} | {ativo}")
    elif escolha == 2:
        nomeBuscar = input("Nome do restaurante: ").upper()

        encontrou = False
        
        for item in restaurantes:
            if item["nome"] == nomeBuscar:
                ativo = 'ativado' if item['ativo'] else 'desativado'
                print(f"- {item['nome'].ljust(25)} | {item['categoria'].ljust(20)} | {ativo}")
                encontrou = True

    elif escolha == 3:
            categoriaBuscar = input("Digite a categoria: ").upper()

            encontrou = False
            
            for item in restaurantes:
                if item["categoria"] == categoriaBuscar:
                    ativo = 'ativado' if item['ativo'] else 'desativado'
                    print(f"- {item['nome'].ljust(25)} | {item['categoria'].ljust(20)} | {ativo}")
                    encontrou = True
            
    if not encontrou:
        print("Restaurante não encontrado.")