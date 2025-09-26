
from flask import Flask, request, jsonify
from models.optimizer import RailwayOptimizer
import json

app = Flask(__name__)
optimizer = RailwayOptimizer("railway_network.json")

@app.route("/shortest_path", methods=["GET"])
def shortest_path():
    start = request.args.get("start")
    end = request.args.get("end")
    result = optimizer.get_shortest_path(start, end)
    return jsonify(result)

@app.route("/stations", methods=["GET"])
def stations():
    return jsonify(optimizer.get_stations())

if __name__ == "__main__":
    app.run(debug=True)
