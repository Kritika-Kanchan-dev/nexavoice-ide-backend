from flask import Flask, request, jsonify
from flask_cors import CORS
from llm_handler import GeminiAssistant
from db import debug_collection, autofix_collection, generate_collection
from datetime import datetime


app = Flask(__name__)
CORS(app)

assistant = GeminiAssistant()

@app.route("/")
def home():
    return {"message": "Backend is running!"}

@app.route("/debug", methods=["POST"])
def debug_code():
    data = request.json
    code = data.get("code", "")

    result = assistant.debug_code(code)

    debug_collection.insert_one({
        "input_code": code,
        "debug_output": result,
        "timestamp": datetime.utcnow()
    })

    return jsonify({"output": result})

@app.route("/autofix", methods=["POST"])
def autofix_code():
    data = request.json
    code = data.get("code", "")

    result = assistant.auto_fix_code(code)

    autofix_collection.insert_one({
        "original_code": code,
        "fixed_code": result,
        "timestamp": datetime.utcnow()
    })

    return jsonify({"output": result})

@app.route("/testcases", methods=["POST"])
def testcases():
    data = request.json
    code = data.get("code", "")

    result = assistant.generate_testcases(code)
    return jsonify({"output": result})

@app.route("/generate", methods=["POST"])
def generate_code():
    data = request.json
    prompt = data.get("prompt", "")

    result = assistant.generate_code(prompt)

    generate_collection.insert_one({
        "prompt": prompt,
        "generated_code": result,
        "timestamp": datetime.utcnow()
    })

    return jsonify({"output": result})



if __name__ == "__main__":
    app.run(debug=True)
