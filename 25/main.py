import turtle

import pandas
from turtle import Turtle, Screen

screen = Screen()
screen.title("US STATES GUESSING GAME")
image = "blank_states_img.gif"
screen.bgpic(image)

data = pandas.read_csv("50_states.csv")
list_of_states = data["state"].values.tolist()
xcors_list = data["x"].values.tolist()
ycors_list = data["y"].values.tolist()


nb_of_states = len(list_of_states)
states_not_guessed =[]
guessed_states = []

while nb_of_states != 0:
    state_named = screen.textinput(title="Guess the state. Type 'Exit' to exit", prompt="Name a state: ")
    if state_named == "Exit":
        for state in list_of_states:
             if state not in guessed_states:
                states_not_guessed.append(state)
        new_data = pandas.DataFrame(states_not_guessed)
        new_data.to_csv("states_not_guessed.csv")
        break
    if state_named in list_of_states :
        index = list_of_states.index(state_named)
        xcor = xcors_list[index]
        ycor = ycors_list[index]
        t = turtle.Turtle()
        t.penup()
        t.goto(xcor, ycor)
        t.write(state_named)
        guessed_states.append(state_named)
        nb_of_states -= 1



