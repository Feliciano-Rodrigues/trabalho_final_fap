from flask import Blueprint, request, jsonify
from service.veterinario_service import VeterinarioService

veterinario_bp = Blueprint('veterinario', __name__)
veterinario_service = VeterinarioService()

@veterinario_bp.route('/veterinarios', methods=['GET'])
def get_veterinarios():
    veterinarios = veterinario_service.get_all_veterinarios()
    return jsonify([vet.to_dict() for vet in veterinarios]), 200

@veterinario_bp.route('/veterinarios/<int:id>', methods=['GET'])
def get_veterinario(id):
    veterinario = veterinario_service.get_veterinario_by_id(id)
    if veterinario:
        return jsonify(veterinario), 200
    return jsonify({'message': 'Veterinario não encontrado'}), 404

@veterinario_bp.route('/veterinarios', methods=['POST'])
def create_veterinario():
    data = request.get_json()
    try:
        new_veterinario = veterinario_service.create_veterinario(data)
        return jsonify(new_veterinario), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@veterinario_bp.route('/veterinarios/<int:id>', methods=['PUT'])
def update_veterinario(id):
    data = request.get_json()
    updated_veterinario = veterinario_service.update_veterinario(id, data)
    if updated_veterinario:
        return jsonify(updated_veterinario), 200
    return jsonify({'message': 'Veterinario não encontrado'}), 404

@veterinario_bp.route('/veterinarios/<int:id>', methods=['DELETE'])
def delete_veterinario(id):
    result = veterinario_service.delete_veterinario(id)
    if result:
        return jsonify({'message': 'Veterinario deletado'}), 200
    return jsonify({'message': 'Veterinario não encontrado'}), 404
