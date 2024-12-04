from flask import Blueprint, request, jsonify
from service.cirurgia_service import CirurgiaService

cirurgia_bp = Blueprint('cirurgia', __name__)

@cirurgia_bp.route('/cirurgia', methods=['POST'])
def criar_cirurgia():
    data = request.get_json()
    cirurgia = CirurgiaService.criar_cirurgia(data)
    return jsonify(cirurgia), 201

@cirurgia_bp.route('/cirurgia/<int:id_cirurgia>', methods=['GET'])
def obter_cirurgia(id_cirurgia):
    cirurgia = CirurgiaService.obter_cirurgia(id_cirurgia)
    if cirurgia:
        return jsonify(cirurgia), 200
    return jsonify({"message": "Cirurgia não encontrada"}), 404

@cirurgia_bp.route('/cirurgia/<int:id_cirurgia>', methods=['PUT'])
def atualizar_cirurgia(id_cirurgia):
    data = request.get_json()
    cirurgia = CirurgiaService.atualizar_cirurgia(id_cirurgia, data)
    if cirurgia:
        return jsonify(cirurgia), 200
    return jsonify({"message": "Cirurgia não encontrada"}), 404

@cirurgia_bp.route('/cirurgia/<int:id_cirurgia>', methods=['DELETE'])
def deletar_cirurgia(id_cirurgia):
    sucesso = CirurgiaService.deletar_cirurgia(id_cirurgia)
    if sucesso:
        return jsonify({"message": "Cirurgia deletada com sucesso"}), 204
    return jsonify({"message": "Cirurgia não encontrada"}), 404
