import os

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import desc
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
MOVIE_API_KEY = os.getenv("MOVIE_API_KEY")
MOVIE_API = "https://api.themoviedb.org/3/search/movie"
MOVIE_DETAIL_API = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie_collection.db"
Bootstrap5(app)
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer)
    description = db.Column(db.String())
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String())
    img_url = db.Column(db.String())


with app.app_context():
    db.create_all()


class EditMovieForm(FlaskForm):
    edit_rating = DecimalField('Your rating out of 10, e.g 7.5', validators=[DataRequired()])
    edit_review = StringField('Your review', validators=[DataRequired()])
    submit = SubmitField('Done')


class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(desc(Movie.rating)).limit(10))
    all_movies = result.scalars()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def update():
    form = EditMovieForm()
    movie_id = request.args.get('id')
    movie_to_update = db.get_or_404(Movie, movie_id)

    if form.validate_on_submit():
        try:
            movie_to_update.rating = float(form.edit_rating.data)
            movie_to_update.review = form.edit_review.data
            db.session.commit()
        except Exception as e:
            print(e)
        return redirect(url_for('home'))

    return render_template("edit.html", movie=movie_to_update, form=form)


@app.route("/delete", methods=["GET", "POST"])
def delete_movie():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)

    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        query = form.title.data
        return redirect(url_for('select_movie', query=query))
    return render_template("add.html", form=form)


@app.route("/select", methods=["GET", "POST"])
def select_movie():
    search_query = request.args.get('query')
    query_param = {
        "query": search_query,
        "api_key": MOVIE_API_KEY,
        "include_adult": "false",
        "language": "en - US"
    }
    response = requests.get(MOVIE_API, params=query_param)
    result = response.json()["results"]
    return render_template("select.html", movie_list=result)


@app.route("/save")
def save_movie():
    movie_id = request.args.get('id')
    query_param = {
        "api_key": MOVIE_API_KEY,
        "language": "en - US"
    }
    if movie_id:
        selected_movie_detail = requests.get(f"{MOVIE_DETAIL_API}/{movie_id}", params=query_param).json()
        print(selected_movie_detail)
        movie = Movie(
            title=selected_movie_detail["title"],
            img_url=f"{MOVIE_DB_IMAGE_URL}{selected_movie_detail['poster_path']}",
            year=selected_movie_detail["release_date"].split("-")[0],
            description=selected_movie_detail["overview"]
        )
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('update', id=movie.id))


## After adding the new_movie the code needs to be commented out/deleted.
## So you are not trying to add the same movie twice.
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
