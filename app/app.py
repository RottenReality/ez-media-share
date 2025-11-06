from fastapi import FastAPI, HTTPException
from app.schemas import PostResponse


app = FastAPI()

text_posts = {
    1: {"title": "New Post", "content": "cool test post"},
    2: {"title": "Testing Setup", "content": "Just verifying the basic installation works as expected."},
    3: {"title": "Performance Check", "content": "A slightly longer piece of content to test longer strings in the database storage."},
    4: {"title": "Feature X Integration", "content": "This post is about a potential new feature being prototyped."},
    5: {"title": "Database Connect", "content": "Confirming SQLAlchemy connection is active and running."},
    6: {"title": "A Quick Note", "content": "Short message for quick POST/GET validation."},
    7: {"title": "Deployment Prep", "content": "Preparing the service for initial deployment readiness checks."},
    8: {"title": "Schema Validation", "content": "Testing different title/content lengths to ensure Pydantic schemas hold up."},
    9: {"title": "Concurrency Test", "content": "Simulating concurrent requests to see how the API handles load."},
    10: {"title": "Final Test Post", "content": "This should be the last one required for initial endpoint verification."}
}

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit and limit < len(text_posts):
        return list(text_posts.values())[:limit]
    return text_posts

@app.post("/posts/{id}")
def get_post(id: int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostResponse) -> PostResponse:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post