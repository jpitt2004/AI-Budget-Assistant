from flask import Flask, jsonify
import csv

app = Flask(__name__)

def load_expenses():
    data = []
    with open("data/sample-expenses.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["amount"] = float(row["amount"])
            data.append(row)
    return data

@app.route("/")
def home():
    return "AI Budget Assistant for Students"

@app.route("/expenses")
def expenses():
    return jsonify(load_expenses())

@app.route("/prediction")
def prediction():
    data = load_expenses()
    total = sum(item["amount"] for item in data)
    average = total / len(data)

    if average > 15:
        message = "Warning: You may be overspending this month."
    else:
        message = "Good job! Your spending is currently under control."

    return jsonify({
        "average_daily_spending": round(average, 2),
        "alert": message
    })

if __name__ == "__main__":
    app.run(debug=True)
