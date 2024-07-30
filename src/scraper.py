import csv
import os
import time

import praw

#scrape posts from a reddit page and manually label them, add data to csv file

# Define the subreddit and number of posts to fetch
subreddit_names = [] 
keywords = []
number_of_posts = 5000

def fetch_posts(reddit, subreddits, limit=10000, keywords=None):
    all_posts = []

    if keywords:
        for subreddit_name in subreddits:
            subreddit = reddit.subreddit(subreddit_name)
            print(f"Fetching new posts from subreddit: {subreddit_name}")
            try:
                for post in subreddit.new(limit=limit):
                    # Check if any keyword is in the post title or selftext
                    if any(keyword.lower() in post.title.lower() or keyword.lower() in post.selftext.lower() for keyword
                           in keywords):
                        all_posts.append(post)
                        if len(all_posts) >= limit:
                            break
            except Exception as e:
                print(f"An error occurred: {e}")
            time.sleep(2)  # Delay to avoid hitting rate limits
    else:
        for subreddit_name in subreddits:
            subreddit = reddit.subreddit(subreddit_name)
            for post in subreddit.new(limit=number_of_posts):
                print(f"Found post: {post.title}")
                all_posts.append(post)

    return all_posts



# Initialize the Reddit client
reddit = praw.Reddit(
    client_id='',
    client_secret='', ##ENTER YOUR API CREDENTIALS
    user_agent=''
)

# Fetch posts from the subreddit
posts = fetch_posts(reddit, subreddit_names, number_of_posts,keywords)

csv_exist = 1 #check if first entry to posts csv
if os.path.exists('../data/posts.csv'):
    csv_exist = 0

# Open the CSV file for writing
with open('../data/posts.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    if csv_exist == 0:
        writer.writerow(['Title', 'Body', 'URL', 'Label'])

    # Write the data for each post
    for post in posts:
        # Clear the terminal screen (cross-platform solution)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        # Display the post title and body for labeling
        print(f"TITLE: {post.title}\n")
        print(f"BODY: {post.selftext}\n")

        # Prompt for labeler to label each post
        label = -1
        while label != '1' and label != '0' and label != 's':
            label = input("Enter label (1 for target intent, 0 for other) or 's' to skip: ")
        if label == 's':
            continue


        # Replace commas in text to prevent CSV format issues
        title = post.title.replace(",", "|")
        body = post.selftext.replace(",", "|")

        # Write the labeled data to the CSV file
        writer.writerow([title, body, post.url, label])
