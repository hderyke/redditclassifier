import pandas as pd
from sklearn.model_selection import train_test_split
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
import torch
import numpy as np

# Load your dataset
df = pd.read_csv('../data/posts.csv')

# Exclude rows where the 'Label' column is equal to 'Label'
df = df[df['Label'] != 'Label']

# Convert the 'Label' column to integer type
df['label'] = df['Label'].astype(int)

# Combine title and body for the text feature
df['text'] = df['Title'] + " " + df['Body']

# Check unique values in 'Label' column
print("Unique values in 'Label' column before mapping:")
print(df['Label'].unique())

# Ensure 'Label' column contains integers
df['label'] = df['Label'].astype(int)

# Check for any NaN values in the 'label' column
print("Any NaN values in 'label' column after mapping:")
print(df['label'].isna().sum())

# Display value counts for the 'label' column
print("Label value counts:")
print(df['label'].value_counts())

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Load pre-trained BERT tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Tokenize the data
train_encodings = tokenizer(list(map(str, X_train.tolist())), truncation=True, padding=True, max_length=128)
test_encodings = tokenizer(list(map(str, X_test.tolist())), truncation=True, padding=True, max_length=128)

# Create torch datasets
class RedditDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

train_dataset = RedditDataset(train_encodings, y_train.tolist())
test_dataset = RedditDataset(test_encodings, y_test.tolist())

# Load pre-trained BERT model for sequence classification
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

# Define training arguments
training_args = TrainingArguments(
    output_dir='../out',
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='../logs',
    logging_steps=10,
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset
)

# Train the model
trainer.train()
print("Training complete.")

# Evaluate the model
print(trainer.evaluate())

# Save the model and tokenizer for future use
model.save_pretrained('../saved_model')
tokenizer.save_pretrained('../saved_model')
