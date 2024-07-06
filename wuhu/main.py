import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the fine-tuned model and tokenizer
model_path = './fine_tuned_model'
model = GPT2LMHeadModel.from_pretrained(model_path)
tokenizer = GPT2Tokenizer.from_pretrained(model_path)

# Function to generate text
def generate_text(prompt, max_length=50, num_return_sequences=1):
    # Encode the input prompt
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    
    # Generate text using the model
    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_length=max_length,
            num_return_sequences=num_return_sequences,
            pad_token_id=tokenizer.eos_token_id,
            no_repeat_ngram_size=2,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.7
        )
    
    # Decode the generated text
    generated_texts = [tokenizer.decode(output[i], skip_special_tokens=True) for i in range(num_return_sequences)]
    
    return generated_texts

# Example usage
prompt = input("Enter Prompt: ")
generated_texts = generate_text(prompt, max_length=50, num_return_sequences=3)

print(generated_texts)
