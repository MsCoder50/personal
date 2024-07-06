import pandas as pd
from transformers import GPT2LMHeadModel, GPT2Tokenizer, TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments

# Load the dataset
file_path = './dataset.tsv'  # Update with your file path
data = pd.read_csv(file_path, sep='\t')

# Ensure the column names match your dataset structure
question_column = 'Question'  # Adjust based on your dataset
answer_column = 'Answer'  # Adjust based on your dataset

# Extract text data from relevant columns
train_texts = list(data[question_column])  # Use 'Question' column for training

# Initialize tokenizer with padding token
model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
tokenizer.add_special_tokens({'pad_token': '[PAD]'})  # Add padding token to tokenizer

# Tokenize dataset
train_encodings = tokenizer(train_texts, truncation=True, padding=True)

# Create TextDataset with specified block_size
block_size = 128  # Adjust as needed, based on your dataset and model requirements
train_dataset = TextDataset(
    tokenizer=tokenizer,
    file_path=file_path,  # Pass the file path directly
    block_size=block_size,
)

# Create DataCollator for Language Modeling
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False  # Set to True if you are doing Masked Language Modeling
)

# Initialize GPT-2 model
model = GPT2LMHeadModel.from_pretrained(model_name, pad_token_id=tokenizer.pad_token_id)

# Define training arguments
training_args = TrainingArguments(
    per_device_train_batch_size=4,
    num_train_epochs=3,
    logging_dir='./logs',
    logging_steps=1000,
    save_steps=1000,
    output_dir='./output',
    overwrite_output_dir=True,
    evaluation_strategy="epoch"
)

# Trainer for training the model
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=train_dataset,  # Use the same dataset for evaluation for simplicity (can be different if needed)
    data_collator=data_collator,
)

# Fine-tune the model
trainer.train()

# Save the fine-tuned model
model.save_pretrained('./fine_tuned_model')
tokenizer.save_pretrained('./fine_tuned_model')

print("Fine-tuning and saving completed successfully!")
