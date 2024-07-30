import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

save_directory="./results-v2"

tokenizer = AutoTokenizer.from_pretrained(save_directory)

model = AutoModelForCausalLM.from_pretrained(save_directory)
#
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

model.quantization_config = bnb_config
#
# model.config.use_cache = False
# model.config.pretraining_tp = 1

input_text = "Autauga County, Alabama?"
inputs = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(inputs['input_ids'], max_length=128)

generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_text)