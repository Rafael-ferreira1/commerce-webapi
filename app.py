from flask import Flask

app = Flask(__name__)

@app.route("/")
def buscar():
    return "<p>Função de busca</p>"