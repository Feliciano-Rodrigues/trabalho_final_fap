from flask import Blueprint, request, jsonify
from init_db import db
from entity.funcionario import Funcionario
from entity.administrador import Administrador
from werkzeug.security import generate_password_hash
from service.administrador_service import AdministradorService
from sqlalchemy.exc import IntegrityError
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

administrador_bp = Blueprint('administrador', __name__)

# Função para validar data
def validar_data(data_str):
    try:
        return datetime.strptime(data_str, '%Y-%m-%d').date()
    except ValueError:
        return None

# Rota para login
@administrador_bp.route('/login', methods=['POST'])
def login_administrador():
    data = request.get_json()
    logger.info("Dados recebidos para login: %s", data)
    
    if not data:
        return jsonify({"message": "Requisição inválida: corpo da requisição está vazio"}), 400
    
    email = data.get('email')
    senha = data.get('senha')

    if not email or not senha:
        return jsonify({"message": "Email e senha são obrigatórios"}), 400
    
    administrador = AdministradorService.login(email, senha)
    
    if administrador:
        token = AdministradorService.gerar_token(administrador)
        return jsonify({
            "message": "Login bem-sucedido",
            "id": administrador.id_funcionario,
            "responsabilidade": administrador.responsabilidade,
            "token": token
        }), 200
        
    return jsonify({"message": "Email ou senha inválidos"}), 400


# Rota para criação de administrador
@administrador_bp.route('/criar', methods=['POST'])
def criar_administrador():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Requisição inválida: corpo da requisição está vazio"}), 400
    
    logger.info("Dados recebidos para criação: %s", data)
    
    required_fields = ['nome', 'cpf', 'email', 'telefone', 'endereco', 'data_nascimento', 'senha', 'responsabilidade']
    for field in required_fields:
        if field not in data or not data[field]:
            logger.warning("Campo obrigatório ausente ou vazio: %s", field)
            return jsonify({"message": "Todos os campos são obrigatórios"}), 400
    
    nome = data.get('nome')
    cpf = data.get('cpf')
    email = data.get('email')
    telefone = data.get('telefone')
    endereco = data.get('endereco')
    data_nascimento = validar_data(data.get('data_nascimento'))
    senha = data.get('senha')
    responsabilidade = data.get('responsabilidade')
    data_contratacao = validar_data(data.get('data_contratacao'))

    # Validação de CPF e Email duplicados
    try:
        funcionario_existente = db.session.query(Funcionario).filter_by(cpf=cpf).first()
        if funcionario_existente:
            logger.warning("CPF já está em uso: %s", cpf)
            return jsonify({"message": "O CPF já está em uso"}), 400

        email_existente = db.session.query(Funcionario).filter_by(email=email).first()
        if email_existente:
            logger.warning("Email já está em uso: %s", email)
            return jsonify({"message": "O email já está em uso"}), 400

        # Criação do Funcionario
        funcionario = Funcionario(
            nome=nome,
            cpf=cpf,
            email=email,
            telefone=telefone,
            endereco=endereco,
            data_nascimento=data_nascimento,
            senha=generate_password_hash(senha, method='pbkdf2:sha256', salt_length=8)
        )

        db.session.add(funcionario)
        db.session.commit()

        logger.info("Funcionario criado com sucesso: %s", funcionario.to_dict())

        # Criação do Administrador
        administrador = Administrador(
            id_funcionario=funcionario.id_funcionario,
            responsabilidade=responsabilidade,
            data_contratacao=data_contratacao
        )

        db.session.add(administrador)
        db.session.commit()

        logger.info("Administrador criado com sucesso: %s", administrador.to_dict())
        return jsonify({"message": "Administrador criado com sucesso!"}), 201

    except IntegrityError as e:
        logger.error("Erro de integridade ao criar administrador: %s", str(e))
        db.session.rollback()
        return jsonify({"message": "Erro de integridade ao criar administrador: " + str(e)}), 400

# Rota para recuperação de senha
@administrador_bp.route('/recuperar-senha', methods=['POST'])
def recuperar_senha_administrador():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({"message": "Email é obrigatório"}), 400

    administrador = AdministradorService.buscar_por_email(email)
    if administrador:
        token = AdministradorService.gerar_token_recuperacao(administrador)
        return jsonify({"message": "Token de recuperação enviado", "token": token}), 200

    return jsonify({"message": "Email não encontrado"}), 400

# Rota para atualizar a senha
@administrador_bp.route('/atualizar-senha', methods=['POST'])
def atualizar_senha_administrador():
    data = request.get_json()
    logger.info("Dados recebidos para atualização de senha: %s", data)

    token = data.get('token')
    nova_senha = data.get('nova_senha')

    if not token or not nova_senha:
        logger.warning("Token ou nova senha ausentes: token=%s, nova_senha=%s", token, nova_senha)
        return jsonify({"message": "Token e nova senha são obrigatórios"}), 400

    administrador = AdministradorService.atualizar_senha(token, nova_senha)
    if administrador:
        return jsonify({"message": "Senha atualizada com sucesso"}), 200

    return jsonify({"message": "Token inválido ou expirado"}), 400

