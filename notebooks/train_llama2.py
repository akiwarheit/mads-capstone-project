import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from datasets import Dataset

# Replace 'your_huggingface_token' with your actual Hugging Face token
huggingface_token = "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"

processed_output_file = "../data/processed/processed_personas_text.txt"

with open(processed_output_file, 'r', encoding='utf-8') as f:
    processed_text = f.read()

max_length = 256 #512
text_chunks = [processed_text[i:i+max_length] for i in range(0, len(processed_text), max_length)]

dataset = Dataset.from_dict({"text": text_chunks})

# Authenticate using the token
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf", token=huggingface_token)
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf", token=huggingface_token)

# Set the pad_token to eos_token
tokenizer.pad_token = tokenizer.eos_token

def tokenize_function(examples):
    encoding = tokenizer(examples["text"], truncation=True, padding="max_length", max_length=max_length)
    encoding["labels"] = encoding["input_ids"].copy()
    return encoding

tokenized_dataset = dataset.map(tokenize_function, batched=True)

training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=1,  # Reduce batch size if needed
    gradient_accumulation_steps=4,  # Accumulate gradients to simulate larger batch size
    save_steps=10_000,
    save_total_limit=2,
    report_to="none",  # Disable reporting to Wandb or Tensorboard
    use_cpu=True  # Ensure no GPU is used
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
)


trainer.train()
model.save_pretrained("../models/fine-tuned-llama2")
tokenizer.save_pretrained("../models/fine-tuned-llama2")