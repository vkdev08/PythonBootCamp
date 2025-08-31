import turtle
import pandas
screen = turtle.Screen()
screen.title("US-States-Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_cor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()
turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()
score = 0
game_on = True
guessed_states = []
data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()
while len(guessed_states)<50:
    user_input = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name ?").title()
    state_data = data[data.state == user_input]
    if user_input == "Exit":
        break
    if state_data.state.iloc[0] == user_input and user_input not in guessed_states:
        # print(state_data.state)
        pos = (int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        turtle.goto(pos)
        turtle.write(state_data.state.iloc[0])
        guessed_states.append(user_input)
    else:
        game_on = False
missed_states = []
for state in all_states:
    if state not in guessed_states:
        missed_states.append(state)
new_data = pandas.DataFrame(missed_states)
new_data.to_csv("missed_states.csv")


screen.exitonclick()