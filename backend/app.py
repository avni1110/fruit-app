from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api/health")
def health():
    return jsonify({
        "status": "ok"
    })


@app.route("/api/fruits")
def fruits():

    return jsonify([
        {
            "name": "Apple",
            "price": 100
        },
        {
            "name": "Strawberry",
            "price": 150
        },
        {
            "name": "Watermelon",
            "price": 60
        },
        {
            "name": "Orange",
            "price": 80
        },
        {
            "name": "Grapes",
            "price": 120
        }
    ])


if __name__ == "__main__":
    app.run(debug=True, port=8000)