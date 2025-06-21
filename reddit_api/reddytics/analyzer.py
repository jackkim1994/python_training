def summarize_posts(posts):
    return {
        "total_posts": len(posts),
        "avg_upvotes": sum(p.score for p in posts) / len(posts) if posts else 0,
        "avg_comments": sum(p.num_comments for p in posts) / len(posts) if posts else 0,
    }
