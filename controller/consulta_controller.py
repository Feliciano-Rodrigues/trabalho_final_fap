from flask import Blueprint, request, jsonify
from service.consulta_service import ConsultaService

consulta_bp = Blueprint('consulta', __name__)

@consulta_bp.route('/consulta', methods=['POST'])
def criar_consulta():
    data = request.get_json()
    consulta = ConsultaService.criar_consulta(data)
    return jsonify(consulta), 201

@consulta_bp.route('/consulta/<int:id_consulta>', methods=['GET'])
def obter_consulta(id_consulta):
    consulta = ConsultaService.obter_consulta(id_consulta)
    if consulta:
        return jsonify(consulta), 200
    return jsonify({"message": "Consulta não encontrada"}), 404

@consulta_bp.route('/consulta/<int:id_consulta>', methods=['PUT'])
def atualizar_consulta(id_consulta):
    data = request.get_json()
    consulta = ConsultaService.atualizar_consulta(id_consulta, data)
    if consulta:
        return jsonify(consulta), 200
    return jsonify({"message": "Consulta não encontrada"}), 404

@consulta_bp.route('/consulta/<int:id_consulta>', methods=['DELETE'])
def deletar_consulta(id_consulta):
    sucesso = ConsultaService.deletar_consulta(id_consulta)
    if sucesso:
        return jsonify({"message": "Consulta deletada com sucesso"}), 204
    return jsonify({"message": "Consulta não encontrada"}), 404
