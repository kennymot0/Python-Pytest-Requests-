import requests
import pytest

URL = "https://api.pokemonbattle.me/v2"
TOKEN = "d0ec712dc8e6adb9a52cbabe19bc6b31"
HEADER = {"Content-Type" : "application/json", "trainer_token" : TOKEN}
TRAINER_ID = "3968"

def test_status_code_pok():
    response = requests.get(url=f"{URL}/pokemons", params={"trainer_id" : TRAINER_ID})
    assert response.status_code == 200

def test_status_code_tr():
    response = requests.get(url=f"{URL}/trainers", params={"trainer_id" : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response_pok():
    response_get = requests.get(url=f"{URL}/pokemons", params={"trainer_id" : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == "Бульбазавр"

def test_part_of_response_tr():
    response_get = requests.get(url=f"{URL}/trainers", params={"trainer_id" : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == "rurk"