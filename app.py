from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def buscar():
    return "<p>Função de busca</p>"

@app.route("/products")
def products():
    response = jsonify = ([
        {
            "title": "Caneca Personalizada de Porcelana ",
            "amount": 123.45,
           " installments": {" number": 3, "total": 41.15, "hasfees": True },
        },
        {
            "title": "Caneca de Choop",
            "amount": 560.45,
            "installments": { "number": 6, "total": 38.15, "hasfees": False},
        }
    ])

    #response.header.add("Access-Control-Allow-Origin","*")

    return response



if __name__ == "__main__":
    app.run(host = 'localhost', port = 5000, debug = True)