from flask import Blueprint, request, jsonify
from service.prescricao_service import PrescricaoService

prescricao_bp = Blueprint('prescricao', __name__)

@prescricao_bp.route('/prescricao', methods=['POST'])
def criar_prescricao():
    data = request.get_json()
    prescricao = PrescricaoService.criar_prescricao(data)
    return jsonify(prescricao), 201

@prescricao_bp.route('/prescricao/<int:id_prescricao>', methods=['GET'])
def obter_prescricao(id_prescricao):
    prescricao = PrescricaoService.obter_prescricao(id_prescricao)
    if prescricao:
        return jsonify(prescricao), 200
    return jsonify({"message": "Prescrição não encontrada"}), 404

@prescricao_bp.route('/prescricao/<int:id_prescricao>', methods=['PUT'])
def atualizar_prescricao(id_prescricao):
    data = request.get_json()
    prescricao = PrescricaoService.atualizar_prescricao(id_prescricao, data)
    if prescricao:
        return jsonify(prescricao), 200
    return jsonify({"message": "Prescrição não encontrada"}), 404

@prescricao_bp.route('/prescricao/<int:id_prescricao>', methods=['DELETE'])
def deletar_prescricao(id_prescricao):
    sucesso = PrescricaoService.deletar_prescricao(id_prescricao)
    if sucesso:
        return jsonify({"message": "Prescrição deletada com sucesso"}), 204
    return jsonify({"message": "Prescrição não encontrada"}), 404
