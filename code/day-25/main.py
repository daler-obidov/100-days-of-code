

import turtle
import pandas


screen = turtle.Screen()
screen.title("Uzbekistan Cities Game")
image = "/home/daler/code/100-days-of-code/code/day-25/uz_cities.gif"
turtle.addshape(image)
turtle.shape(image)


# def get_mouse_click(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()

data = pandas.read_csv("/home/daler/code/100-days-of-code/code/day-25/12_cities.csv")
all_states = data.state.to_list()
guessed = []


def write_state(state_name, x, y):
    turtle_obj = turtle.Turtle()
    turtle_obj.hideturtle()
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.write(state_name)


while len(guessed) < 12:
    answer = screen.textinput(title=f"{len(guessed)}/12 Cities correct!", prompt="What's another city's name?").title()

    if answer == "Exit":
        # Save the states that were correctly guessed
        missed_states = [state for state in all_states if state not in guessed]
        missed_states_df = pandas.DataFrame(missed_states, columns=["State"])
        missed_states_df.to_csv("/home/daler/code/100-days-of-code/code/day-25/missed_states.csv")
        break

    if answer in all_states and answer not in guessed:
        guessed.append(answer)
        state_data = data[data.state == answer]
        x, y = state_data.x.item(), state_data.y.item()
        write_state(answer, x, y)
    else:
        screen.textinput(title="Error", prompt="Region not found or already guessed. Try again.")


