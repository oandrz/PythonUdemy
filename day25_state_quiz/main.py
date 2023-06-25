import turtle
import pandas
from answer_turtle import AnswerTurtle

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "./data/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer = AnswerTurtle()

states_data = pandas.read_csv("./data/50_states.csv")
states_list = states_data.state.to_list()
states_count = len(states_list)
guessed_states = []

while len(guessed_states) < states_count:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/{states_count} States Correct",
        prompt="What's another state's name ?"
    )

    if answer_state is None:
        break
    elif answer_state.title() in states_list:
        guessed_states.append(answer_state.title())
        guess = states_data[states_data.state == answer_state.title()]
        answer.showAnswer(guess)

# Check not in given array
missing_state = states_data[~states_data["state"].isin(guessed_states)]["state"]
missing_state.to_csv("./data/learn.csv")
