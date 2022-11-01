import requests
import json
from random import randint
pokeapi_url = "https://pokeapi.co/api/v2/pokemon/"
pokeapi_url_ramdon = "https://pokeapi.co/api/v2/pokemon/?offset=0&limit=1154"
# Solicitamos un pokemon al azar
def ramdom_pokemon()-> str:
    ramdon_response = requests.get(pokeapi_url_ramdon).json()
    pokemon_ramdon = ramdon_response['results'][randint(0,ramdon_response['count'])]['name']
    return pokemon_ramdon

def api_get_request(name: str):      # requerimiento al API
    response = requests.get(pokeapi_url + name).json()
    return response  

def get_abilities_from_response(response: dict): # Obtener habilidades
    abilities=[]
    for i in range(len(response['abilities'])):
        abilities.append(response['abilities'][i]['ability']['name'])
    return abilities

def get_weight_from_response(response: dict): #Obtener Peso
    weight = response['weight']
    return weight
def get_stats_from_response(response: dict):
    stats = {}
    for i in range (len(response['stats'])):
        stats[response['stats'][i]['stat']['name']]=response['stats'][i]['base_stat']
    return stats

def get_info_from_pokemon(name: str) -> dict:
    response = api_get_request(name)
    abilities = get_abilities_from_response(response)
    weight = get_weight_from_response(response)
    stats = get_stats_from_response(response)
    pokemon = {}
    pokemon['name'] = name
    pokemon['abilities'] = abilities
    pokemon['weight'] = weight
    pokemon['stats'] = stats
    return pokemon

def battle_pokemon():
    player1 = get_info_from_pokemon(ramdom_pokemon())
    player2 = get_info_from_pokemon(ramdom_pokemon())
    stats_payer1 = sum(player1['stats'].values())
    stats_payer2 = sum(player2['stats'].values())
    if stats_payer1 < stats_payer2 :
        ganador = player2['name'].title()
    else:
        ganador = player1['name'].title()
    print(f"""
Bienvenido a la batalla Pokemon
Jugador 01: {player1['name'].title()} Yo te elijo !!!
Nombre          :   {player1['name'].title()}
Peso            :   {player1['weight']}
Habilidades     :   {player1['abilities']}
Estadisticas    :
    Hp                  :   {player1['stats']['hp']}
    Ataque              :   {player1['stats']['attack']}
    Defensa             :   {player1['stats']['defense']}
    Ataque Especial     :   {player1['stats']['special-attack']}
    Defensa Especial    :   {player1['stats']['special-defense']}
    Velocidad           :   {player1['stats']['speed']}
    TOTAL               :   {stats_payer1}

Jugador 02: {player2['name'].title()} Yo te elijo !!!
Nombre          :   {player2['name'].title()}
Peso            :   {player2['weight']}
Habilidades     :   {player2['abilities']}
Estadisticas    :
    Hp                  :   {player2['stats']['hp']}
    Ataque              :   {player2['stats']['attack']}
    Defensa             :   {player2['stats']['defense']}
    Ataque Especial     :   {player2['stats']['special-attack']}
    Defensa Especial    :   {player2['stats']['special-defense']}
    Velocidad           :   {player2['stats']['speed']}
    TOTAL               :   {stats_payer2}

Ganador {ganador} !!!!
""")
    return



battle_pokemon()