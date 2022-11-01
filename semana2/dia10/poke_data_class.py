#1ro Iniciamos con la conexión

import requests

pokeapi_url = "https://pokeapi.co/api/v2/pokemon/"
 
class Conexion_pokeapi:
    def __init__(self, name:str):
        self.name = name

    def api_get_request(self):
        response = requests.get(pokeapi_url + self.name).json()
        return response 

#2do Generamos las clases con las caracteristicas de los pokemones

class Abilities:
    def __init__(self, msg:str, name:str):
        self.msg      = msg
        self.response = Conexion_pokeapi(name)

    def get_abilities_from_response(self):
        respon = self.response.api_get_request()
        response = respon["abilities"]
        abilities = []
        for i in range(len(response)):
            abilities.append(response[i]['ability']['name'])
        return abilities

pokemon = Abilities("Se recibió con exito!!!", "ditto")
print(pokemon.msg)
print(pokemon.response)
print(pokemon.get_abilities_from_response())

"""
class PokeData:
    def __init__(self, name: str = None, abilities:list = None, weight: int = None, other_abilities:list = None):
        self.name = name
        self.abilities = abilities
        self.weight = weight
        self.other_abilities = other_abilities
    
    def api_get_request(name: str):
        response = requests.get(pokeapi_url + name).json()
        return response 

    def __del__(self):
        return None

"""