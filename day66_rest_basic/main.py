import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def as_dictionary(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)

    # another method of serialising our database row Object to JSON is by first
    # converting it to a dictionary
    return jsonify(
        name=random_cafe.name,
        can_take_calls=random_cafe.can_take_calls,
        has_sockets=random_cafe.has_sockets,
        has_toilet=random_cafe.has_toilet,
        has_wifi=random_cafe.has_wifi,
        id=random_cafe.id,
        img_url=random_cafe.img_url,
        location=random_cafe.location,
        map_url=random_cafe.map_url,
        seats=random_cafe.seats,
    )


@app.route("/all")
def get_all_cafe():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    response = jsonify(cafes=[cafe.as_dictionary() for cafe in all_cafes])
    return response


@app.route("/search")
def search_cafe():
    query_location = request.args.get('loc')
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    all_cafes = result.scalars().all()

    if len(all_cafes) == 0:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})

    response = jsonify(cafes=[cafe.as_dictionary() for cafe in all_cafes])
    return response


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=request.form.get("has_toilet").lower() == "true",
        has_wifi=request.form.get("has_wifi").lower() == "true",
        has_sockets=request.form.get("has_sockets").lower() == "true",
        can_take_calls=request.form.get("can_take_calls").lower() == "true",
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>")
def update_price(cafe_id):
    new_price = request.args.get('new_price')
    cafe_to_update = db.get_or_404(Cafe, cafe_id)
    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>")
def remove_cafe(cafe_id):
    api_key = request.args.get('api_key')
    if api_key != "TopSecretAPIKey":
        return jsonify(error={"Not Found": "Sorry that's not allowed. Make sure you have the correct api_key"}), 404

    cafe_to_delete = db.get_or_404(Cafe, cafe_id)
    if cafe_to_delete:
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return jsonify(response={"success": "Successfully closed the cafe, thank you for the report."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


if __name__ == '__main__':
    app.run(debug=True)
