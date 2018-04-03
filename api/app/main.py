from flask import Flask, jsonify


from app.mongodb.connector import handle_connection
from app.routes.events import blueprint as events


app = Flask(__name__)
app.register_blueprint(events)


@app.route('/health-check')
def health_check():
    with handle_connection():
        return jsonify({"message": "I'm alive."})
