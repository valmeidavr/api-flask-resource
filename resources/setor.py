from flask_restful import Resource, reqparse
from models.setor import SetorModel

class Setores(Resource):
    def get(self):
        return {'banana': [setor.json() for setor in SetorModel.query.all()]}

class SetorCreated(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome')
    atributos.add_argument('status')

    def post(self):
        dados = Setor.atributos.parse_args()
        setor = SetorModel(**dados)
        setor.save_setor()
        return setor.json()

class Setor(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome')
    atributos.add_argument('status')

    def get(self, setor_id):
       setor = SetorModel.find_setor(setor_id)
       if setor:
           return setor.json()
       return {'message': 'Setor não encontrado.'}, 404

    def put(self, setor_id):
        pass

    def delete(self, setor_id):
        pass

    def post(self, setor_id):
        pass