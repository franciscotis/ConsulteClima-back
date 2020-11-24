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
    response = client.get('/checar',headers= dados)
    assert response.get_json()['count'] ==1 and response.status_code == 200

def test_retorno_nenhuma_informacao():
    #A API deve retornar o status 500 caso a cidade informada não esteja disponível
    client = getClient()
    dados = {
        'cidade': 'ABCDEF'
    }
    response = client.get('/checar',headers= dados)
    assert response.status_code == 500