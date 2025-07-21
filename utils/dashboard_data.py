from collections import Counter

# Sample static data (replace with real query logs if needed)
query_logs = [
    {"query": "How to heal from a breakup?", "language": "English"},
    {"query": "Toxic relationship signs", "language": "English"},
    {"query": "self worth", "language": "English"},
    {"query": "डिप्रेशन से बाहर कैसे निकले", "language": "Hindi"},
    {"query": "emotional abuse", "language": "English"},
    {"query": "How to heal from a breakup?", "language": "English"},
]

# Computes insights for admin dashboard
def get_insights():
    top_queries = Counter([q["query"] for q in query_logs]).most_common(3)
    languages = Counter([q["language"] for q in query_logs])

    return {
        "top_queries": [q for q, _ in top_queries],
        "languages": dict(languages),
        "unanswered": 2  # Placeholder; replace with actual count if logging unanswered queries
    }
