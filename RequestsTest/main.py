import requests


URL = "https://api.pokemonbattle.me/v2"
TOKEN = "d0ec712dc8e6adb9a52cbabe19bc6b31"
HEADER = {"Content-Type" : "application/json", "trainer_token" : TOKEN}
BODY_REGISTR = {
    "trainer_token": TOKEN,
    "email": "kenny@yandex.ru",
    "password": "Iloveqa11"
}

BODY_CONF = {
    "trainer_token": TOKEN
}

BODY_CREATE = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/009.png"
}

BODY_PUT = {
    "pokemon_id": "26218",
    "name": "NewБульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

BODY_POKEBALL = {
    "pokemon_id": "26218"
}

'''response = requests.post(url = f"{URL}/trainers/reg", headers=HEADER, json=BODY_REGISTR)
print(response.text)'''

'''response_confirmation = requests.post(url=f"{URL}/trainers/confirm_email", headers=HEADER, json=BODY_CONF)
print(response_confirmation.text)'''

'''requests_create = requests.post(url=f"{URL}/pokemons", headers=HEADER, json=BODY_CREATE)
print(requests_create.text)
'''
'''pokemon_id = requests_create.json()["id"]
print(pokemon_id)'''

'''requests_put = requests.put(url=f"{URL}/pokemons", headers=HEADER, json=BODY_PUT)
print(requests_put.text)'''

'''requests_pokeball = requests.post(url=f"{URL}/trainers/add_pokeball", headers=HEADER, json=BODY_POKEBALL)
print(requests_pokeball.text)'''