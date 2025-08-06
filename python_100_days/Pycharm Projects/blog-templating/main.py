import requests
from flask import Flask, render_template
from post import Post

app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
json_posts = response.json()
posts = [Post(json_posts[i]["title"], json_posts[i]["subtitle"], json_posts[i]["body"], i) for i in range(len(json_posts))]

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/post/<int:post_id>')
def render_post(post_id):
    post = None
    for p in posts:
        if p.post_id == post_id:
            post = p
            break

    if not post:
        return f"There's no post with id {post_id}!"

    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
