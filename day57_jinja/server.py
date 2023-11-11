import random
import datetime as dt
import requests

from flask import Flask, render_template

app = Flask(__name__)

URL_AGE = "https://api.agify.io"
URL_GENDER = "https://api.genderize.io"


@app.route('/')
def hello_world():
    random_number = random.randint(1, 10)
    time = dt.date.today().year

    return render_template("index.html", num=random_number, year=time)


@app.route('/guess/<name>')
def guess(name):
    params = {
        "name": name
    }
    time = dt.date.today().year
    age_response = requests.get(URL_AGE, params=params).json()
    gender_response = requests.get(URL_GENDER, params=params).json()
    return render_template(
        "guess_front.html",
        name=name.capitalize(),
        age=age_response["age"],
        gender=gender_response["gender"],
        year=time
    )

'''
Examle of jinja multi format
'''
@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()

    return render_template("blog.html", posts=all_posts)


@app.route('/blog/<num>')
def get_blog_num(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()

    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
