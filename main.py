# This program is a code rapresentation of the "Flumequine" Hirts painting
from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

t = Turtle()
t.hideturtle()
t.penup()
t.speed("fastest")

# Configuration of the x and y axes, to set the initial position of the turtle
x = -235
y = -275
t.setposition(x,y)

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

def draw_line():
    """ This function draw a line of dots """
    dots = 10
    dot_distance = 50
    for i in range(dots):
        random_color = random.choice(color_list)
        t.pendown()
        t.dot(20, random_color)
        t.penup()
        t.forward(dot_distance)

#running the while loop until all lines of dots are drawn
lines_counter = 0
while lines_counter < 12:
    lines_counter += 1
    draw_line()
    y += 50
    t.setposition(x,y)

screen.exitonclick()