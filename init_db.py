from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Inicializa o SQLAlchemy sem o app

def config_app(app):
    """
    Configura a aplicação Flask com as configurações do banco de dados.
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost/clinica_veterinaria3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o SQLAlchemy com o app
    db.init_app(app)

def import_all_entities(app):
    """
    Importa todas as entidades para registrá-las no SQLAlchemy e cria as tabelas.
    """
    with app.app_context():
        from entity.funcionario import Funcionario
        from entity.veterinario import Veterinario
        from entity.auxiliar_veterinario import AuxiliarVeterinario
        from entity.administrador import Administrador
        from entity.cliente import Cliente
        from entity.paciente import Paciente
        from entity.cirurgia import Cirurgia
        from entity.consulta import Consulta
        from entity.prescricao import Prescricao
        from entity.internamento import Internamento
        from entity.agenda import Agenda
        from entity.exame import Exame
        from entity.medicamento import Medicamento
        from entity.financeiro import Financeiro

        # Depois, crie as tabelas
        db.create_all()
