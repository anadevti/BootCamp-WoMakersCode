import requests
from flask import Flask, render_template, json

app = Flask(__name__)

@app.route('/')
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character"
    response = requests.get(url)
    data = response.json()
    return render_template('characters.html', characters=data['results'])

@app.route('/test')
def test_layout():
    return render_template('profile.html')



@app.route('/profile/<id>')
def get_profile(id):
    url = f"https://rickandmortyapi.com/api/character/{id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        character_data = response.json()
        return render_template('profile.html', profile=character_data)
    except requests.RequestException as e:
        return f"An error occurred: {e}", 500

@app.route('/lista')
def get_list_elements():
    url = "https://rickandmortyapi.com/api/character"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        characters_list = [
            {'name': character['name'], 'status': character['status']}
            for character in data['results']
        ]

        return {'characters': characters_list}
    except requests.RequestException as e:
        return f"An error occurred: {e}", 500
