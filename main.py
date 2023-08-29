from turtle import Turtle, Screen
import random

turtle_start = Turtle()
turtle_start.shape("turtle")

#walk
color_list = ["red", "blue", "green", "pink", "black", "orange", "gold", "yellow"]
directions = [0,90,180,270]
turtle_start.pensize(15)
turtle_start.speed("fastest")
for _ in range(200):
    turtle_start.color(random.choice(color_list))
    turtle_start.forward(100)
    turtle_start.setheading(random.choice(directions))
# for _ in range(200):
#     turtle_start.color(random.choice(color_list))
#     random_number = random.randint(0, 3)
#     if random_number == 0:
#         turtle_start.forward(100)
#     elif random_number == 1:
#         turtle_start.backward(100)
#     elif random_number == 2:
#         turtle_start.right(90)
#     else:
#         turtle_start.left(90)

# Shapes
# color_list = ["red", "blue", "green", "pink", "black", "orange", "gold", "yellow"]
# FULL_DEGREES = 360
# def draw_shape(side):
#     for _ in range(side):
#         turtle_start.forward(100)
#         turtle_start.right(FULL_DEGREES/side)
#
# for shape_side in range(3,11):
#     turtle_start.color(random.choice(color_list))
#     draw_shape(shape_side)

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
