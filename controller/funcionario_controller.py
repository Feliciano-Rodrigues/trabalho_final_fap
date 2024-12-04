from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from entity.funcionario import Funcionario
from service.funcionario_service import FuncionarioService
from init_db import db

funcionario_bp = Blueprint('funcionario', __name__)
funcionario_service = FuncionarioService()

# Campos obrigatórios para a entidade Funcionario
REQUIRED_FIELDS = ['nome', 'cpf', 'email', 'telefone', 'endereco', 'data_nascimento', 'senha']

# Listar todos os funcionários
@funcionario_bp.route('/', methods=['GET'])
def get_funcionarios():
    try:
        funcionarios = funcionario_service.get_all_funcionarios()
        if isinstance(funcionarios, list) and all(isinstance(func, Funcionario) for func in funcionarios):
            return jsonify([func.to_dict() for func in funcionarios]), 200
        return jsonify({'message': 'Erro ao buscar funcionários: dados inválidos'}), 500
    except SQLAlchemyError as e:
        return jsonify({'message': 'Erro ao buscar funcionários', 'error': str(e)}), 500

# Obter funcionário por ID
@funcionario_bp.route('/<int:id>', methods=['GET'])
def get_funcionario(id):
    try:
        funcionario = funcionario_service.get_funcionario_by_id(id)
        if funcionario:
            return jsonify(funcionario.to_dict()), 200
        return jsonify({'message': 'Funcionário não encontrado'}), 404
    except SQLAlchemyError as e:
        return jsonify({'message': 'Erro ao buscar funcionário', 'error': str(e)}), 500

# Criar novo funcionário
@funcionario_bp.route('/', methods=['POST'])
def create_funcionario():
    try:
        data = request.get_json()

        # Validação de campos obrigatórios
        for field in REQUIRED_FIELDS:
            if not data.get(field):
                return jsonify({"message": f"Campo obrigatório ausente ou vazio: {field}"}), 400

        # Verificar se o CPF já existe
        cpf = data.get('cpf')
        if Funcionario.query.filter_by(cpf=cpf).first():
            return jsonify({"message": "CPF já cadastrado"}), 400

        # Criar uma nova instância de Funcionario
        new_funcionario = Funcionario(**data)
        db.session.add(new_funcionario)
        db.session.commit()

        return jsonify(new_funcionario.to_dict()), 201

    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"message": "Erro de integridade ao salvar funcionário", "error": str(e.orig)}), 400

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"message": "Erro ao salvar no banco de dados", "error": str(e)}), 500

# Atualizar funcionário
@funcionario_bp.route('/<int:id>', methods=['PUT'])
def update_funcionario(id):
    try:
        data = request.get_json()

        funcionario = Funcionario.query.get(id)
        if not funcionario:
            return jsonify({"message": "Funcionário não encontrado"}), 404

        # Atualizar campos do funcionário
        for key, value in data.items():
            if hasattr(funcionario, key):
                setattr(funcionario, key, value)

        db.session.commit()
        return jsonify(funcionario.to_dict()), 200

    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"message": "Erro de integridade ao atualizar funcionário", "error": str(e)}), 400

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"message": "Erro ao atualizar funcionário", "error": str(e)}), 500

# Deletar funcionário
@funcionario_bp.route('/<int:id>', methods=['DELETE'])
def delete_funcionario(id):
    try:
        funcionario = Funcionario.query.get(id)
        if not funcionario:
            return jsonify({'message': 'Funcionário não encontrado'}), 404

        db.session.delete(funcionario)
        db.session.commit()
        return jsonify({'message': 'Funcionário deletado com sucesso'}), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'message': 'Erro ao deletar funcionário', 'error': str(e)}), 500
