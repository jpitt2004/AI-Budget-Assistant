from flask import Flask, jsonify
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Budget Assistant for Students"

@app.route("/expenses")
def expenses():
    data = []
    with open("data/sample-expenses.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
