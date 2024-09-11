## Consumindo uma API

'''

com Python puro, sem bibliotecas de terceiros
'''

'''
import urllib.request
import json

def search_addres(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    with urllib.request.urlopen(url) as response:
        data = response.read()
        data = json.loads(data)
        print(data)

cep_input = input("Digite o CEP para a consulta: ")
search_addres(cep_input)

'''

## usando flask

from flask import Flask, request

app = Flask(__name__)

products = {
    "code" : 1,
    "name" : "product 1",
    "price" : 100.00
    }

@app.route('/')
def hello_world():
    return 'Hello, World!'

# list all products
@app.route('/products', methods=['GET'])
def list_products():
    return products, 200

# create products
@app.route('/products', methods=['POST'])
def create_products():
    print(request)

    return products, 200


if __name__ == '__main__':
    app.run(debug=True)
