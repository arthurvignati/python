from flask import Blueprint, jsonify

#Criação de um agregador de rotas --> marca para suportar todas as rotas
event_route_bp = Blueprint("event_route", __name__)
#Com isso é possível criar qualquer rota para o programa


#Ao exportar esse agregador de rotas ao server.py, qualquer rota que eu for criar e estiver dentro do agregador (event_route_bp) de rotas, 
#ja fica cadastrado dentro do servidor --> Graças ao Blueprint

@event_route_bp.route("/event", methods=["POST"])
def create_new_event():
    return jsonify({ "estou": "aqui" }), 201