# shapes.py
# Di Luo
# CS 151 Fall 2018
# Project 11: 3D Scenes
# Version 5

import sys
import random
import turtle_interpreter as t
import math

r3 = math.sqrt(3)

class Shape:

    def __init__(self, distance = 100, angle = 90, color = (0, 0, 0), istring = '' ):
        '''Initialize the Shape class'''
        self.style = 'normal'
        self.jitterSigma = 2
        self.lineWidth = 1
        self.distance = distance
        self.angle = angle
        self.color = color
        self.string = istring
        self.dotSize = 2
    
    def setStyle(self, s):
        '''set the style field to s'''
        self.style = s
    
    def setJitter(self, j):
        '''set the jitterSigme field to j'''
        self.jitterSigma = j
    
    def setWidth(self, w):
        '''set the lineWidth field to w'''
        self.lineWidth = w
    
    def setColor(self, c):
        '''set the color field to c'''
        self.color = c

    def setDistance(self, d):
        '''set the distance field to d'''
        self.distance = d
    
    def setAngle(self, a):
        '''set the angle field to a'''
        self.angle = a

    def setString(self, s):
        '''set the string field to s'''
        self.string = s
    
    def setDotSize(self, d):
        '''set the dot size to d'''
        self.dotSize = d

    def draw(self, xpos, ypos, scale=1.0, orientation=0, pitch=0, roll=0, zpos=0):
        '''draw the shape at (xpos, yos) with a scale and a orientation'''
        ti = t.TurtleInterpreter()
        ti.place(xpos, ypos, orientation, pitch, roll, zpos)
        ti.setStyle(self.style)
        ti.setJitter(self.jitterSigma)
        ti.setWidth(self.lineWidth)
        ti.setDotSize(self.dotSize)
        ti.color(self.color)
        ti.drawString(self.string, scale*self.distance, self.angle)
    
class Square(Shape):
    '''Initialize Square class as the child class of Shape'''
    def __init__(self, distance=100, color=(0, 0, 0) ):
        Shape.__init__(self, distance, 90, color, 'F-F-F-F-')

class Triangle(Shape):
    '''Initialize Triangle class as the child class of Shape'''
    def __init__(self, distance=100, color=(0, 0, 0) ):
        Shape.__init__(self, distance, 120, color, 'F-F-F-')

class Cuboid(Shape):
    '''Cuboid with adjustable side lengths in
    width (w; x), height (h; y), and depth (d; z)
    '''
    def __init__(self, distance=5, color=(0, 0, 0),
                 w=1, h=1, d=1):
        Shape.__init__(self, distance=distance, angle=90, color=color)

        baseAndSide_str = f'({w})F+[^({d})F]({h})F+[^({d})F]({w})F+[^({d})F]({h})F+^({d})F'
        top_str = f'&({w})F+({h})F+({w})F+({h})F'

        self.setString(''.join([baseAndSide_str, top_str]))

class Cylinder(Shape):
    '''Cylinder with adjustable radius and depth in
    radius (r; x/y), depth (d; z)
    '''
    def __init__(self, distance=5, color=(1, 0, 0),
                 r=2, d=1):
        Shape.__init__(self, distance=distance, angle=90, color=color)

        baseAndSide_str = f'[-({r})F+({r})C][({r})F^({d})F]+[({r})F^({d})F]+[({r})F^({d})F]'
        middleAndTop_str = f'+({r})F+^({d/2})F&({r})C^({d/2})F&({r})C'

        self.setString(''.join([baseAndSide_str, middleAndTop_str]))

class Ball(Shape):
    '''Ball with adjustable radius in radius (r)'''
    def __init__(self, distance=5, color=(0, 1, 0),
                r=1):
        Shape.__init__(self, distance=distance, angle=90, color=color)

        ball_str = f'[-({r})F+({r})C-^\\({r})C]({r})F^\\({r})C'

        self.setString(ball_str)

class TriangularPrism(Shape):
    '''Triangular prism with adjustable side lengths in
    width (w; x), and depth (d; z)
    '''
    def __init__(self, distance=5, color=(0, 0, 1), w=1, d=1):
        Shape.__init__(self, distance=distance, angle=90, color=color)
        self.w = w
        self.d = d

        baseAndSide_str = f'({w})F(120)+[^({d})F]({w})F(120)+[^({d})F]({w})F(120)+'
        top_str = f'^({d})F&({w})F(120)+({w})F(120)+({w})F'

        self.setString(''.join([baseAndSide_str, top_str]))

    # Task 3
    def setw(self, w):
        '''set the field of w as w'''
        self.w = w
    
    def setd(self, d):
        '''set the field of d as d'''
        self.d = d
    
    def resetString(self):
        '''reset the string'''
        baseAndSide_str = f'({self.w})F(120)+[^({self.d})F]({self.w})F(120)+[^({self.d})F]({self.w})F(120)+'
        top_str = f'^({self.d})F&({self.w})F(120)+({self.w})F(120)+({self.w})F'

        self.setString(''.join([baseAndSide_str, top_str]))

    def drawBinaryTriangularPrism(self, x, y, z, nLevels):

        if nLevels == 0:
            return

        self.width = self.w*self.distance
        self.depth = self.d*self.distance
        
        self.draw(xpos=x, ypos=y, zpos=z)

        self.drawBinaryTriangularPrism(x=x-self.width/2, y=y-r3*self.width/2, z=z, nLevels=nLevels-1)
        self.drawBinaryTriangularPrism(x=x+self.width/2, y=y-r3*self.width/2, z=z, nLevels=nLevels-1)


def test():
    '''a test function showing my 3D shapes:
    Cuboid, Cylinder, Ball, and TriangularPrism 
    with 2 different styles
    '''
    cuboid = Cuboid(distance=20)
    cylinder = Cylinder(distance=10, d=5)
    ball = Ball(distance=20)
    triangularPrism = TriangularPrism(distance=20, w=2, d=1)

    cuboid.draw(-50, 100)
    cuboid.setStyle('jitter')
    cuboid.draw(-20, 100)

    cylinder.draw(50, 100)
    cylinder.setStyle('dotted')
    cylinder.draw(100, 100)

    ball.draw(-50, -100)
    ball.setStyle('jitter3')
    ball.draw(0, -100)

    triangularPrism.draw(50, -100)
    triangularPrism.setStyle('dotted')
    triangularPrism.draw(100, -100)

    t.TurtleInterpreter().hold()

if __name__ == "__main__":
    test()