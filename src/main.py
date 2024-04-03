import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

api_key = os.getenv('API-KEY')

genai.configure(api_key=api_key)

@app.route(
    "/prompt",
    methods=["POST"],
)

def prompt():
    data = request.json()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({
            "error": "Prompt is required",
        }), 400

    try:
        model = genai.GenerativeModel("gemini-pro")

        response = model.generate_content(prompt)

        return jsonify({
            "response": response.text
        })

    except Exception as e:
        return jsonify({
            "error": "Request Failed",
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
