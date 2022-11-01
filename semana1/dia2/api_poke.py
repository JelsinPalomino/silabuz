from unicodedata import name
import requests


def info_pokemon(pokemon_nombre):
    x = requests.get('https://pokeapi.co/api/v2/pokemon/{pokemon_nombre}')
    pokeapi_response = x.json()

    pokeapi_list = pokeapi_response["results"]

    print(pokeapi_list)

# [ que parametros acepta y ver que se puede consultar]
# [se puede parcear, para obtener el valor]