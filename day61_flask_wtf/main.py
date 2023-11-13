from flask import Flask, render_template
from flask_bootstrap import Bootstrap4, Bootstrap5

from day61_flask_wtf.LoginForm import LoginForm

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
WTF_CSRF_SECRET_KEY = 'a random string'

app = Flask(__name__)
app.secret_key = WTF_CSRF_SECRET_KEY

bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # return boolean, true -> validation success else false
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email == "admin@email.com" and password == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
