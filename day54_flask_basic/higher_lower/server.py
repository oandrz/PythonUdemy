import random

from flask import Flask

app = Flask(__name__)
generated_number = random.randint(0, 9)


@app.route('/')
def hello_world():
    return '''
        <h1> Guess a number between 0 and 9 </h1>
        <image src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">
    '''


@app.route('/<int:number>')
def guess(number):
    if number > generated_number:
        return '''
        <h1 style="color: purple">Too high, try again!</h1>
        <image src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">
    '''
    elif number < generated_number:
        return '''
        <h1 style="color: red">Too low, try again!</h1>
        <image src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">
        '''
    else:
        return '''
                <h1 style="color: green">You found me!</h1>
                <image src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">
        '''


if __name__ == "__main__":
    # equal to flask run in terminal
    # Debug mode will automatically reload server when there's a change in the code, so no need to run everytime there's a changes
    app.run(debug=True)
