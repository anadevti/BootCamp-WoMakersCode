from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)


@app.route('/')
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template('characters.html', characters=dict['results'])
@app.route('/lista')
def get_list_elements():
    url = "https://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    characters_list = []

    for character in dict['results']:
        characters = {
            'name': character['name'],
            'status': character['status'],
        }
        characters_list.append(characters)

    return {'characters': characters_list}