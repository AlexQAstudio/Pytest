import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'token'
HEADER = {'Content-Type' : 'application/json', "trainer_token": TOKEN}

# Нокаут покемона
body_knockout = {
    "pokemon_id": "270808"
}

response_knockout = requests.post(url = f'{URL}pokemons/knockout', headers = HEADER, json = body_knockout)
print(response_knockout.text)