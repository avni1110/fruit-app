from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

FRUITS = [
    {
        "id": 1,
        "name": "Apple",
        "price": 220,
        "unit": "kg"
    },
    {
        "id": 2,
        "name": "Strawberry",
        "price": 280,
        "unit": "200g"
    },
    {
        "id": 3,
        "name": "Watermelon",
        "price": 120,
        "unit": "piece"
    },
    {
        "id": 4,
        "name": "Orange",
        "price": 110,
        "unit": "kg"
    },
    {
        "id": 5,
        "name": "Grapes",
        "price": 95,
        "unit": "500g"
    },
    {
    "id": 6,
    "name": "Mango",
    "price": 180,
    "unit": "kg"
    }
]

@app.route("/api/health")
def get_health():
    return jsonify({
        "status": "ok",
        "message": "Fruit Store API is running"
    })


@app.route("/api/fruits")
def get_fruits():

    return jsonify(FRUITS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)