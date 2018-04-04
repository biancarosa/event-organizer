from flask import jsonify, request, Blueprint
from app.models.event import Event


blueprint = Blueprint('event', __name__)


@blueprint.route('/events', methods=['GET'])
def list_events():
    events_obj = Event.objects()
    events = []
    for event in events_obj:
        events.append({'id': str(event.id), 'name': event.name, 'date': event.date})
    return jsonify({"data": events}), 200


@blueprint.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    event = Event()
    event.name = data.get('name')
    event.date = data.get('date')
    event.save()
    return jsonify({"data": {'id': str(event.id), 'name': event.name, 'date': event.date}}), 201
