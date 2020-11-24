from flask import request,jsonify
from cachetools import TTLCache
import json, requests,os
from flask_cors import CORS

with open(os.path.abspath(os.curdir)+'/credentials.json') as json_file:
    credentials = json.load(json_file)

cache = TTLCache(maxsize=1024, ttl=900)

def define_routes(app):
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    @app.route('/checar', methods=['POST'])
    def checar():
        try:
            data = request.get_json()
            cidade = data.get('cidade')
            if(cidade not in cache):
                url = 'http://api.weatherbit.io/v2.0/current'
                payload = {
                    'key':credentials['key'],
                    'lang':'pt',
                    'city':cidade,
                }
                response = (requests.get(url,params=payload)).json()
                dados = response['data'][0]
                resultado = {}
                resultado['temp'] = dados['temp']
                resultado['cidade'] = dados['city_name']
                resultado['clima'] = dados['weather']
                cache[cidade] = resultado
            return (cache[cidade],200)
        except:
            return {"error": "Ocorreu um problema ao acessar os dados"},500