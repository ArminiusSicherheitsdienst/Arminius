from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# OpenAI API-Schlüssel
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=user_message,
        max_tokens=150
    )
    bot_message = response.choices[0].text.strip()
    return jsonify({"message": bot_message})

if __name__ == "__main__":
    app.run(debug=True)
