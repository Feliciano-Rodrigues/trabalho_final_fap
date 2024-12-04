from flask import Blueprint, request, jsonify
from service.cliente_service import ClienteService
  
cliente_bp = Blueprint('cliente_bp', __name__)
cliente_service = ClienteService()

@cliente_bp.route('/clientes', methods=['GET'])
def get_clientes():
    clientes = cliente_service.get_all_clientes()
    result = [
        {
            'id_cliente': cliente.id_cliente,
            'nome': cliente.nome,
            'cpf': cliente.cpf,
            'email': cliente.email,
            'telefone': cliente.telefone,
            'endereco': cliente.endereco
        }
        for cliente in clientes
    ]
    return jsonify(result), 200

@cliente_bp.route('/clientes/<int:id_cliente>', methods=['GET'])
def get_cliente(id_cliente):
    cliente = cliente_service.get_cliente_by_id(id_cliente)
    if cliente:
        return jsonify({
            'id_cliente': cliente.id_cliente,
            'nome': cliente.nome,
            'cpf': cliente.cpf,
            'email': cliente.email,
            'telefone': cliente.telefone,
            'endereco': cliente.endereco
        }), 200
    return jsonify({'message': 'Cliente não encontrado'}), 404

@cliente_bp.route('/clientes', methods=['POST'])
def create_cliente():
    data = request.get_json()
    required_fields = ['nome', 'cpf', 'email', 'telefone', 'endereco']
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        return jsonify({'error': 'Campos obrigatórios ausentes', 'missing_fields': missing_fields}), 400

    novo_cliente = cliente_service.create_cliente(data)
    return jsonify({
        'id_cliente': novo_cliente.id_cliente,
        'nome': novo_cliente.nome,
        'cpf': novo_cliente.cpf,
        'email': novo_cliente.email,
        'telefone': novo_cliente.telefone,
        'endereco': novo_cliente.endereco
    }), 201

@cliente_bp.route('/clientes/<int:id_cliente>', methods=['PUT'])
def update_cliente(id_cliente):
    data = request.get_json()
    cliente_atualizado = cliente_service.update_cliente(id_cliente, data)
    if cliente_atualizado:
        return jsonify({
            'id_cliente': cliente_atualizado.id_cliente,
            'nome': cliente_atualizado.nome,
            'cpf': cliente_atualizado.cpf,
            'email': cliente_atualizado.email,
            'telefone': cliente_atualizado.telefone,
            'endereco': cliente_atualizado.endereco
        }), 200
    return jsonify({'message': 'Cliente não encontrado'}), 404

@cliente_bp.route('/clientes/<int:id_cliente>', methods=['DELETE'])
def delete_cliente(id_cliente):
    if cliente_service.delete_cliente(id_cliente):
        return jsonify({'message': 'Cliente deletado com sucesso'}), 200
    return jsonify({'message': 'Cliente não encontrado'}), 404
