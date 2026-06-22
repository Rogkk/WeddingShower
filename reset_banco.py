from app import app
from models import db, Presente, Escolha

presentes = [
    "Açucareiro",
    "Afiador de Faca",
    "Amassador de Batata",
    "Bacias",
    "Balança Digital",
    "Boleira",
    "Cesto de Pão",
    "Coador de Café",
    "Concha para Sorvete",
    "Copo Medidor",
    "Copos",
    "Cortador de Bolo",
    "Cortador de Pizza",
    "Cortador de Queijo",
    "Descanso de Panela",
    "Escorredor de Arroz",
    "Escorredor de Louça",
    "Escorredor de Macarrão",
    "Escumadeira e Descascador de Legumes",
    "Espátulas",
    "Faca de Pão",
    "Forma de Pizza",
    "Forma para Bolo",
    "Forma de Pudim",
    "Fouet",
    "Funil e Rodo de Pia",
    "Galheteiro",
    "Garrafa de Café",
    "Jarra",
    "Jogo Americano",
    "Jogo de Colher de Pau",
    "Jogo de Peneiras",
    "Lixeira para Cozinha",
    "Luca térmica",
    "Pá de Lixo e Balde",
    "Panos de Prato",
    "Pegador de Salada",
    "Pirex Quadrado",
    "Pirex Redondo",
    "Porta Papel Higienico",
    "Porta Sabão Detergente",
    "Porta Temperos",
    "Potes",
    "Queijeira",
    "Ralador e Concha",
    "Rolo de Massa",
    "Saca Rolha",
    "Saleiro e Abridor de Latas",
    "Saladeira",
    "Tábua de Carne",
    "Xícara de Café",
    "Xícara de Chá"
]

with app.app_context():

    Escolha.query.delete()
    Presente.query.delete()

    db.session.commit()

    for nome in presentes:
        db.session.add(
            Presente(
                nome=nome,
                escolhido=False
            )
        )

    db.session.commit()

print("Banco resetado com sucesso!")