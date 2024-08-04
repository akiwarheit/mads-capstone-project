from flask import Flask, request, jsonify
from flask_cors import CORS

from inference import query_endpoint
from argparse import ArgumentParser

from questionnaire import generate_question
# from env_loader import EnvLoader
# import os
#
# EnvLoader.load_env_file('../local.env')
# aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
# aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

parser = ArgumentParser()
parser.add_argument("-key", "--aws_access_key_id", help="AWS Access Key ID")
parser.add_argument("-secret", "--aws_secret_access_key", help="Secret Access Key")

args = parser.parse_args()

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get("questions", "")
    response = data.get("responses", "")
    if not question:
        return jsonify({"error": "No question provided"}), 400

    q = generate_question(question, response)
    print(q)
    
    response = query_endpoint({ "inputs": q }, aws_access_key_id=args.aws_access_key_id, aws_secret_access_key=args.aws_secret_access_key)
    
    return jsonify({"response": f"{response}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    # app.run(host='0.0.0.0', port=5000) # TODO switch back to this when commiting
