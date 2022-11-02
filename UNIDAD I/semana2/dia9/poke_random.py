import requests
import json
from random import randint

pokeapi_url_ramdon = "https://pokeapi.co/api/v2/pokemon/?offset=0&limit=1154"

def random_pokemon()-> str:
    ramdon_response = requests.get(pokeapi_url_ramdon).json()
    pokemon_ramdon = ramdon_response['results'][randint(0,ramdon_response['count'])]['name']
    print(pokemon_ramdon)
    return pokemon_ramdon

random_pokemon()