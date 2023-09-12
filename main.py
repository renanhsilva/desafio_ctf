#usando flask, crie uma pagina que busque nome de estados do brasil e retorne a uma imagem da bandeira do estado

from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/busca', methods=['POST'])
def busca():
    estado = request.form['estado']
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/' + estado
    r = requests.get(url)
    r = r.json()
    estado_info = r['nome']
    return render_template('index.html', estado_info=estado_info)

app.run(debug=True)

