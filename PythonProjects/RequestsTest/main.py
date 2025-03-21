import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'token'
HEADER = {'Content-Type' : 'application/json', "trainer_token": TOKEN}

# Создание покемона
body_create = {
    "name": "Murder77",
    "photo_id": 12
}

response_create = requests.post(url = f'{URL}pokemons', headers = HEADER, json = body_create)
print(response_create.text)
pokemon_id = response_create.json()['id']

# Изменение имени покемона
body_rename = {
    "pokemon_id": pokemon_id,
    "name": "Created"
}

response_rename = requests.patch(url = f'{URL}pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)

# Поймать покемона в покебол

body_pokeball = {
    "pokemon_id": pokemon_id
}

response_pokeball = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)