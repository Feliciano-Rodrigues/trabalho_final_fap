from flask import Blueprint, request, jsonify
from service.auxiliar_veterinario_service import AuxiliarVeterinarioService

auxiliar_veterinario_bp = Blueprint('auxiliar_veterinario', __name__)

@auxiliar_veterinario_bp.route('/auxiliar_veterinario', methods=['POST'])
def criar_auxiliar_veterinario():
    data = request.get_json()
    try:
        auxiliar_veterinario = AuxiliarVeterinarioService.add_auxiliar_veterinario(data)
        return jsonify(auxiliar_veterinario), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@auxiliar_veterinario_bp.route('/auxiliar_veterinario/<int:id_funcionario>', methods=['GET'])
def obter_auxiliar_veterinario(id_funcionario):
    auxiliar_veterinario = AuxiliarVeterinarioService.obter_auxiliar_veterinario(id_funcionario)
    if auxiliar_veterinario:
        return jsonify(auxiliar_veterinario), 200
    return jsonify({"message": "Auxiliar Veterinário não encontrado"}), 404

@auxiliar_veterinario_bp.route('/auxiliar_veterinario/<int:id_funcionario>', methods=['PUT'])
def atualizar_auxiliar_veterinario(id_funcionario):
    data = request.get_json()
    try:
        auxiliar_veterinario = AuxiliarVeterinarioService.atualizar_auxiliar_veterinario(id_funcionario, data)
        if auxiliar_veterinario:
            return jsonify(auxiliar_veterinario), 200
        return jsonify({"message": "Auxiliar Veterinário não encontrado"}), 404
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@auxiliar_veterinario_bp.route('/auxiliar_veterinario/<int:id_funcionario>', methods=['DELETE'])
def deletar_auxiliar_veterinario(id_funcionario):
    sucesso = AuxiliarVeterinarioService.deletar_auxiliar_veterinario(id_funcionario)
    if sucesso:
        return jsonify({"message": "Auxiliar Veterinário deletado com sucesso"}), 204
    return jsonify({"message": "Auxiliar Veterinário não encontrado"}), 404
