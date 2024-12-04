from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from entity.veterinario import Veterinario
from entity.consulta import Consulta
from entity.paciente import Paciente
from entity.administrador import Administrador
from entity.funcionario import Funcionario
from entity.auxiliar_veterinario import AuxiliarVeterinario
from entity.prescricao import Prescricao

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost/clinica_veterinaria2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
