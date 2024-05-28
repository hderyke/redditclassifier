import csv
import praw

#scrape posts from a reddit page and manually label them, add data to csv file

# Define the subreddit and number of posts to fetch
subreddit_names = ['nyc','houston']
keywords = ['sports','rec sports','make friends','meet people','club sports','things to do']
number_of_posts = 3000

def fetch_posts(reddit, subreddits, limit, keywords=None,):
    all_posts = []

    if keywords:
        for subreddit_name in subreddits:
            subreddit = reddit.subreddit(subreddit_name)
            for post in subreddit.new(limit=limit):
                if any(keyword.lower() in post.title.lower() or keyword.lower() in post.selftext.lower() for keyword in
                       keywords):
                    all_posts.append(post)
    else:
        for subreddit_name in subreddits:
            subreddit = reddit.subreddit(subreddit_name)
            for post in subreddit.new(limit=limit):
                all_posts.append(post)

    return all_posts


# Initialize the Reddit client
reddit = praw.Reddit(
    client_id='6QfzZm6XRYDKE7Kj_An9EA',
    client_secret='jAkuGVm4uL0XDM6LKrEoAvz2oqTnKA',
    user_agent='my_reddit_scraper/0.1 by hderyke59'
)

# Fetch posts from the subreddit
posts = fetch_posts(reddit, subreddit_names, number_of_posts,keywords)

# Open the CSV file for writing
with open('../data/posts.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['Title', 'Body', 'URL', 'Label'])

    # Write the data for each post
    for post in posts:
        # Clear the terminal screen (cross-platform)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        # Display the post title and body for labeling
        print(f"TITLE: {post.title}\n")
        print(f"BODY: {post.selftext}\n")

        # Prompt for labeler to label each post
        label = -1
        while label != '1' and label != '0':
            label = input("Enter label (1 for target intent, 0 for other): ")


        # Replace commas in text to prevent CSV format issues
        title = post.title.replace(",", "|")
        body = post.selftext.replace(",", "|")

        # Write the labeled data to the CSV file
        writer.writerow([title, body, post.url, label])
