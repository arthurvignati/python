#Criação do servidor HTTP (Flask)
from flask import Flask
from src.main.routes.event import event_route_bp #importa o agregador de rotas


app = Flask(__name__)

app.register_blueprint(event_route_bp) #Adiciona o agregador de rotas ao servidor