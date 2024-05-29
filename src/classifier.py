import datetime
from datetime import datetime, timedelta
import sys

import praw
from transformers import BertForSequenceClassification, BertTokenizer
import torch

#classifier. Usage: python classifier.py {subreddit name} {n/o days to scan}

def fetch_posts(subreddit_name,days): #get posts given subreddit name and no days
    print("Scanning the "+subreddit_name+" subreddit from the last "+days+" days")

    reddit = praw.Reddit(
        client_id='6QfzZm6XRYDKE7Kj_An9EA',
        client_secret='jAkuGVm4uL0XDM6LKrEoAvz2oqTnKA',
        user_agent='my_reddit_scraper/0.1 by hderyke59'
    )

    all_posts = []

    # Calculate the timestamp for the start of the desired time period
    end_time = datetime.now()
    days = int(days)
    start_time = end_time - timedelta(days=days)

    # Access the subreddit
    subreddit = reddit.subreddit(subreddit_name)

    # Fetch posts using the 'search' method with the 'timestamp' filter
    for post in subreddit.new(limit=1000):
        post_created_time = datetime.fromtimestamp(post.created_utc)
        if start_time <= post_created_time <= end_time:
            combined_text = f"{post.title} {post.selftext}"
            all_posts.append(combined_text)

    return all_posts


num_args = len(sys.argv)
if num_args == 3:
    prompts = fetch_posts(sys.argv[1],sys.argv[-1])
else:
    print("Usage: reddit_scan {subreddit name} {n/o days to scan}")
    exit(0)

# Load the trained model (or untrained)
model = BertForSequenceClassification.from_pretrained('../saved_model')
# Load the tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')


# Preprocess the new data
# test prompts
for text in prompts:
    inputs = tokenizer(text, truncation=True, padding=True, max_length=128, return_tensors="pt")

    # Make predictions
    with torch.no_grad():
        outputs = model(**inputs)

    # Post-process the predictions
    predictions = torch.sigmoid(outputs.logits)
    #print(predictions)
    pred_0_first = predictions[0][0].item()
    pred_last_second = predictions[-1][1].item()

    # safely compare these values
    if pred_0_first > pred_last_second:
        continue
    else:
        print(text)
