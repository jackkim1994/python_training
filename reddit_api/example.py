from reddytics.client import RedditClient
from reddytics.analyzer import summarize_posts

def main():
    subreddit_name = "DataScience"  # Note: subreddit names have no spaces
    print(f"Fetching top 10 posts from r/{subreddit_name}...")

    client = RedditClient()
    posts = client.get_top_posts(subreddit_name, limit=10)

    if not posts:
        print(f"No posts found in r/{subreddit_name}.")
        return

    summary = summarize_posts(posts)

    print("\n--- Reddit Analytics Summary ---")
    print(f"Subreddit: r/{subreddit_name}")
    print(f"Total posts fetched: {summary['total_posts']}")
    print(f"Average upvotes per post: {summary['avg_upvotes']:.2f}")
    print(f"Average comments per post: {summary['avg_comments']:.2f}")

    print("\nSample post titles:")
    for i, post in enumerate(posts[:5], start=1):
        print(f"{i}. {post.title} (Score: {post.score}, Comments: {post.num_comments})")

if __name__ == "__main__":
    main()
