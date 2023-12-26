import turtle
import pandas
from Scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = turtle.Screen()
screen.setup(725, 491)
screen.title('U.S. States Game')
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
is_game_on = True

while len(scoreboard.correct_guessed) < 50 and is_game_on:
    answer_table = screen.textinput(title=f'{scoreboard.guessed}/50 Stated correct',
                                    prompt="what's another state's name?")
    answer = answer_table.title()
    states = data.state.to_list()
    for state in range(len(states)):

        if answer == "Exit":
            missing_state = [given_state for given_state in states if given_state not in scoreboard.correct_guessed]
            new_csv = pandas.DataFrame(missing_state)
            new_csv.to_csv('states_to_learn.csv')
            is_game_on = False
        elif answer == states[state] and answer not in scoreboard.correct_guessed:
            x_cor = data.x[data.state == answer][state]
            y_cor = data.y[data.state == answer][state]
            tim = turtle.Turtle()
            tim.shape('circle')
            tim.shapesize(0.3)
            tim.penup()
            tim.goto(x_cor, y_cor)
            tim.write(f'{answer}')
            scoreboard.add_guessed(answer)
