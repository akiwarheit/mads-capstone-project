import json
import boto3
newline, bold, unbold = "\n", "\033[1m", "\033[0m"
endpoint_name = "jumpstart-dft-hf-text2text-flan-t5-20240804-092102"

def query_endpoint(payload, aws_access_key_id, aws_secret_access_key):
    client = boto3.client("runtime.sagemaker",
        region_name="us-east-1",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )
    response = client.invoke_endpoint(
        EndpointName=endpoint_name, ContentType="application/json", Body=json.dumps(payload).encode("utf-8")
    )
    model_predictions = json.loads(response["Body"].read())
    generated_text = model_predictions[0]["generated_text"]

    return generated_text