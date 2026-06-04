from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Presente(db.Model):

    __tablename__ = "presentes"

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(200), nullable=False)

    escolhido = db.Column(
        db.Boolean,
        default=False
    )


class Escolha(db.Model):

    __tablename__ = "escolhas"

    id = db.Column(db.Integer, primary_key=True)

    nome_convidado = db.Column(
        db.String(200),
        nullable=False
    )

    presente_id = db.Column(
        db.Integer,
        db.ForeignKey("presentes.id")
    )

    presente = db.relationship("Presente")