from flask import Flask, jsonify, request
from models.event import Event
from mongodb import connector as mongo_connector

app = Flask(__name__)
mongo_connector.connect()

@app.route('/health-check')
def health_check():
    return jsonify({"message" : "I'm alive."})

@app.route('/events', methods=['GET'])
def list_events():
    events_obj = Event.objects()
    events = []
    for event in events_obj:
        events.append({'id' : str(event.id), 'name' : event.name, 'date' : event.date })
    return jsonify({"data" : events}), 200

@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    event = Event()
    event.name = data.get('name')
    event.date = data.get('date')
    event.save()
    return jsonify({"data" : {'id' : str(event.id), 'name' : event.name, 'date' : event.date }}), 201
