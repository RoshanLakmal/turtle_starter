import turtle as t
import random

t.colormode(255)
turtle_start = t.Turtle()

turtle_start.shape("turtle")
turtle_start.speed("fastest")

#spirograph
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ran_color = (r,g,b)
    return ran_color

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        turtle_start.color(random_color())
        turtle_start.circle(100)
        turtle_start.setheading(turtle_start.heading() + size_of_gap)

draw_spirograph(5)
# for degree in range(1,361):
#     turtle_start.color(random_color())
#     turtle_start.circle(100)
#     turtle_start.setheading(degree)

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     ran_color = (r,g,b)
#     return ran_color
#
# directions = [0,90,180,270]
# turtle_start.pensize(15)
# turtle_start.speed("fastest")
# for _ in range(200):
#     turtle_start.color(random_color())
#     turtle_start.forward(100)
#     turtle_start.setheading(random.choice(directions))

#walk
# color_list = ["red", "blue", "green", "pink", "black", "orange", "gold", "yellow"]
# directions = [0,90,180,270]
# turtle_start.pensize(15)
# turtle_start.speed("fastest")
# for _ in range(200):
#     turtle_start.color(random.choice(color_list))
#     turtle_start.forward(100)
#     turtle_start.setheading(random.choice(directions))
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
