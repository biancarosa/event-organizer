from flask import Flask, jsonify
from mongodb import connector as mongo_connector

app = Flask(__name__)
mongo_connector.connect()

@app.route('/health-check')
def health_check():
    return jsonify({"message" : "I'm alive."})