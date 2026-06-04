from app import app
from models import db, Presente

presentes = [
    "Faca de Pão",
    "Ralador",
    "Porta-Tempero",
    "Xícara de Café",
    "Xícara de Chá",
    "Copo Medidor",
    "Lixeira de Pia",
    "Jogo de Peneira",
    "Tabua de Carne",
    "Batedor de Carne",
    "Descascador de Legumes",
    "Jogo de Faca",
    "Porta Papel Higienico",
    "Assadeiras Quadrada",
    "Bacia",
    "Assadeira de Pudim",
    "Escorredor de Louça",
    "Escorredor de Macarrão",
    "Forma de Pizza",
    "Galeteiro",
    "Balde",
    "Pá",
    "Pirex",
    "Puxa-saco",
    "Potes",
    "Jarra",
    "Copos",
    "Taças",
    "Utensílios de Cozinha",
    "Descanso de Panela",
    "Cortador de Pizza",
    "Colher de Pau",
    "Abridor de Lata",
    "Fuet",
    "Saladeira",
    "Prato de Bolo",
    "Colher de Sorvete",
    "Coador de Café",
    "Conjunto de Sobremesa",
    "Pano de Prato",
    "Afiador de Facas",
    "Cesta de Paes",
    "Travessa Quadrada",
    "Travessa Redonda",
    "Queijeira",
    "Espremedor de Batata",
    "Rodo de Pia",
    "Luva Termica",
    "Espatula de Bolo",
    "Funil",
    "Pegador de Salada",
    "Prendedor de Roupa"
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