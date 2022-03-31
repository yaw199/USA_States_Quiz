from operator import is_
from turtle import Turtle, Screen
import pandas as pd
import os

os.system("cls")


my_tut = Turtle()
my_tut.hideturtle()
my_screen = Screen()
my_screen.title("U.S States Quiz")

#my_screen.bgcolor("cyan")
my_screen.bgpic("./blank_states_img.gif")

#my_tut.shape("./blank_states_img.gif")

# Getting coordinates from the map

# def on_screen_cod(x,y):

#     print(x,y)

# my_screen.onscreenclick(on_screen_cod)

is_running = []

while len(is_running) < 50:
    state_name = my_screen.textinput(title=f"{len(is_running)}/50 States", prompt="Enter State Name").title()


    #Read Pandas

    states_file = pd.read_csv("./50_states.csv")
    state_series = pd.Series(states_file["state"]).array
    # Check if state_name in states_file

    if state_name in state_series and state_name not in is_running:
        is_running.append(state_name)
        state_data = states_file[states_file.state == state_name]
        my_tut.hideturtle()
        my_tut.penup()
        my_tut.goto(int(state_data.x),int(state_data.y))
        my_tut.write(f"{state_data.state.item()}")
    # Exit 

    if state_name == "Exit":
        
        miss_state = []
        for each_state in state_series:
            if each_state not in is_running:
                miss_state.append(each_state)
        miss_data = pd.DataFrame(miss_state)
        miss_data.to_csv("States_missed.csv")    
        break

print(miss_state)



#my_screen.mainloop()
