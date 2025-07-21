from flask import Flask, request, render_template, jsonify
from chatbot.groq_agent import ask_jas_bot
from utils.dashboard_data import get_insights

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    data = get_insights()
    return render_template("dashboard.html", data=data)

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("query")
    print("➡️ Flask received:", user_input)

    # Get the actual response object (likely an AIMessage)
    response_obj = ask_jas_bot(user_input)

    # Extract the text content from AIMessage
    response_text = response_obj.content if hasattr(response_obj, "content") else str(response_obj)

    print("⬅️ Sending back:", response_text)
    return jsonify({"response": response_text})


if __name__ == "__main__":
    app.run(debug=True)
