from textx import metamodel_from_file

metamodel = metamodel_from_file("turtle.tx")
scene = metamodel.model_from_file("shapes.turtle")

print(scene)

from pprint import pprint

pprint(vars(scene))

import turtle


def draw_shape(shape):
    turtle.pencolor(shape.pencolor.color if shape.pencolor is not None else "black")
    turtle.fillcolor(shape.fillcolor.color if shape.fillcolor is not None else "white")

    turtle.down()
    turtle.begin_fill()

    for line in shape.lines:
        draw_line(line)

    turtle.end_fill()


def draw_line(line):
    bearing = line.direction.bearing

    if bearing == "N":
        turtle.setheading(90)
    elif bearing == "NE":
        turtle.setheading(45)
    elif bearing == "E":
        turtle.setheading(0)
    elif bearing == "SE":
        turtle.setheading(-45)
    elif bearing == "S":
        turtle.setheading(-90)
    elif bearing == "SW":
        turtle.setheading(-135)
    elif bearing == "W":
        turtle.setheading(-180)
    elif bearing == "NW":
        turtle.setheading(-225)
    else:
        turtle.left(line.direction.angle.degrees)

    turtle.forward(line.length)


for draw in scene.draws:
    turtle.up()
    turtle.goto(
        draw.position.x if draw.position is not None else 0,
        draw.position.y if draw.position is not None else 0,
    )
    draw_shape(draw.shape)

turtle.hideturtle()
turtle.done()
