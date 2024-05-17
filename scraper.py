import praw

reddit = praw.Reddit(
    client_id='6QfzZm6XRYDKE7Kj_An9EA',
    client_secret='jAkuGVm4uL0XDM6LKrEoAvz2oqTnKA',
    user_agent='my_reddit_scraper/0.1 by hderyke59'
)

# Define the subreddit and number of posts to fetch
subreddit_name = 'indianapolis'
number_of_posts = 20

# Fetch posts from the subreddit
subreddit = reddit.subreddit(subreddit_name)
posts = subreddit.hot(limit=number_of_posts)

# Print the title and URL of each post
for post in posts:
    print(f'Title: {post.title}, URL: {post.url}')
    print(f'body: {post.selftext}, URL: {post.url}')
