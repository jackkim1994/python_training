# Reddit API Client
import os
import praw
from dotenv import load_dotenv

load_dotenv()

class RedditClient:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=os.getenv("REDDIT_USER_AGENT"),
        )

    def get_subreddit(self, name):
        return self.reddit.subreddit(name)

    def get_top_posts(self, subreddit, limit=10):
        return [post for post in self.get_subreddit(subreddit).top(limit=limit)]
