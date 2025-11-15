import os
import json

def carregar_dados():
    if not os.path.exists("restaurantes.json"):
        return []
    with open("restaurantes.json", "r") as file:
        return json.load(file)