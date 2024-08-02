from flask import Flask, request, jsonify
from flask_cors import CORS

from inference import query_endpoint
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-key", "--aws_access_key_id", help="AWS Access Key ID")
parser.add_argument("-secret", "--aws_secret_access_key", help="Secret Access Key")

args = parser.parse_args()

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get("question", "")
    
    if not question:
        return jsonify({"error": "No question provided"}), 400
    
    response = query_endpoint({ "inputs": question }, aws_access_key_id=args.aws_access_key_id, aws_secret_access_key=args.aws_secret_access_key)
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
