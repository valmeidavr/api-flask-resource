from sql_alchemy import db

class SetorModel(db.Model):
    __tablename__ = 'setores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)

    def __init__(self, nome, status):
        self.nome = nome
        self.status = status

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'status': self.status,
            'teste': 'banana'
        }

    @classmethod
    def find_setor(cls, id):
        setor = cls.query.filter_by(id=id).first()
        if setor:
            return setor
        return None

    def save_setor(self):
        db.session.add(self)
        db.session.commit()