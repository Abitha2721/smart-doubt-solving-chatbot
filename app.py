from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load dataset
data = pd.read_csv("dataset.csv")

# Check whether dataset loaded correctly
print(data.head())

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json["question"].strip().lower()

    answer = "Sorry, I don't know the answer."

    for i in range(len(data)):
        db_question = str(data["Question"][i]).strip().lower()

        if question == db_question:
            answer = data["Answer"][i]
            break

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)