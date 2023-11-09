from flask import Flask, request, jsonify, make_response
import string
from cifrador import cifrar, decifrar
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

#hello world
@app.route('/')
def hello_world():
    return 'Hello, Worlds!'

#rota para cifrar
@app.route('/cifrar', methods=['POST'])
def cifrar_frase():
    frase = request.json['data']
    chave = request.json['key']
    if len(chave) != 3:
        return make_response(jsonify({'error': 'Chave inválida'}), 400)
    return jsonify({'cifra': cifrar(frase, chave)})

#rota para decifrar
@app.route('/decifrar', methods=['POST'])
def decifrar_frase():
    frase = request.json['data']
    chave = request.json['key']
    if len(chave) != 3:
        return make_response(jsonify({'error': 'Chave inválida'}), 400)
    return jsonify({'decifra': decifrar(frase, chave)})

app.run(host='0.0.0.0', port=5000, debug=True)
