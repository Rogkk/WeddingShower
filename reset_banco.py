from app import app
from models import db, Presente, Escolha

presentes = [
    "Açucareiro",
    "Afiador de Faca",
    "Amassador de Batata",
    "Bacias",
    "Balança Digital",
    "Boleira",
    "Bowls",
    "Cesto de Pão",
    "Concha para Sorvete",
    "Copo Medidor",
    "Cortador de Bolo",
    "Cortador de Pizza",
    "Cortador de Queijo",
    "Descanso de Panela",
    "Escorredor de Arroz",
    "Escorredor de Louça",
    "Escorredor de Macarrão",
    "Descascador de Legumes e Prendedor de Roupa",
    "Faca de Pão",
    "Forma de Pizza",
    "Forma para Bolo",
    "Funil e Rodo de Pia",
    "Galheteiro",
    "Garrafa de Café",
    "Jarra de Água",
    "Jogo Americano",
    "Jogo de Colher de Pau",
    "Jogo de Peneiras",
    "Luva térmica",
    "Pá de Lixo e Balde",
    "Panos de Prato",
    "Pegador de Salada",
    "Pirex Quadrado",
    "Pirex Redondo",
    "Porta Papel Higienico",
    "Porta Sabão Detergente",
    "Porta Temperos",
    "Porta-filtro de café",
    "Potes",
    "Queijeira",
    "Ralador",
    "Rolo de Massa",
    "Saca Rolha",
    "Saleiro e Abridor de Latas",
    "Saladeira",
    "Tábua de Carne",
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