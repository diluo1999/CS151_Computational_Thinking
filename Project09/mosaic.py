# mosaic.py
# Di Luo
# CS 151 Fall 2018
# Project 9: Unique Trees and Shapes

import sys
import math
import shapes as s
import turtle_interpreter as ti

def tile(x, y, scale):
    '''draw a square tile with four trapezoids with different colors'''
    r3 = math.sqrt(3)
    trapezoid = s.Trapezoid(distance=scale, fill=True)
    trapezoid.setColor('red')
    trapezoid.draw(x+0.25*r3*scale, y+0.75*scale, 0.5, 270)
    trapezoid.setColor('green')
    trapezoid.draw(x+(1-0.25*r3)*scale, y+0.25*scale, 0.5, 90)
    trapezoid.setColor('orange')
    trapezoid.draw(x+0.75*scale, y+(1-0.25*r3)*scale, 0.5, 180)
    trapezoid.setColor('blue')
    trapezoid.draw(x+0.25*scale, y+0.25*r3*scale, 0.5, 0)

def mosaic(x, y, scale, Nx, Ny):
    '''draw a 2D array of tiles Nx by Ny'''
    for i in range(Nx):
        for j in range(Ny):
            tile(x+i*scale, y+j*scale, scale)

# extensions
def tile1(x, y, scale):
    '''draw a square tile with four rhombi with different colors'''
    r3 = math.sqrt(3)
    rhombus = s.Rhombus(distance=scale, fill=True)
    rhombus.setColor('yellow')
    rhombus.draw(x, y+0.5*scale, 0.5/r3, 30)
    rhombus.setColor('purple')
    rhombus.draw(x+0.5*scale, y+0.5*scale, 0.5/r3, 30)
    rhombus.setColor('pink')
    rhombus.draw(x+0.5*scale, y, 0.5/r3, 120)
    rhombus.setColor('black')
    rhombus.draw(x+0.5*scale, y+0.5*scale, 0.5/r3, 120)

def tile2(x, y, scale):
    '''draw a square tile with a yellow star and a red pentagon inside the star'''
    star = s.Star(distance=scale, fill=True)
    pentagon = s.Ngon(distance=scale, fill=True, ngon=5)
    star.setColor('yellow')
    pentagon.setColor('red')
    star.draw(x+0.1*scale, y+scale*0.6, 0.8, 0)
    pentagon.draw(x+0.6*scale, y+scale*0.6, 0.2, 180)

def mosaic1(x, y, scale, Nx, Ny):
    '''draw a 2D array of tiles (including tile1 and tile2) Nx by Ny'''
    for i in range(Nx):
        for j in range(int(Ny/3)):
            tile(x+i*scale, y+(3*j)*scale, scale)
            tile1(x+i*scale, y+(3*j+1)*scale, scale)
            tile2(x+i*scale, y+(3*j+2)*scale, scale)

def tile3(x, y, scale):
    '''draw a hexagon tile with six triangles with different colors'''

    r3 = math.sqrt(3)
    triangle = s.Triangle(distance=scale, fill=True)
    triangle.setColor('red')
    triangle.draw(x, y+scale*0.5*r3, 1, 60)
    triangle.setColor('orange')
    triangle.draw(x+scale*0.5, y+scale*r3, 1, 0)
    triangle.setColor('yellow')
    triangle.draw(x+scale, y+scale*0.5*r3, 1, 60)
    triangle.setColor('green')
    triangle.draw(x+scale, y+scale*0.5*r3, 1, 0)
    triangle.setColor('blue')
    triangle.draw(x+scale*0.5, y, 1, 60)
    triangle.setColor('purple')
    triangle.draw(x, y+scale*0.5*r3, 1, 0)

def mosaic2(x, y, scale, Nx, Ny):
    '''draws a 2D array of tiles (including tile3) Nx by Ny'''
    r3 = math.sqrt(3)
    if Nx % 2 == 0:
        for i in range(int(Nx/2)):
            for j in range(Ny):
                tile3(x+i*3*scale, y+j*r3*scale, scale)
            for k in range(Ny-1):
                tile3(x+(1.5+i*3)*scale, y+(0.5+k)*r3*scale, scale)
    else:
        for i in range(int(Nx/2)):
            for k in range(Ny-1):
                tile3(x+(1.5+i*3)*scale, y+(0.5+k)*r3*scale, scale)
        for i in range(int(Nx/2)+1):
            for j in range(Ny):
                tile3(x+i*3*scale, y+j*r3*scale, scale)

mosaic(-300, 50, 50, 5, 4)
# extensions
mosaic1(0, 50, 50, 6, 6)
mosaic2(-300, -300, 50, 6, 4)

# change Nx and Ny to create a sequence of images to create animation 
# (add # to all main code above and delete # for codes below one by one)
#mosaic2(-300, -300, 50, 1, 1)
#mosaic2(-300, -300, 50, 2, 2)
#mosaic2(-300, -300, 50, 3, 3)
#mosaic2(-300, -300, 50, 4, 4)
#mosaic2(-300, -300, 50, 5, 5)
#mosaic2(-300, -300, 50, 6, 6)
#mosaic2(-300, -300, 50, 7, 7)

ti.TurtleInterpreter().hold()