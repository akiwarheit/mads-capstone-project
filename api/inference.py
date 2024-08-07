from sagemaker.predictor import retrieve_default
endpoint_name = "jumpstart-dft-meta-textgeneration-l-20240807-011912"
predictor = retrieve_default(endpoint_name)


def query_endpoint(inputs):
    inputs["parameters"] = {
        "max_new_tokens": 1024,
        "top_p": 0.1,
        "temperature": 0.2
    }

    return predictor.predict(inputs)