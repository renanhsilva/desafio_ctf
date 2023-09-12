#crie um banco sqlite3 com nomes dos estados, siglas, populacao, regiao e referencia para uma imagem da bandeira

import re
import sqlite3
from flask import Flask, jsonify, request, render_template  

app = Flask(__name__)

conn = sqlite3.connect("estados.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS estados (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        sigla TEXT NOT NULL,
        populacao INTEGER NOT NULL,
        qtd_agencias INTERGER NOT NULL,
        regiao TEXT NOT NULL,
        imagem TEXT NOT NULL
);
""")

cursor.execute("""
INSERT INTO estados (nome, sigla, populacao, qtd_agencias, regiao, imagem)
VALUES ('Sao Paulo', 'SP', 46289333, 1245, 'Sudeste', '/static/sp.png'),
('Rio de Janeiro', 'RJ', 17366189, 555, 'Sudeste', '/static/rj.png'),
('Minas Gerais', 'MG', 21252026, 501,'Sudeste', '/static/mg.png'),
('Espírito Santo', 'ES', 4018656, 41,'Sudeste', '/static/es.png'),
('Sao Paulo', '7707f6812879867a3c219186b9129575ea2ab581', 46289333, 245, 'Sudeste','/static/1952a01898073d1e561b9b4f2e42cbd7.png'),
('Rio de Janeiro', '7f4f5c4e995422d3e34fed178c901e3e8d8084ba', 17366189, 555, 'Sudeste', '/static/56cd07000362b73cbfc6973dcd3aa275.png'),
('Minas Gerais', 'bd62be75218df6c5083b334231b86e13ce40799b', 21252026, 501, 'Sudeste', '/static/b351bb9b0af6e4fc678749675c53ad67.png'),
('Espírito Santo', '9debabbaa01a190fabe8324c5e6e2f2808052099', 4018656, 41, 'Sudeste', '/static/12470fe406d44017d96eab37dd65fc14.png')
""")

conn.commit()
conn.close()

@app.route('/')
def get_estado():
    conn = sqlite3.connect('estados.db')
    cursor = conn.cursor()
    estado = request.args.get('estado')
    if ' ' in estado:
        return "Boa tentativa :)"
    cursor.execute(f"""
    SELECT * FROM estados WHERE sigla = '{estado}'
    """)
    resultado = cursor.fetchone()
    if resultado is None:
        return jsonify({'erro': 'Estado nao encontrado'}), 404
    nome = resultado[1]
    populacao = resultado[3]
    qtd_agencias = resultado[4]
    regiao = resultado[5]
    imagem = resultado[6]
    conn.close()
    return render_template('index.html', nome = nome, imagem = imagem, populacao = populacao, qtd_agencias = qtd_agencias, regiao = regiao)

if __name__ == '__main__':
    app.run(debug=False)

