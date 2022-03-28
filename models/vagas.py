from sql_alchemy import banco

class VagasEmpregoModel(banco.Model):
    __tablename__ = "vagas"

    vaga_id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(80))
    descricao = banco.Column(banco.String(200))
    empresa = banco.Column(banco.String(200))
    salario = banco.Column(banco.Float(precision=2))

    def __init__(self, vaga_id, nome, descricao, empresa, salario):
        self.vaga_id = vaga_id
        self.nome = nome
        self.descricao = descricao
        self.empresa = empresa
        self.salario = salario


    def json(self):
        return {
            "vaga_id": self.vaga_id,
            "nome": self.nome,
            "descricao": self.descricao,
            "empresa": self.empresa,
            "salario": self.salario
        }

    @classmethod
    def procurar_vaga(cls, vaga_id):
        return cls.query.filter_by(vaga_id=vaga_id).first()
    
    @classmethod
    def listar_vagas(cls):
        vagas = cls.query.all()
        return vagas

    def salvar_vaga(self):
        banco.session.add(self)
        banco.session.commit()

    def atualizar_vaga(self, nome, descricao, empresa, salario):
        self.nome = nome
        self.descricao = descricao
        self.empresa = empresa
        self.salario = salario

    def deletar_vaga(self):
        banco.session.delete(self)
        banco.session.commit()