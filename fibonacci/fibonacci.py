import turtle

colours = ['red', 'green', 'blue', 'purple', 'grey', 'black']

def shape(side_length, colour, angle=90):
    turtle.color(colour)
    for i in range(4):
        if i == 3:
            turtle.right(angle)
        turtle.forward(side_length)
        turtle.right(angle)


side_length = 1
previous_side = 1

turtle.forward(side_length)
turtle.right(90)
n = 14

for i in range(1, n, 1):
    colour = colours[i % len(colours)]
    shape(side_length, colour)
    side_length, previous_side = (side_length + previous_side, side_length)

turtle.done()