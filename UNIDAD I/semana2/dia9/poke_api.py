from random import randint
import requests
import json
 
pokeapi_url = "https://pokeapi.co/api/v2/pokemon/"
 
def api_get_request(name: str):
    response = requests.get(pokeapi_url + name).json()
    return response 

def get_abilities_from_response(response: dict):
    response = response["abilities"]    
    abilities = []
    for i in range(len(response)):
        abilities.append(response[i]['ability']['name'])
    return abilities

def get_weight_from_response(response: dict):
    weight = response["weight"] 
    return weight

def get_stats_from_response(response: dict):
    stats = {}
    for i in range (len(response['stats'])):
        stats[response['stats'][i]['stat']['name']]=response['stats'][i]['base_stat']
    return stats

# from poke_data import PokeData

def get_info_from_pokemon(name: str) -> dict:
    response = api_get_request(name)
    abilities = get_abilities_from_response(response)
    weight = get_weight_from_response(response)
    other_abilities = get_stats_from_response(response)
    
    pokemon = {}
    pokemon["name"]            = name
    pokemon["abilities"]       = abilities
    pokemon["weight"]          = weight
    pokemon["other_abilities"] = other_abilities
    
    return pokemon

# Generamos pokemones aleatoriamente
pokeapi_url_ramdon = "https://pokeapi.co/api/v2/pokemon/?offset=0&limit=1154"

def random_pokemon()-> str:
    ramdon_response = requests.get(pokeapi_url_ramdon).json()
    pokemon_ramdon = ramdon_response['results'][randint(0,ramdon_response['count'])]['name']
    print(pokemon_ramdon)
    return pokemon_ramdon

name = random_pokemon()

# RESULTADOS DE LA CONSULTA AL API
pokemon = get_info_from_pokemon(name)
print(pokemon)


