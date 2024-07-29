from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch
from flask_cors import CORS
from peft import LoraConfig

app = Flask(__name__)
CORS(app)

# @TODO ADJUST THE LLAMA MODEL HERE
MODEL_NAME = "NousResearch/Llama-2-7b-chat-hf" # "../notebooks/results"

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    quantization_config=bnb_config
)
model.config.use_cache = False
model.config.pretraining_tp = 1

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

peft_config = LoraConfig(
    lora_alpha=16,
    lora_dropout=0.1,
    r=64,
    bias="none",
    task_type="CAUSAL_LM",
)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get("question", "")
    
    if not question:
        return jsonify({"error": "No question provided"}), 400
    
    # Tokenize and prepare input
    inputs = tokenizer(question, return_tensors="pt").to("cuda")
    output = model.generate(**inputs, max_length=128)
    
    # Decode and return the response
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
