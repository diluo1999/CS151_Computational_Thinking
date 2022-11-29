# shapes.py
# Di Luo
# CS 151 Fall 2018
# Project 9: Unique Trees and Shapes
# Version 1
import sys
import random
import turtle_interpreter as t

class Shape:

    def __init__(self, distance = 100, angle = 90, color = (0, 0, 0), istring = '' ):
        '''Initialize the Shape class'''
        self.distance = distance
        self.angle = angle
        self.color = color
        self.string = istring
    
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

    def draw(self, xpos, ypos, scale=1.0, orientation=0):
        '''draw the shape at (xpos, yos) with a scale and a orientation'''
        ti = t.TurtleInterpreter()
        ti.place(xpos, ypos, orientation)
        ti.color(self.color)
        ti.drawString(self.string, scale*self.distance, self.angle)
    
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

def test():
    '''a test function of drawing incorporated different shapes'''

    square = Square()
    triangle = Triangle()
    star = Star()
    rhombus = Rhombus()
    trapezoid = Trapezoid(fill=True)

    square.setColor('blue')
    square.draw(-50, 0, 1, 0)
    triangle.setColor('green')
    triangle.draw(50, 0, 1, 180)
    rhombus.setColor('purple')
    rhombus.draw(0, 0, 1, 120)
    star.draw(-25, 100, 0.5, 0)
    trapezoid.draw(-50, -100, 1, 0)

    t.TurtleInterpreter().hold()

if __name__ == "__main__":
    test()
