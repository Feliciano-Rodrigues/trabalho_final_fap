from flask import Flask
from init_db import db, config_app, import_all_entities
from controller.funcionario_controller import funcionario_bp
from controller.administrador_controller import administrador_bp
from controller.paciente_controller import paciente_bp
from controller.cliente_controller import cliente_bp
from controller.consulta_controller import consulta_bp
from controller.prescricao_controller import prescricao_bp
from controller.veterinario_controller import veterinario_bp
from controller.auxiliar_veterinario_controller import auxiliar_veterinario_bp
from controller.cirurgia_controller import cirurgia_bp
from controller.internamento_controller import internamento_bp
from controller.agenda_controller import agenda_bp
from controller.exame_controller import exame_bp
from controller.medicamento_controller import medicamento_bp
from controller.financeiro_controller import financeiro_bp

app = Flask(__name__)

# Configurações do banco de dados
config_app(app)

# Importa todas as entidades
import_all_entities(app)

# Registra os Blueprints
app.register_blueprint(funcionario_bp, url_prefix='/api/funcionarios')
app.register_blueprint(administrador_bp, url_prefix='/api/administradores')
app.register_blueprint(paciente_bp, url_prefix='/api/pacientes')
app.register_blueprint(cliente_bp, url_prefix='/api/clientes')
app.register_blueprint(consulta_bp, url_prefix='/api/consultas')
app.register_blueprint(prescricao_bp, url_prefix='/api/prescricoes')
app.register_blueprint(veterinario_bp, url_prefix='/api/veterinarios')
app.register_blueprint(auxiliar_veterinario_bp, url_prefix='/api/auxiliares')
app.register_blueprint(cirurgia_bp, url_prefix='/api/cirurgias')
app.register_blueprint(internamento_bp, url_prefix='/api/internamentos')
app.register_blueprint(agenda_bp, url_prefix='/api/agendas')
app.register_blueprint(exame_bp, url_prefix='/api/exames')
app.register_blueprint(medicamento_bp, url_prefix='/api/medicamentos')
app.register_blueprint(financeiro_bp, url_prefix='/api/financeiro')

@app.route('/')
def home():
    return 'Bem-vindo à página inicial!'

# Inicia o servidor
if __name__ == "__main__":
    app.run(debug=True)
