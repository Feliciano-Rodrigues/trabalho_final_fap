from flask import Blueprint, request, jsonify
from service.medicamento_service import MedicamentoService

medicamento_bp = Blueprint('medicamento', __name__)

@medicamento_bp.route('/medicamento', methods=['POST'])
def criar_medicamento():
    data = request.get_json()
    medicamento = MedicamentoService.criar_medicamento(data)
    return jsonify(medicamento), 201

@medicamento_bp.route('/medicamento/<int:id_medicamento>', methods=['GET'])
def obter_medicamento(id_medicamento):
    medicamento = MedicamentoService.obter_medicamento(id_medicamento)
    if medicamento:
        return jsonify(medicamento), 200
    return jsonify({"message": "Medicamento não encontrado"}), 404

@medicamento_bp.route('/medicamento/<int:id_medicamento>', methods=['PUT'])
def atualizar_medicamento(id_medicamento):
    data = request.get_json()
    medicamento = MedicamentoService.atualizar_medicamento(id_medicamento, data)
    if medicamento:
        return jsonify(medicamento), 200
    return jsonify({"message": "Medicamento não encontrado"}), 404

@medicamento_bp.route('/medicamento/<int:id_medicamento>', methods=['DELETE'])
def deletar_medicamento(id_medicamento):
    sucesso = MedicamentoService.deletar_medicamento(id_medicamento)
    if sucesso:
        return jsonify({"message": "Medicamento deletado com sucesso"}), 204
    return jsonify({"message": "Medicamento não encontrado"}), 404
