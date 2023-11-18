from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

all_books = []


# the primary key fields is optional. you can also write:
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    review = db.Column(db.Float)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # When we execute a query during a database session we get back the rows in the database (a Result object).
    # We then use scalars() to get the individual elements rather than entire rows.
    books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
    return render_template("index.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book = Book(
            title=request.form["book_name"],
            author=request.form["book_author"],
            review=request.form["rating"]
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit_rating.html", book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = db.get_or_404(Book, book_id)
    # Alternative way to select the book to delete.
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True, port=5000)

# how to connect sqlite in vanilla sqlite
# db = sqlite3.connect("books-collection.db")

# cursor object to navigate table in vanilla sqlite
# cursor = db.cursor()
# This method will tell the cursor to execute an action. All actions in SQLite databases are expressed as SQL (Structured Query Language) commands
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
