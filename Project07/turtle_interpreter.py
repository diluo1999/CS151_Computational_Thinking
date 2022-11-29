# turtle_interpreter.py
# Di Luo
# CS 151 Fall 2018
# Project 7: Fractals and Trees

import turtle

def drawString( dstring, distance, angle ):
    ''' Interpret the characters in string dstring as a series
    of turtle commands. Distance specifies the distance
    to travel for each forward command. Angle specifies the
    angle (in degrees) for each right or left command. The list of 
    turtle supported turtle commands is:
    F : forward
    - : turn right
    + : turn left
    [ : save position and heading
    ] : restore position and heading
    A : change the color to green
    B : change the color to orange
    C : change the color to black
    D : change the color to saddle brown
    '''

    stack = []
    color = []

    for char in dstring:
        if char == 'F':
            turtle.forward(distance)
        elif char == '-':
            turtle.right(angle)
        elif char == '+':
            turtle.left(angle)
        elif char == '[':
            stack.append(turtle.position())
            stack.append(turtle.heading())
        elif char == ']':
            turtle.penup()
            turtle.setheading(stack.pop())
            turtle.goto(stack.pop())
            turtle.pendown()
        elif char == 'A':
            turtle.color('green')
        elif char == 'B':
            turtle.color('orange')
        elif char == 'C':
            turtle.color('black')
        elif char == 'D':
            turtle.color('saddle brown')


    turtle.update()

def hold():
    '''Holds the screen open until user clicks or presses 'q' key'''

    turtle.hideturtle()
    turtle.update()

    turtle.onkey(turtle.bye, 'q')

    turtle.listen()

    turtle.exitonclick()