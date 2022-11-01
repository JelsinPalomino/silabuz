class PokeData:
    def __init__(self, name: str = None, abilities:list = None, weight: int = None, other_abilities:list = None):
        self.name = name
        self.abilities = abilities
        self.weight = weight
        self.other_abilities = other_abilities
    
    def def api_get_request(name: str):
        response = requests.get(pokeapi_url + name).json()
        return response 

    def __del__(self):
        return None

    