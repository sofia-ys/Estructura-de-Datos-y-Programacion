import turtle
import random as rnd

def ejercicio1():
    # setup
    scr = turtle.Screen()
    scr.setup(600, 400)
    scr.screensize(1000, 800)

    colores = ["white", "black", "red", "blue", "green", "cyan", "magenta",
            "yellow", "pink", "orange"]

    t = turtle.Turtle()
    t.speed(0)

    for i in range(6):
        turtle.setheading(60*i)
        turtle.pencolor(rnd.choice(colores))
        turtle.forward(60)

    scr.exitonclick()

def ejercicio2():
    scr = turtle.Screen()
    scr.setup(600, 400)
    scr.screensize(1000, 800)

    t = turtle.Turtle()
    t.speed(0)

    # circle
    turtle.penup()
    turtle.goto(0,-100)
    turtle.pendown()
    turtle.circle(100)

    # segments
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.setheading(110)
    turtle.forward(100)

    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.setheading(40)
    turtle.forward(100)

    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(100)

    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.setheading(250)
    turtle.forward(100)

    # text
    turtle.penup()
    turtle.goto(-60,0)
    turtle.write("notables")

    turtle.goto(10,50)
    turtle.write("aprobados")

    scr.exitonclick()

def ejercicio3():
    scr = turtle.Screen()
    scr.setup(600, 400)
    scr.screensize(1000, 800)

    t = turtle.Turtle()
    t.speed(0)

    turtle.pencolor("red")
    turtle.fillcolor("yellow")

    turtle.begin_fill()
    for i in range(4):
        turtle.setheading(i*-90)
        turtle.forward(50)
    turtle.end_fill()
    
    scr.exitonclick()

ejercicio3()