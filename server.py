from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify


db_connect = create_engine('sqlite:///condor.db')
app = Flask(__name__)
api = Api(app)

class Usuario(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select id, nombre, skin, id_rep_skins from usuario;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
    #funcion post

    def post(self):
        conn = db_connect.connect()
        print(request.json)
        Nombre = request.json['Nombre']
        Skin = request.json['Skin']
        query = conn.execute("insert into usuario values(null,'{0}')".format(Nombre,Skin))
        return {'status':'success'}

class Partida(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select id, id_nivel, progreso_realizado, monedas_recolectadas, letras_recolectadas from partida;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Seleccionar(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select id, id_usuario, id_mapa, score from seleccionar;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Mapa(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select id, id_nivel, progreso_realizado, monedas_recolectadas, letras_recolectadas from mapa ;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Nivel(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select id, nombre, numero_monedas, numero_letras from nivel ;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Selector_Partida(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select id, id_usuario, id_partida from Selector_Partida;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Tienda(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select id, id_usuario,id_rep_skins,monedas_disponibles from tienda;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Repositorio_Skins(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select id, id_usuario, id_tienda, skin from Repositorio_Skins;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
#por completar


api.add_resource(Usuario, '/usuario') # Route_1
api.add_resource(Partida, '/partida') # Route_2
api.add_resource(Seleccionar, '/seleccionar') # Route_3
api.add_resource(Mapa, '/mapa') # Route_4
api.add_resource(Nivel, '/nivel') # Route_5
api.add_resource(Selector_Partida, '/selector_partida') # Route_6
api.add_resource(Tienda, '/tienda') # Route_7
api.add_resource(Repositorio_Skins, '/repositorio') # Route_8

if __name__ == '__main__':
     app.run(port=5002)
