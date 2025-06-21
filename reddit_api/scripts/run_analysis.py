from reddytics.client import RedditClient
from reddytics.analyzer import summarize_posts

client = RedditClient()
posts = client.get_top_posts("python", limit=10)
summary = summarize_posts(posts)

print("Subreddit Analytics:")
print(summary)