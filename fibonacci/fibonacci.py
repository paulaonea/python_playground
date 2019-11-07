import turtle
import random


def square(side_length):
    colour = "#" + "{:06x}".format(random.randrange(0, 0xffffff))
    turtle.color(colour)
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)
    turtle.circle(side_length, 90)


side_length = 1
previous_side = 1
n = int(input('How many squared do you want to draw (maximum 14)?'))

square(side_length)

for i in range(1, n, 1):
    square(side_length)
    side_length, previous_side = (side_length + previous_side, side_length)

turtle.done()
