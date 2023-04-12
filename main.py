from flask import Flask
from flask_restful import Api
from resources.setor import Setores, Setor, SetorCreated

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/projetocrud'
api = Api(app)

api.add_resource(Setores, '/banana')
api.add_resource(Setor, '/setor/<int:setor_id>')
api.add_resource(SetorCreated, '/setor/cadastro')

if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)