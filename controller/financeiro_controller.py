from flask import Blueprint, request, jsonify
from service.financeiro_service import FinanceiroService

financeiro_bp = Blueprint('financeiro', __name__)

@financeiro_bp.route('/financeiro', methods=['POST'])
def criar_financeiro():
    data = request.get_json()
    financeiro = FinanceiroService.criar_financeiro(data)
    return jsonify(financeiro), 201

@financeiro_bp.route('/financeiro/<int:id_financeiro>', methods=['GET'])
def obter_financeiro(id_financeiro):
    financeiro = FinanceiroService.obter_financeiro(id_financeiro)
    if financeiro:
        return jsonify(financeiro), 200
    return jsonify({"message": "Financeiro não encontrado"}), 404

@financeiro_bp.route('/financeiro/<int:id_financeiro>', methods=['PUT'])
def atualizar_financeiro(id_financeiro):
    data = request.get_json()
    financeiro = FinanceiroService.atualizar_financeiro(id_financeiro, data)
    if financeiro:
        return jsonify(financeiro), 200
    return jsonify({"message": "Financeiro não encontrado"}), 404

@financeiro_bp.route('/financeiro/<int:id_financeiro>', methods=['DELETE'])
def deletar_financeiro(id_financeiro):
    sucesso = FinanceiroService.deletar_financeiro(id_financeiro)
    if sucesso:
        return jsonify({"message": "Financeiro deletado com sucesso"}), 204
    return jsonify({"message": "Financeiro não encontrado"}), 404
