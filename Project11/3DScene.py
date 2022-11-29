# shapes.py
# Di Luo
# CS 151 Fall 2018
# Project 11: 3D Scenes

import sys
import random
import turtle_interpreter as t
import shapes as s

'''
Create a scene of the Miller Library in Colby College
'''


cuboid1 = s.Cuboid(distance=10, w=30, h=7, d=15)
cuboid2 = s.Cuboid(distance=10, w=20, h=7, d=10)
cuboid3 = s.Cuboid(distance=10, w=15, h=15, d=4)
cuboid4 = s.Cuboid(distance=6, w=1, h=10, d=1)
cylinder1 = s.Cylinder(distance=10, r=1, d=15)
cylinder2 = s.Cylinder(distance=5, r=5, d=10)
ball = s.Ball(distance=5, r=5)
triangularPrism = s.TriangularPrism(distance=10, w=20, d=10)

cuboid1.draw(-150, -300)
cuboid2.draw(-100, -230)
cuboid3.draw(-75, -160)
cylinder1.draw(-60, -160, roll=-90, zpos=70)
cylinder1.draw(-20, -160, roll=-90, zpos=70)
cylinder1.draw(20, -160, roll=-90, zpos=70)
cylinder1.draw(60, -160, roll=-90, zpos=70)
triangularPrism.draw(-100, -10)
cylinder2.draw(0, 200, roll=90, zpos=50)
ball.draw(0, 200, zpos=50)
cuboid4.draw(-3, 225, zpos=50)

# Task 3 (uncomment the codes below for Task 3)
# triangularPrism.setDistance(2)
# triangularPrism.setColor('brown')
# triangularPrism.setd(50)
# triangularPrism.resetString()
# triangularPrism.drawBinaryTriangularPrism(x=-20, y=-10+80*s.r3, z=0, nLevels=5)

t.TurtleInterpreter().hold()