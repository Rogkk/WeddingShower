from flask import Flask, render_template, jsonify, request
from models import db, Presente, Escolha
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

database_url = os.getenv("DATABASE_URL")

if not database_url:
    raise ValueError(
        "DATABASE_URL não foi encontrada."
    )

if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace(
        "postgres://",
        "postgresql://",
        1
    )

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# ====================
# Página principal
# ====================

@app.route("/")
def home():
    return render_template("index.html")


# ====================
# Carregar presentes
# ====================

@app.route("/presentes")
def listar_presentes():

    presentes = Presente.query.filter_by(
        escolhido=False
    ).all()

    return jsonify([
        {
            "id": p.id,
            "nome": p.nome
        }
        for p in presentes
    ])


# ====================
# Escolher presente
# ====================

@app.route("/escolher", methods=["POST"])
def escolher():

    dados = request.json

    nome = dados["nome"]
    presente_id = dados["presente_id"]

    presente = Presente.query.get(presente_id)

    if not presente:
        return jsonify({
            "sucesso": False,
            "mensagem": "Presente não encontrado."
        })

    if presente.escolhido:
        return jsonify({
            "sucesso": False,
            "mensagem": "Presente já escolhido."
        })

    presente.escolhido = True

    escolha = Escolha(
        nome_convidado=nome,
        presente_id=presente.id
    )

    db.session.add(escolha)
    db.session.commit()

    return jsonify({
        "sucesso": True,
        "mensagem": "Presente reservado com sucesso!"
    })


# ====================
# Painel Admin
# ====================

@app.route("/admin")
def admin():

    escolhas = Escolha.query.all()
    presentes = Presente.query.all()

    return render_template(
        "admin.html",
        escolhas=escolhas,
        presentes=presentes
    )


if __name__ == "__main__":
    app.run(debug=True)