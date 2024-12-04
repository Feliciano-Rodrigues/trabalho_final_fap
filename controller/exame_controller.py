from flask import Blueprint, request, jsonify
from service.exame_service import ExameService

exame_bp = Blueprint('exame', __name__)

@exame_bp.route('/exame', methods=['POST'])
def criar_exame():
    data = request.get_json()
    exame = ExameService.criar_exame(data)
    return jsonify(exame), 201

@exame_bp.route('/exame/<int:id_exame>', methods=['GET'])
def obter_exame(id_exame):
    exame = ExameService.obter_exame(id_exame)
    if exame:
        return jsonify(exame), 200
    return jsonify({"message": "Exame não encontrado"}), 404

@exame_bp.route('/exame/<int:id_exame>', methods=['PUT'])
def atualizar_exame(id_exame):
    data = request.get_json()
    exame = ExameService.atualizar_exame(id_exame, data)
    if exame:
        return jsonify(exame), 200
    return jsonify({"message": "Exame não encontrado"}), 404

@exame_bp.route('/exame/<int:id_exame>', methods=['DELETE'])
def deletar_exame(id_exame):
    sucesso = ExameService.deletar_exame(id_exame)
    if sucesso:
        return jsonify({"message": "Exame deletado com sucesso"}), 204
    return jsonify({"message": "Exame não encontrado"}), 404
