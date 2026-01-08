from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)   #  IMPORTANT: Allow frontend to access backend

movies = [
    {"id": 1, "name": "Inception", "year": 2010},
    {"id": 2, "name": "Interstellar", "year": 2014},
    {"id": 3, "name": "Interstellar", "year": 2014}
]

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/movies", methods=["GET"])
def get_movies():
    return jsonify(movies)

@app.route("/movies", methods=["POST"])
def add_movie():
    data = request.json
    movie = {
        "id": len(movies) + 1,
        "name": data["name"],
        "year": data["year"]
    }
    movies.append(movie)
    return jsonify(movie), 201

@app.route("/")
def home():
    return "Movie API Running"

#  ONLY ONE app.run()
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

