from flask import Blueprint, request, jsonify
from entity import paciente
from service.paciente_service import PacienteService

paciente_bp = Blueprint('paciente', __name__)

@paciente_bp.route('/paciente', methods=['POST'])
def criar_paciente():
    data = request.get_json()
    paciente = PacienteService.criar_paciente(data)
    return jsonify(paciente), 201

@paciente_bp.route('/paciente/<int:id_paciente>', methods=['GET'])
def obter_paciente(id_paciente):
    paciente = PacienteService.obter_paciente(id_paciente)
    if paciente:
        return jsonify(paciente), 200
    return jsonify({"message": "Paciente não encontrado"}), 404

@paciente_bp.route('/paciente/<int:id_paciente>', methods=['PUT'])
def atualizar_paciente(id_paciente):
    data = request.get_json()
    paciente = PacienteService.atualizar_paciente(id_paciente, data)
    if paciente:
        return jsonify(paciente), 200
    return jsonify({"message": "Paciente não encontrado"}), 404

@paciente_bp.route('/paciente/<int:id_paciente>', methods=['DELETE'])
def deletar_paciente(id_paciente):
    sucesso = PacienteService.deletar_paciente(id_paciente)
    if sucesso:
        return jsonify({"message": "Paciente deletado com sucesso"}), 204
    return jsonify({"message": "Paciente não encontrado"}), 404
