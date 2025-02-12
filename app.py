from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv  # type: ignore

app = Flask(__name__)
CORS(app)  # Allow all origins for testing

load_dotenv()  # Load environment variables

openai.api_key = os.getenv("OPENAI_API_KEY:", "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")  # Securely get the key

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    
    if not user_message:
        return jsonify({"reply": "Sorry, I didn't understand that."})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are PFC Africa's AI Assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response["choices"][0]["message"]["content"]
    except Exception as e:
        reply = "Sorry, I couldn't process that request."

    return jsonify({"reply": reply})  # ✅ Corrected return placement

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Default to 10000 or use Render's assigned port
    app.run(host="0.0.0.0", port=port, debug=True)

