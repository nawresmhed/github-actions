from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API!", "status":"ok"}), 200

@app.route('/about')
def about():
    return jsonify({"author": "Nawres", "goal": "A simple tutorial to understand Github Actions"}), 200

if __name__ == '__main__':
    app.run(debug=True)
