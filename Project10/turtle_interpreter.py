# turtle_interpreter.py
# Di Luo
# CS 151 Fall 2018
# Project 10: Non-Photorealistic Rendering
# Version 4

import sys
import turtle
import random

class TurtleInterpreter:

    initialized = False

    def __init__(self, dx = 800, dy = 800):
        '''Initialize the TurtleInterpreter class'''
        self.style = 'normal'
        self.jitterSigma = 2
        self.dotSize = 2
        self.lineSize = 4
        if TurtleInterpreter.initialized:
	        return
        TurtleInterpreter.initialized = True
        turtle.setup(dx, dy)
        turtle.tracer(False)
    
    def setStyle(self, s):
        '''set the style field to s'''
        self.style = s
    
    def setJitter(self, j):
        '''set the jitterSigme field to j'''
        self.jitterSigma = j

    def setWidth(self, w):
        '''set the line width to w'''
        turtle.width(w)
    
    def setDotSize(self, d):
        '''set the dot size to d'''
        self.dotSize = d
    
    def setLineSize(self, l):
        '''set the line size of angled lines to l'''
        self.lineSize = l
    
    def forward(self, distance):
        '''draw a line of length 'distance' in different styles'''
        if self.style == 'normal':
            turtle.forward(distance)
        elif self.style == 'jitter':
            (x0, y0) = turtle.position()
            turtle.penup()
            turtle.forward(distance)
            (xf, yf) = turtle.position()
            curwidth = turtle.width()
        
            jx = random.gauss(0, self.jitterSigma)
            jy = random.gauss(0, self.jitterSigma)
            kx = random.gauss(0, self.jitterSigma)
            ky = random.gauss(0, self.jitterSigma)

            turtle.width(curwidth + random.randint(0, 2))
            turtle.goto(x0 + jx, y0 + jy)
            turtle.pendown()
            turtle.goto(xf + kx, yf + ky)
            turtle.penup()
            turtle.goto(xf, yf)
            turtle.width(curwidth)
            turtle.pendown()
        elif self.style == 'jitter3':
            (x0, y0) = turtle.position()
            turtle.penup()
            turtle.forward(distance)
            (xf, yf) = turtle.position()
            curwidth = turtle.width()
            for i in range(3):
                jx = random.gauss(0, self.jitterSigma)
                jy = random.gauss(0, self.jitterSigma)
                kx = random.gauss(0, self.jitterSigma)
                ky = random.gauss(0, self.jitterSigma)

                turtle.width(curwidth + random.randint(0, 2))
                turtle.goto(x0 + jx, y0 + jy)
                turtle.pendown()
                turtle.goto(xf + kx, yf + ky)
                turtle.penup()
            turtle.goto(xf, yf)
            turtle.width(curwidth)
            turtle.pendown()
        elif self.style == 'dotted':
            (x0, y0) = turtle.position()
            turtle.penup()
            turtle.forward(distance)
            (xf, yf) = turtle.position()
            turtle.goto(x0, y0)
            for i in range(int(distance/(self.dotSize*2))):
                if i%2==0:
                    turtle.pendown()
                    turtle.begin_fill()
                    turtle.circle(self.dotSize)
                    turtle.end_fill()
                    turtle.penup()
                    turtle.forward(self.dotSize*4)
            turtle.goto(xf, yf)
            turtle.pendown()
        elif self.style == 'angledLines':
            (x0, y0) = turtle.position()
            turtle.penup()
            turtle.forward(distance)
            (xf, yf) = turtle.position()
            turtle.goto(x0, y0)
            for i in range(int(distance/(self.lineSize/2))):
                turtle.pendown()
                turtle.right(60)
                turtle.forward(self.lineSize)
                turtle.penup()
                turtle.backward(self.lineSize)
                turtle.left(60)
                turtle.forward(int(self.lineSize/2))
            turtle.goto(xf, yf)
            turtle.pendown()
        elif self.style == 'brush':
            color = ['red', 'orange', 'yellow', 'green', 'blue']
            (x0, y0) = turtle.position()
            turtle.penup()
            turtle.forward(distance)
            (xf, yf) = turtle.position()
            c = turtle.color()[0]
            turtle.goto(x0, y0)
            w = turtle.width()
            turtle.left(90)
            turtle.forward(w*2.5)
            turtle.right(90)
            turtle.pendown()
            for i in range(5):
                turtle.color(color[i])
                turtle.forward(distance)
                turtle.penup()
                turtle.backward(distance)
                turtle.right(90)
                turtle.forward(w)
                turtle.left(90)
                turtle.pendown()
            turtle.penup()
            turtle.goto(xf, yf)
            turtle.color(c)
            turtle.pendown()
            
    def drawString(self, dstring, distance, angle, droop=False):
        ''' Interpret the characters in string dstring as a series
        of turtle commands. Distance specifies the distance
        to travel for each forward command. Angle specifies the
        angle (in degrees) for each right or left command. The list of 
        turtle supported turtle commands is:
        F/f : draw either a normal line or a jittered line
        - : turn right
        + : turn left
        ! : set width of turtle
        [ : save position and heading
        ] : restore position and heading
        < : push the current turtle color onto a color stack
        > : pop the current turtle color off the color stack and set the turtle's color to that value
        g : set the turtle's color to green
        y : set the turtle's color to light yellow
        r : set the turtle's color to red
        L : draw a leaf
        B : draw a berry
        { : begin to fill
        } : end filling
        ( : begin to grab
        ) : end grabing
        '''
        modstring = ''
        modval = None
        modgrab = False

        stack = []
        colorstack = []

        for char in dstring:
            if char == '(':
                modstring = ''
                modgrab = True
                continue
            elif char == ')':
                modval = float(modstring)
                modgrab = False
                continue
            elif modgrab:
                modstring += char
                continue
            
            if char == 'F' or char == 'f':
                if modval == None:
                    self.forward(distance)
                else:
                    self.forward(distance * modval)
            elif char == '-':
                if droop == False:
                    if modval == None:
                        turtle.right(angle)
                    else:
                        turtle.right(modval)
                else:
                    if modval == None:
                        if 90<turtle.heading()<=270:
                            turtle.right(angle-20)
                        elif 0<=turtle.heading()<=90 or 270<turtle.heading()<=360:
                            turtle.right(angle+20)
                    else:
                        if 90<turtle.heading()<=270:
                            turtle.right(modval-20)
                        elif 0<=turtle.heading()<=90 or 270<turtle.heading()<=360:
                            turtle.right(modval+20)
            elif char == '+':
                if modval == None:
                    turtle.left(angle)
                else:
                    turtle.left(modval)
            elif char == '!':
                if modval == None:
                    w = turtle.width()
                    if w > 1:
                        turtle.width(w-1)
                else:
                    turtle.width(modval)
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
            elif char == '{':
                turtle.begin_fill()
            elif char == '}':
                turtle.end_fill()
            modval = None
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