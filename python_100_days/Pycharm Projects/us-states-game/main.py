import pandas
import turtle

screen = turtle.Screen()
screen.setup(width=720, height=500, startx=900, starty=250)
screen.title("US State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

drawer = turtle.Turtle()
drawer.penup()
drawer.pencolor("black")
drawer.hideturtle()

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    state = (screen.textinput(title=f"Guess the State ({len(guessed_states)}/50)", prompt="What's another state's name?")
             .lower().capitalize().strip())

    if state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break

    if state in states_list and state not in guessed_states:
        guessed_states.append(state)
        state_row = data[data.state == state]
        state_x = state_row["x"].item()
        state_y = state_row["y"].item()

        drawer.goto((state_x, state_y))
        drawer.write(state)
