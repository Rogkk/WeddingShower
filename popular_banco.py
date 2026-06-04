from app import app
from models import db, Presente

presentes = [
    "Air Fryer",
    "Liquidificador",
    "Jogo de Panelas",
    "Conjunto de Pratos",
    "Microondas"
]

with app.app_context():

    for nome in presentes:

        existe = Presente.query.filter_by(
            nome=nome
        ).first()

        if not existe:

            db.session.add(
                Presente(nome=nome)
            )

    db.session.commit()

print("Banco populado.")