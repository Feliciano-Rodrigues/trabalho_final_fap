from flask import Blueprint, request, jsonify
from service.internamento_service import InternamentoService

internamento_bp = Blueprint('internamento', __name__)

@internamento_bp.route('/internamento', methods=['POST'])
def criar_internamento():
    data = request.get_json()
    internamento = InternamentoService.criar_internamento(data)
    return jsonify(internamento), 201

@internamento_bp.route('/internamento/<int:id_internamento>', methods=['GET'])
def obter_internamento(id_internamento):
    internamento = InternamentoService.obter_internamento(id_internamento)
    if internamento:
        return jsonify(internamento), 200
    return jsonify({"message": "Internamento não encontrado"}), 404

@internamento_bp.route('/internamento/<int:id_internamento>', methods=['PUT'])
def atualizar_internamento(id_internamento):
    data = request.get_json()
    internamento = InternamentoService.atualizar_internamento(id_internamento, data)
    if internamento:
        return jsonify(internamento), 200
    return jsonify({"message": "Internamento não encontrado"}), 404

@internamento_bp.route('/internamento/<int:id_internamento>', methods=['DELETE'])
def deletar_internamento(id_internamento):
    sucesso = InternamentoService.deletar_internamento(id_internamento)
    if sucesso:
        return jsonify({"message": "Internamento deletado com sucesso"}), 204
    return jsonify({"message": "Internamento não encontrado"}), 404
