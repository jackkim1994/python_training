from reddytics.analyzer import summarize_posts

class DummyPost:
    def __init__(self, score, comments):
        self.score = score
        self.num_comments = comments

def test_summarize_posts():
    posts = [DummyPost(10, 5), DummyPost(20, 10)]
    summary = summarize_posts(posts)
    assert summary["total_posts"] == 2
    assert summary["avg_upvotes"] == 15
    assert summary["avg_comments"] == 7.5
