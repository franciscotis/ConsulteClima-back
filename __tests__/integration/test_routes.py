from flask import Flask, jsonify
import json,pytest

from src.routes.routes import define_routes

def getClient():
    app = Flask(__name__)
    define_routes(app)
    client = app.test_client()
    return client

def test_busca_informacoes_corretas():
    client = getClient()
    dados = {
        'cidade': 'Feira de Santana'
    }
    headers = {'content-type': 'application/json'}
    response = client.post('/checar', data=json.dumps(dados), headers= headers)
    assert response.status_code == 200

def test_retorno_nenhuma_informacao():
    #A API deve retornar o status 500 caso a cidade informada não esteja disponível
    client = getClient()
    dados = {
        'cidade': 'ABCDEF'
    }
    headers = {'content-type': 'application/json'}
    response = client.post('/checar', data=json.dumps(dados), headers= headers)
    assert response.status_code == 500