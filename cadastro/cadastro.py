from cadastro.carregardados import carregar_dados
import os
import json

def cadastrar_restaurante():
        from app import mostrar_titulo, retornar_menu
        mostrar_titulo("Cadastrar Restaurante")
        dados = carregar_dados()
        
        nome_restaurante = input("Nome do Restaurante: ").upper()
        categoria = input("Categoria do Restaurante: ").upper()

        dados.append({
            'nome': nome_restaurante,
            'categoria': categoria,
            'ativo': False
        })

        salvar_dados(dados)

        retornar_menu()

def salvar_dados(restaurantes):
        with open("restaurantes.json", "w") as file:
            json.dump(restaurantes, file, indent=2)

def carregar_dados():
        if not os.path.exists("restaurantes.json"):
            return []
        with open("restaurantes.json", "r") as file:
            return json.load(file)