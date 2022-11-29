# turtle_interpreter.py
# Di Luo
# CS 151 Fall 2018
# Project 11: 3D Scenes
# Version 5

import sys
import turtleTk3D
import random

turtle = None

class TurtleInterpreter:

    initialized = False

    def __init__(self, dx = 800, dy = 800):
        '''Initialize the TurtleInterpreter class'''
        self.style = 'normal'
        self.jitterSigma = 2
        self.dotSize = 2
        if TurtleInterpreter.initialized:
	        return
        TurtleInterpreter.initialized = True
        global turtle
        turtle = turtleTk3D.Turtle3D(dx, dy)
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
    
    def forward(self, distance):
        '''draw either a normal line or a jittered line with distance'''
        if self.style == 'normal':
            turtle.forward(distance)
        elif self.style == 'jitter':
            (x0, y0, z0) = turtle.position()
            turtle.up()
            turtle.forward(distance)
            (xf, yf, zf) = turtle.position()
            curwidth = turtle.width()
        
            jx = random.gauss(0, self.jitterSigma)
            jy = random.gauss(0, self.jitterSigma)
            jz = random.gauss(0, self.jitterSigma)
            kx = random.gauss(0, self.jitterSigma)
            ky = random.gauss(0, self.jitterSigma)
            kz = random.gauss(0, self.jitterSigma)

            turtle.width(curwidth + random.randint(0, 2))
            turtle.goto(x0 + jx, y0 + jy, z0 + jz)
            turtle.down()
            turtle.goto(xf + kx, yf + ky, zf + kz)
            turtle.up()
            turtle.goto(xf, yf, zf)
            turtle.width(curwidth)
            turtle.down()
        elif self.style == 'jitter3':
            (x0, y0,z0) = turtle.position()
            turtle.up()
            turtle.forward(distance)
            (xf, yf, zf) = turtle.position()
            curwidth = turtle.width()
            for i in range(3):
                jx = random.gauss(0, self.jitterSigma)
                jy = random.gauss(0, self.jitterSigma)
                jz = random.gauss(0, self.jitterSigma)
                kx = random.gauss(0, self.jitterSigma)
                ky = random.gauss(0, self.jitterSigma)
                kz = random.gauss(0, self.jitterSigma)

                turtle.width(curwidth + random.randint(0, 2))
                turtle.goto(x0 + jx, y0 + jy, z0 + jz)
                turtle.down()
                turtle.goto(xf + kx, yf + ky, zf + kz)
                turtle.up()
            turtle.goto(xf, yf, zf)
            turtle.width(curwidth)
            turtle.down()
        elif self.style == 'dotted':
            (x0, y0, z0) = turtle.position()
            turtle.up()
            turtle.forward(distance)
            (xf, yf, zf) = turtle.position()
            turtle.goto(x0, y0, z0)
            turtle.right(90)
            turtle.forward(self.dotSize)
            turtle.left(90)
            for i in range(int(distance/(self.dotSize*2))):
                if i%2==0:
                    turtle.down()
                    turtle.fill(True)
                    turtle.circle(self.dotSize)
                    turtle.fill(False)
                    turtle.up()
                    turtle.forward(self.dotSize*4)
            turtle.goto(xf, yf, zf)
            turtle.down()
    #Extension
    def setRightMouseCallback(self, function):
        turtle.setRightMouseCallback(function)


    def drawString(self, dstring, distance, angle):
        ''' Interpret the characters in string dstring as a series
        of turtle commands. Distance specifies the distance
        to travel for each forward command. Angle specifies the
        angle (in degrees) for each right or left command. The list of 
        turtle supported turtle commands is:
        F : draw either a normal line or a jittered line
        - : turn right
        + : turn left
        [ : save position and heading
        ] : restore position and heading
        < : push the current turtle color onto a color stack
        > : pop the current turtle color off the color stack and set the turtle's color to that value
        g : set the turtle's color to green
        y : set the turtle's color to light yellow
        r : set the turtle's color to red
        L : draw a leaf
        { : begin to fill
        } : end to fill
        
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
            elif char == '&':
                if modval == None:
                    turtle.pitch(angle)
                else:
                    turtle.pitch(modval)
            elif char == '^':
                if modval == None:
                    turtle.pitch(-angle)
                else:
                    turtle.pitch(-modval)
            elif char == '\\':
                if modval == None:
                    turtle.roll(angle)
                else:
                    turtle.roll(modval)
            elif char == '/':
                if modval == None:
                    turtle.roll(-angle)
                else:
                    turtle.roll(-modval)
            elif char == '-':
                if modval == None:
                    turtle.right(angle)
                else:
                    turtle.right(modval)
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
                stack.append(turtle.width())
            elif char == ']':
                turtle.up()
                turtle.width(stack.pop())
                turtle.setheading(stack.pop())
                turtle.goto(stack.pop())
                turtle.down()
            elif char == '<':
                colorstack.append( turtle.color() )
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
                turtle.fill(True)
                turtle.left(30)
                turtle.forward(int(distance)*0.5)
                turtle.right(60)
                turtle.forward(int(distance)*0.5)
                turtle.right(120)
                turtle.forward(int(distance)*0.5)
                turtle.right(60)
                turtle.forward(int(distance)*0.5)
                turtle.fill(False)
                turtle.setheading( oldheading )
            elif char == 'B':
                oldheading = turtle.heading()
                turtle.begin_fill()
                turtle.circle(0.2*distance)
                turtle.end_fill()
                turtle.setheading( oldheading )
            elif char == 'C':
                if modval == None:
                    turtle.circle(distance)
                else:
                    turtle.circle(distance * modval)
            elif char == '{':
                turtle.fill(True)
            elif char == '}':
                turtle.fill(False)
            modval = None
        turtle.update()

    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' key'''
        turtle.mainloop()
    
    def place(self, xpos, ypos, angle=None, pitch=0, roll=0, zpos=0):
        '''place the turtle at location (xpos, ypos), 
        orient the turtle if the angle argument is not None'''
        turtle.up()
        turtle.goto(xpos, ypos, zpos)
        if angle != None:
            self.orient(angle, roll, pitch)
        turtle.down()


    def orient(self, angle, roll=0, pitch=0):
        '''set turtle's heading to the given angle'''
        turtle.setheading(0)
        turtle.roll(roll)
        turtle.pitch(pitch)
        turtle.yaw(angle)

    def goto(self, xpos, ypos, zpos=0):
        '''Moves the turtle to position (xpos, ypos, zpos)'''
        turtle.up()
        turtle.goto(xpos, ypos, zpos)
        turtle.down()

    
    def color(self, c):
        '''set c as the color of turtle'''
        turtle.color(c)
    
    def width(self, w):
        '''set w asthe width of turtle'''
        turtle.width(w)
    
    def roll(self, r):
        '''roll the turtle with r'''
        turtle.roll(r)

    def pitch(self, p):
        '''pitch the turtle with p'''
        turtle.pitch(p)

    def yaw(self, y):
        '''yaw the turtle with y'''
        turtle.yaw(y)
