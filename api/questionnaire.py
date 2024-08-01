from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

model_name = 'gpt2'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def provide_reco(profile_str):
    def generate_response(prompt, output_length=100):
        inputs = tokenizer(prompt, return_tensors='pt')
        input_ids = inputs['input_ids']
        attention_mask = inputs['attention_mask']

        max_length = input_ids.shape[1] + output_length
        outputs = model.generate(
            input_ids,
            attention_mask=attention_mask,
            max_length=max_length,
            pad_token_id=tokenizer.eos_token_id,
            num_return_sequences=1
        )
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response


    def make_recommendation(profile_str):
        prompt = (
            f"Based on this profile:\n{profile_str}\n"
            "Considering the user's preferences, which county in the United States would be the best to live in?\n\n"
            "Provide your recommendation in a single sentence."
        )
        recommendation = generate_response(prompt)
        return recommendation

    recommendation = make_recommendation(profile_str)
    return recommendation
