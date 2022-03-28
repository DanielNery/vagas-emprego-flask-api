from flask import Flask
from flask_restful import Api

from resources.vagas import VagasEmpregoResource

App = Flask(__name__)

App.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
App.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Api = Api(App)

# Vai criar o banco e todas aas suas tabelas
@App.before_first_request
def cria_banco():
	banco.create_all()


def set_routes(Api):

    Api.add_resource(
        VagasEmpregoResource,
        "/vagas"
    )


if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(App)
    set_routes(Api)
    App.run(debug=True)