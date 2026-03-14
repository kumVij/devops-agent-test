from flask import Flask, jsonify
from utils.calculator import add, divide

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "ok", "message": "DevOps Agent Test App"})

@app.route("/calculate")
def calculate():
    result = add(10, 5)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True, port=5000)