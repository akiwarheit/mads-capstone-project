import re

def generate_question(question, response):
    def clean_question(question):
        return re.sub(r'\s*\(.*?\)', '', question).strip()

    q_payload = "Given the following question/answer pairs, recommend me a county to live in the US: \n"
    for i in range(2):
        q_payload += f"{clean_question(question[i])}" + ": " + f"{response[i]}\n"
    return q_payload

