from sagemaker.predictor import retrieve_default
import argparse
import boto3

parser = argparse.ArgumentParser(description='Access SageMaker endpoint with AWS credentials')
parser.add_argument('-key', type=str, required=True, help='AWS Access Key')
parser.add_argument('-secret', type=str, required=True, help='AWS Secret Key')

args = parser.parse_args()

session = boto3.Session(
    aws_access_key_id=args.key,
    aws_secret_access_key=args.secret,
    region_name='us-east-1'
)

endpoint_name = "llama-2-7b-chat-011912-Endpoint-20240819-015325"
predictor = retrieve_default(endpoint_name)


def query_endpoint(inputs):
    inputs["parameters"] = {
        "max_new_tokens": 1024,
        "top_p": 0.1,
        "temperature": 0.2
    }

    return predictor.predict(inputs)