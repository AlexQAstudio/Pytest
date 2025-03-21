import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'token'
HEADER = {'Content-Type' : 'application/json', "trainer_token": TOKEN}
TRAINER_ID = '22882'

def test_autostatus():
    response = requests.get(url = f'{URL}trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_autonametrainers():
    response_trainers = requests.get(url = f'{URL}me', params = {'trainer_id' : TRAINER_ID}, headers = HEADER)
    assert response_trainers.json()["data"][0]["trainer_name"] == 'LambOfGod'