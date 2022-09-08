import turtle
from random import randint

turtle.colormode(255)


gay = turtle.Turtle()


gay.shape("arrow")


turtle.bgcolor("black")

gay.speed(10000)

def draw_spiral(starting_radius, loops):
    for i in range(0, loops):
        gay.pencolor(randint(0,255),randint(0,255),randint(0,255))
        gay.circle(starting_radius + i, 60) 

draw_spiral(10, 600)



turtle.done()