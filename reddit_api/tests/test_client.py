from reddytics.client import RedditClient

def test_get_top_posts():
    client = RedditClient()
    posts = client.get_top_posts("python", limit=5)
    assert len(posts) == 5
    assert hasattr(posts[0], "title")
