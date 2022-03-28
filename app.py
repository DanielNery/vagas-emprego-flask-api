from flask import Flask
from flask_restful import Api

from resources.vagas import VagasEmpregoResource

App = Flask(__name__)
Api = Api(App)

def set_routes(Api):

    Api.add_resource(
        VagasEmpregoResource,
        "/vagas"
    )


if __name__ == '__main__':
    set_routes(Api)
    App.run(debug=True)