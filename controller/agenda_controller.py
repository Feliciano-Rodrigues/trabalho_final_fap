from flask import Blueprint, request, jsonify
from service.agenda_service import AgendaService

agenda_bp = Blueprint('agenda', __name__)

@agenda_bp.route('/agenda', methods=['POST'])
def criar_agenda():
    data = request.get_json()
    agenda = AgendaService.criar_agenda(data)
    return jsonify(agenda), 201

@agenda_bp.route('/agenda/<int:id_agenda>', methods=['GET'])
def obter_agenda(id_agenda):
    agenda = AgendaService.obter_agenda(id_agenda)
    if agenda:
        return jsonify(agenda), 200
    return jsonify({"message": "Agenda não encontrada"}), 404

@agenda_bp.route('/agenda/<int:id_agenda>', methods=['PUT'])
def atualizar_agenda(id_agenda):
    data = request.get_json()
    agenda = AgendaService.atualizar_agenda(id_agenda, data)
    if agenda:
        return jsonify(agenda), 200
    return jsonify({"message": "Agenda não encontrada"}), 404

@agenda_bp.route('/agenda/<int:id_agenda>', methods=['DELETE'])
def deletar_agenda(id_agenda):
    sucesso = AgendaService.deletar_agenda(id_agenda)
    if sucesso:
        return jsonify({"message": "Agenda deletada com sucesso"}), 204
    return jsonify({"message": "Agenda não encontrada"}), 404
