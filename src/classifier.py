from transformers import BertForSequenceClassification, BertTokenizer
import torch

# Load the trained model (or untrained)

model = BertForSequenceClassification.from_pretrained('../saved_model')

# Load the tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Preprocess the new data
text = "my house was built in the 90’s and it still has the original A/C unit but it finally gave out last week. It is a dual system and the heat still works but it is time for a full replacement. Looking for a middle of the road system that will not break the bank and for a team that will get the job done right!"

inputs = tokenizer(text, truncation=True, padding=True, max_length=128, return_tensors="pt")

# Make predictions
with torch.no_grad():
    outputs = model(**inputs)

# Post-process the predictions
predictions = torch.sigmoid(outputs.logits)
print(predictions)