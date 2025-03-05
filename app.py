from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

leaderboard_file = "leaderboard.json"

def load_leaderboard():
    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, "r") as file:
            return json.load(file)
    return []

def save_leaderboard(leaderboard):
    with open(leaderboard_file, "w") as file:
        json.dump(leaderboard, file)

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    leaderboard = load_leaderboard()
    return jsonify(leaderboard)

@app.route('/leaderboard', methods=['POST'])
def submit_score():
    data = request.json
    leaderboard = load_leaderboard()
    leaderboard.append(data)
    leaderboard = sorted(leaderboard, key=lambda x: x["score"], reverse=True)
    save_leaderboard(leaderboard)
    return jsonify({"status": "success"}), 201

if __name__ == '__main__':
    app.run(debug=True)