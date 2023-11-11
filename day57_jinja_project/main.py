import requests
from post import Post
from flask import Flask, render_template

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
post_list = []
response = requests.get(blog_url)
all_posts = response.json()
for post_response in all_posts:
    post_list.append(
        Post(
            id=post_response["id"],
            title=post_response["title"],
            subtitle=post_response["subtitle"],
            body=post_response["body"],
        )
    )

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=post_list)


@app.route('/blog/<post_id>')
def get_blog_num(post_id):
    selected_post = post_list[int(post_id) - 1]
    return render_template("post.html", post=selected_post)


if __name__ == "__main__":
    app.run(debug=True)
