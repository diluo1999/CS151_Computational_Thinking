# turtle_interpreter.py
# Di Luo
# CS 151 Fall 2018
# Project 8: Better Trees
# Version 2

import sys
import turtle
import random

class TurtleInterpreter:

    def __init__(self, dx = 800, dy = 800):
        turtle.setup(dx, dy)
        turtle.tracer(False)

    def drawString(self, dstring, distance, angle):
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
        < : push the current turtle color onto a color stack
        > : pop the current turtle color off the color stack and set the turtle's color to that value
        g : set the turtle's color to green
        y : set the turtle's color to light yellow
        r : set the turtle's color to red
        w : set the turtle's color to wheat
        b : set the turtle's color to black
        s : set the turtle's color to sky blue
        L : draw a leaf
        B : draw a berry
        ( : start to fill color
        ) : end filling color
        '''

        stack = []
        colorstack = []

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
            elif char == '<':
                colorstack.append( turtle.color()[0] )
            elif char == '>':
                turtle.color(colorstack.pop())
            elif char == 'g':
                turtle.color(0.15, 0.5, 0.2)
            elif char == 'y':
                turtle.color(0.8, 0.8, 0.3)
            elif char == 'r':
                turtle.color(0.7, 0.2, 0.3)
            elif char == 'w':
                turtle.color('wheat')
            elif char == 'b':
                turtle.color('black')
            elif char == 's':
                turtle.color('sky blue')
            elif char == 'L':
                oldheading = turtle.heading()
                turtle.begin_fill()
                turtle.left(30)
                turtle.forward(int(distance))
                turtle.right(60)
                turtle.forward(int(distance))
                turtle.right(120)
                turtle.forward(int(distance))
                turtle.right(60)
                turtle.forward(int(distance))
                turtle.end_fill()
                turtle.setheading( oldheading )
            elif char == 'B':
                oldheading = turtle.heading()
                turtle.begin_fill()
                turtle.circle(0.5*distance)
                turtle.end_fill()
                turtle.setheading( oldheading )
            elif char == '(':
                turtle.begin_fill()
            elif char == ')':
                turtle.end_fill()

        turtle.update()

    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' key'''

        turtle.hideturtle()
        turtle.update()

        turtle.onkey(turtle.bye, 'q')

        turtle.listen()

        turtle.exitonclick()
    
    def place(self, xpos, ypos, angle=None):
        '''place the turtle at location (xpos, ypos), 
        orient the turtle if the angle argument is not None'''
        turtle.penup()
        turtle.goto(xpos, ypos)
        if angle != None:
            turtle.setheading(angle)
        turtle.pendown()


    def orient(self, angle):
        '''set turtle's heading to the given angle'''
        turtle.setheading(angle)

    def goto(self, xpos, ypos):
        '''Moves the turtle to position (xpos, ypos)'''
        turtle.penup()
        turtle.goto(xpos, ypos)
        turtle.pendown()

    
    def color(self, c):
        '''set c as the color of turtle'''
        turtle.color(c)
    
    def width(self, w):
        '''set w asthe width of turtle'''
        turtle.width(w)
    
    def text(self, object):
        '''Print out the base and rules of L-system (object) in a dialog'''
        turtle.textinput('L-system',str(object))