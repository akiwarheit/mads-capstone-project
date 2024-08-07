from flask import Flask, request, jsonify
from flask_cors import CORS

from inference import query_endpoint

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get("question", "")
    
    response = query_endpoint({ "inputs": question })[0]['generated_text'].replace(question, '').strip()
    
    return jsonify({"response": f"{response}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)