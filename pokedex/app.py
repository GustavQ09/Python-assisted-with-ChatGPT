from flask import Flask, render_template, jsonify, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Obtener datos de los primeros 251 Pokémon
    pokemon_data = get_pokemon_data(251)
    return render_template('index.html', pokemon_data=pokemon_data)

@app.route('/pokemon/<int:pokemon_id>')
def pokemon(pokemon_id):
    # Obtener información del Pokémon
    pokemon_data = get_pokemon_info(pokemon_id)
    return render_template('pokemon.html', pokemon_data=pokemon_data)

def get_pokemon_data(limit):
    # Obtener los datos básicos de los Pokémon desde la PokeAPI
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}"
    response = requests.get(url)
    data = response.json()
    pokemon_data = []
    for result in data['results']:
        pokemon_id = result['url'].split('/')[-2]
        pokemon_name = result['name'].capitalize()
        pokemon_data.append({'id': pokemon_id, 'name': pokemon_name})
    return pokemon_data

def get_pokemon_info(pokemon_id):
    # Obtener información detallada de un Pokémon específico desde la PokeAPI
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    data = response.json()
    pokemon_info = {
        'id': data['id'],
        'name': data['name'].capitalize(),
        'abilities': [ability['ability']['name'].capitalize() for ability in data['abilities']],
        'stats': {stat['stat']['name'].capitalize(): stat['base_stat'] for stat in data['stats']},
        'description': get_pokemon_description(pokemon_id),
        'image': data['sprites']['front_default']
    }
    return pokemon_info

def get_pokemon_description(pokemon_id):
    # Obtener la descripción de un Pokémon específico desde la PokeAPI
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}"
    response = requests.get(url)
    data = response.json()
    for entry in data['flavor_text_entries']:
        if entry['language']['name'] == 'en':
            description = entry['flavor_text'].replace('\n', ' ')
            return description

if __name__ == '__main__':
    app.run(debug=True)
