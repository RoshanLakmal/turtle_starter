from turtle import Turtle, Screen
turtle_start = Turtle()
turtle_start.shape("turtle")
turtle_start.color("red")

# Dash
for _ in range(50):
    turtle_start.forward(10)
    turtle_start.penup()
    turtle_start.forward(10)
    turtle_start.pendown()

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