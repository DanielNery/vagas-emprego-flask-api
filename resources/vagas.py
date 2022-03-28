from flask_restful import Resource, reqparse


class VagasEmpregoResource(Resource):

    def __init__(self, *args, **kwargs):
        
        self.parser = reqparse.RequestParser()
        self.id_vaga = self.parser.add_argument('idVaga', type=int, required=False, help='Identificador da vaga')
        self.name = self.parser.add_argument('name')
        self.description = self.parser.add_argument('description')
        self.empresa = self.parser.add_argument('empresa')
        self.salary = self.parser.add_argument('salary')
        self.args = self.parser.parse_args()

        return super().__init__(*args, **kwargs)

    def get(self):
        
        print(self.args)
        return "Hello World"

    def post(self):
        
        print(self.args)
        return "Hello World"

    def put(self):

        print(self.args)
        return "Hello World"

    def delete(self):

        print(self.args)
        return "Hello World"