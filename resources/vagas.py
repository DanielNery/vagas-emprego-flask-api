from flask_restful import Resource, reqparse
from services.vagas import VagasEmpregoService


class VagasEmpregoResource(Resource):

    

    def __init__(self, *args, **kwargs):
        
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('vaga_id', type=int, required=False, help='Identificador da vaga')
        self.parser.add_argument('nome')
        self.parser.add_argument('descricao')
        self.parser.add_argument('empresa')
        self.parser.add_argument('salario', type=float)
        self.args = self.parser.parse_args()

        self.vagas_service = VagasEmpregoService()

        return super().__init__(*args, **kwargs)

    def get(self):
        
        argumentos = self.args
        if argumentos["vaga_id"]:
            dados_vaga = self.vagas_service.buscar_vaga(argumentos["vaga_id"])
            return dados_vaga.json()

        return self.vagas_service.listar_vagas()


    def post(self):
        dados = self.args
        return self.vagas_service.criar_vaga(dados)

    def put(self):

        print(self.args)
        return "Hello World"

    def delete(self):

        vaga_id = self.args["vaga_id"]
        if vaga_id:
            vaga = self.vagas_service.deletar_vaga(vaga_id)
            return vaga.json()
            
        return {"msg": "vaga_id é obrigatório."}, 400