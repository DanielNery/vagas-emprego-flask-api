
from itsdangerous import json
from models.vagas import VagasEmpregoModel

class VagasEmpregoService:

    def buscar_vaga(self, vaga_id: int) -> dict:
        vaga = VagasEmpregoModel.procurar_vaga(vaga_id)
        return vaga

    def listar_vagas(self) -> list:
        lista_vagas = VagasEmpregoModel.listar_vagas()
        vagas =  [vaga_model.json() for vaga_model in lista_vagas] 
        return vagas

    def criar_vaga(self, dados: dict) -> dict:
        vaga = VagasEmpregoModel(**dados)
        try:
            print(vaga)
            resultado = vaga.salvar_vaga()
            print(resultado)
        except Exception as e:
            return {"msg": "Erro ao persistir vaga.", "error": e}, 500
            
        return vaga.json()

    def deletar_vaga(self, vaga_id: int) -> dict:
        vaga = self.buscar_vaga(vaga_id)
        vaga_deletada = vaga
        vaga.deletar_vaga()
        return vaga_deletada

    def atualizar_vaga(self, dados: dict) -> dict:
        nova_vaga = {**dados}
        return nova_vaga