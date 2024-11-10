from flask import Flask, render_template, request, jsonify
from llm import llm_output

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json.get("user_input")
    if user_input:
        bot_response = llm_output(user_input)
        return jsonify({"response": bot_response})
    return jsonify({"response": "No input received."})

    

if __name__ == "__main__":
    app.run(debug=True)
