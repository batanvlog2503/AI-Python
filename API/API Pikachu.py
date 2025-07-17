import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        pokemon_data = response.json()
        #print(pokemon_data)
        return pokemon_data

    else:
        print("Failed")
pokemon_name = "pikachu"

pokemon_infor = get_pokemon_info(pokemon_name)

print(f"Name: {pokemon_infor.get("name")}")
print(f"Weight: {pokemon_infor.get("weight")}")
print(f"Height: {pokemon_infor.get("height")}")
