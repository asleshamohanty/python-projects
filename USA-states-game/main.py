import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(800,600)


data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

game_is_on = True
correct_guesses = 0
guessed_states = []

while game_is_on:
    title = f"{correct_guesses}/50 guessed!"
    answer_state = screen.textinput(title=title, prompt="What's another state name: ").title()
    if answer_state in states_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        xcor = (data.at[states_list.index(answer_state), "x"])
        ycor = (data.at[states_list.index(answer_state), "y"])
        state_name = (data.at[states_list.index(answer_state), "state"])
        t.goto(xcor, ycor)
        t.write(state_name)
        correct_guesses += 1
        guessed_states.append(answer_state)
    elif answer_state == "Exit":
        break

#States miss out - to learn
print(guessed_states)
for state in guessed_states:
    if state in states_list:
        states_list.remove(state)

missed_states_dict = {
    "states": states_list
}

df = pandas.DataFrame(missed_states_dict)
df.to_csv("States_to_learn.csv")


