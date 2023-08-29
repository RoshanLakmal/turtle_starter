from turtle import Turtle, Screen
import random

turtle_start = Turtle()
turtle_start.shape("turtle")

color_list = ["red", "blue", "green", "pink", "black", "orange", "gold", "yellow"]
FULL_DEGREES = 360
def draw_shape(side):
    for _ in range(side):
        turtle_start.forward(100)
        turtle_start.right(FULL_DEGREES/side)

for shape_side in range(3,11):
    turtle_start.color(random.choice(color_list))
    draw_shape(shape_side)
# Dash
# for _ in range(50):
#     turtle_start.forward(10)
#     turtle_start.penup()
#     turtle_start.forward(10)
#     turtle_start.pendown()

# Squre
# for _ in range(4):
#     turtle_start.forward(100)
#     turtle_start.right(90)

# turtle_start.forward(100)
# turtle_start.right(90)
# turtle_start.forward(100)
# turtle_start.right(90)
# turtle_start.forward(100)
# turtle_start.right(90)
# turtle_start.forward(100)


screen = Screen()
screen.exitonclick()
