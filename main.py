from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(500, 400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[index])
    turtle.penup()
    turtle.goto(x=-230, y=y_pos[index])
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turt in all_turtles:
        if turt.xcor() > 230:
            is_race_on = False
            winning = turt.pencolor()
            if winning == user_bet:
                print(f"You've won! The {winning} turtle is the winner!")
            else:
                print(print(f"You've lost! The {winning} turtle is the winner!"))

        distanc = random.randint(0, 10)
        turt.forward(distanc)





screen.exitonclick()