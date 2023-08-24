import json
import uuid
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data_file = 'data.json'

def load_data():
    try:
        with open(data_file, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {[]}

def save_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/presentations', methods=['POST'])
def add_new_presentation():
    new_presentation = request.json
    presentations_data = load_data()
    
    new_presentation['id'] = str(uuid.uuid4())  # Generate a unique ID for the presentation
    presentations_data.append(new_presentation)
    save_data(presentations_data)
    
    return jsonify({"message": "Presentation added successfully"}), 201

@app.route('/presentations', methods=['GET'])
def list_all_presentations():
    presentations_data = load_data()
    return jsonify(presentations_data), 200

@app.route('/presentations/<string:presentation_id>', methods=['GET'])
def get_presentation(presentation_id):
    presentations_data = load_data()
    for presentation in presentations_data:
        if presentation['id'] == presentation_id:
            return jsonify(presentation), 200
    return jsonify({"message": "Presentation not found"}), 404

@app.route('/presentations/<string:presentation_id>', methods=['PUT'])
def modify_presentation(presentation_id):
    modified_presentation = request.json
    presentations_data = load_data()
    
    for presentation in presentations_data:
        if presentation['id'] == presentation_id:
            presentation.update(modified_presentation)
            save_data(presentations_data)
            return jsonify({"message": "Presentation modified successfully"}), 200
    
    return jsonify({"message": "Presentation not found"}), 404

@app.route('/presentations/<string:presentation_id>', methods=['DELETE'])
def delete_presentation(presentation_id):
    presentations_data = load_data()
    
    for presentation in presentations_data:
        if presentation['id'] == presentation_id:
            presentations_data.remove(presentation)
            save_data(presentations_data)
            return jsonify({"message": "Presentation deleted successfully"}), 200
    
    return jsonify({"message": "Presentation not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
