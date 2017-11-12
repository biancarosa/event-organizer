from flask import Flask, jsonify, request
from models.event import Event
from app import flask_app

@flask_app.route('/events', methods=['GET'])
def list_events():
    events_obj = Event.objects()
    events = []
    for event in events_obj:
        events.append({'id' : str(event.id), 'name' : event.name, 'date' : event.date })
    return jsonify({"data" : events}), 200

@flask_app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    event = Event()
    event.name = data.get('name')
    event.date = data.get('date')
    event.save()
    return jsonify({"data" : {'id' : str(event.id), 'name' : event.name, 'date' : event.date }}), 201