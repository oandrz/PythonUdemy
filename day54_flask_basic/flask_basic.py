from flask import Flask

def make_bold(function):
    def wrapper_function():
        return f'<b>{function()}</b>'

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f'<em>{function()}</em>'

    return wrapper_function

def make_underline(function):
    def wrapper_function():
        return f'<u>{function()}</u>'

    return wrapper_function

# __name__ is a special variable that gets the name of the file that is running
app = Flask(__name__)

'''
How to use html in flask
'''
@app.route('/')
def hello_world():
    return """
        <h1 style="text-align: center">Hello, World!</h1>
        <p> This is a paragraph</p>
        <img src="https://d16kd6gzalkogb.cloudfront.net/magazine_images/Jaebum-Joo.jpg" width=500>
    """

@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def bye():
    return 'Hello, Bye!'

# Path param
@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

# @app.route('/greet/<name>/dorayaki')
# def greet_second(name):
#     return f'Hello, {name}!'

# Path param with data type get a param as a string without a /
# Example http://local./greet/Andreas/25
# resulting in name = Andreas/25
@app.route('/greet/<path:name>/dorayaki')
def greet_second(name):
    return f'Hello, {name}!'

@app.route('/greet/<name>/<int:age>')
def greet_aage(name, age):
    return f'Hello, {name} is {age}!'

if __name__ == "__main__":
    # equal to flask run in terminal
    # Debug mode will automatically reload server when there's a change in the code, so no need to run everytime there's a changes
    app.run(debug=True)
