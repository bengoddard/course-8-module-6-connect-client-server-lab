from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='./client', static_url_path='')
CORS(app)

events = [
    {"id": 1, "title": "Yoga in the Park"},
    {"id": 2, "title": "Lake 5K Run"}
]

@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome!"}), 200


@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events), 200

@app.route("/events", methods=["POST"])
def add_event():
    data = request.get_json()
    new_id = max((e["id"] for e in events), default=0) + 1
    if "title" not in data or not data["title"]:
        return ("Missing required field: title"), 400
    else:
        new_event = {"id": new_id, "title": data["title"]}
        events.append(new_event)
    if new_event:
        return jsonify(new_event), 201
    else:
        return ("Event not found"), 400

if __name__ == "__main__":
    app.run(debug=True)
