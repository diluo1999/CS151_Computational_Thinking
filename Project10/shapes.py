# shapes.py
# Di Luo
# CS 151 Fall 2018
# Project 10: Non-Photorealistic Rendering
# Version 2

import sys
import random
import turtle_interpreter as t

class Shape:

    def __init__(self, distance = 100, angle = 90, color = (0, 0, 0), istring = '' ):
        '''Initialize the Shape class'''
        self.style = 'normal'
        self.jitterSigma = 2
        self.dotSize = 2
        self.lineSize = 4
        self.lineWidth = 1
        self.distance = distance
        self.angle = angle
        self.color = color
        self.string = istring
    
    def setStyle(self, s):
        '''set the style field to s'''
        self.style = s
    
    def setJitter(self, j):
        '''set the jitterSigme field to j'''
        self.jitterSigma = j
    
    def setWidth(self, w):
        '''set the lineWidth field to w'''
        self.lineWidth = w
    
    def setDotSize(self, d):
        '''set the dot size to d'''
        self.dotSize = d
    
    def setLineSize(self, l):
        '''set the line size of angled lines to l'''
        self.lineSize = l
    
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

    def draw(self, xpos, ypos, scale=1.0, orientation=0, droop=False):
        '''draw the shape at (xpos, yos) with a scale and a orientation'''
        ti = t.TurtleInterpreter()
        ti.place(xpos, ypos, orientation)
        ti.setStyle(self.style)
        ti.setJitter(self.jitterSigma)
        ti.setWidth(self.lineWidth)
        ti.setDotSize(self.dotSize)
        ti.color(self.color)
        ti.setLineSize(self.lineSize)
        ti.drawString(self.string, scale*self.distance, self.angle, droop)
    
class Square(Shape):
    '''Initialize Square class as the child class of Shape'''
    def __init__(self, distance=100, color=(0, 0, 0), fill=False):
        draw_str = 'F-F-F-F-'
        if fill:
            draw_str = '{' + draw_str + '}'
        Shape.__init__(self, distance, 90, color, draw_str)

class Triangle(Shape):
    '''Initialize Triangle class as the child class of Shape'''
    def __init__(self, distance=100, color=(0, 0, 0), fill=False):
        draw_str = 'F-F-F-'
        if fill:
            draw_str = '{' + draw_str + '}'
        Shape.__init__(self, distance, 120, color, draw_str)

class Star(Shape):
    '''Initialize Star class as the child class of Shape'''
    def __init__(self, distance=100, color=(0, 0, 0), fill=False):
        draw_str = 'F-F-F-F-F-'
        if fill:
            draw_str = '{' + draw_str + '}'
        Shape.__init__(self, distance, 144, color, draw_str)

class Rhombus(Shape):
    '''Initialize Rhombus class as the child class of Shape'''
    def __init__(self, distance=100, color=(0, 0, 0), fill=False):
        draw_str = 'F-F--F-F--'
        if fill:
            draw_str = '{' + draw_str + '}'
        Shape.__init__(self, distance, 60, color, draw_str)

class Trapezoid(Shape):
    '''Initialize Trapezoid class as the child class of Shape'''
    def __init__(self, distance=100, color=(0, 0, 0), fill=False):
        draw_str = 'F-F--FF--F-'
        if fill:
            draw_str = '{' + draw_str + '}'
        Shape.__init__(self, distance, 60, color, draw_str)

class Ngon(Shape):
    '''Initialize Ngon class as the child class of Shape'''
    def __init__(self, distance=100, color=(0, 0, 0), fill=False, ngon=3):
        if ngon < 3:
            print('ngon should not be smaller than 3')
            return
        angle = 360/ngon
        draw_str = ngon*'F+'
        if fill:
            draw_str = '{' + draw_str + '}'
        Shape.__init__(self, distance, angle, color, draw_str)