# shapes.py
# Di Luo
# CS 151 Fall 2018
# Project 11: 3D Scenes

import tree
import sys
import random
import turtle_interpreter as t
import shapes as s

'''
Extension:
New L-systems
Create another scene of the Miller Library in Colby College
Create wire frame geodesic spheres
Set right mouse call back
'''

def main( argv ):

    if len(argv) < 3:
        print('usage: %s <systemZ2.txt> <Lsystem.txt> <opt: iterations>' % (argv[0]))
        exit()

    iterations = 6
    if len(argv) > 3:
        iterations = int(argv[2])

    ti = t.TurtleInterpreter()

    cuboid1 = s.Cuboid(distance=10, w=30, h=7, d=15)
    cuboid2 = s.Cuboid(distance=10, w=20, h=7, d=10)
    cuboid3 = s.Cuboid(distance=10, w=15, h=15, d=4)
    cuboid4 = s.Cuboid(distance=6, w=1, h=10, d=1)
    cylinder1 = s.Cylinder(distance=10, r=1, d=15)
    cylinder2 = s.Cylinder(distance=5, r=5, d=10)
    ball = s.Ball(distance=5, r=5)
    triangularPrism = s.TriangularPrism(distance=10, w=20, d=10)

    cuboid1.draw(-150, -300, zpos=-300)
    cuboid2.draw(-100, -230, zpos=-300)
    cuboid3.draw(-75, -160, zpos=-300)
    cylinder1.draw(-60, -160, roll=-90, zpos=-230)
    cylinder1.draw(-20, -160, roll=-90, zpos=-230)
    cylinder1.draw(20, -160, roll=-90, zpos=-230)
    cylinder1.draw(60, -160, roll=-90, zpos=-230)
    triangularPrism.draw(-100, -10, zpos=-300)
    cylinder2.draw(0, 200, roll=90, zpos=-250)
    ball.draw(0, 200, zpos=-250)
    cuboid4.draw(-3, 225, zpos=-250)

    triangularPrism.setDistance(2)
    triangularPrism.setColor('brown')
    triangularPrism.setd(50)
    triangularPrism.resetString()
    triangularPrism.drawBinaryTriangularPrism(x=-20, y=-10+80*s.r3, z=-300, nLevels=5)

    # Extension: new L-systems
    ld = tree.Tree( 10, filename = argv[1] )
    ld.setColor( (0.5, 0.4, 0.2) )
    ld.setWidth(2)
    ld.setIterations( iterations )
    for i in range(5):
        ld.draw( -200, -300, scale=1.0, zpos=-200+i*100)
    
    ld2 = tree.Tree( 10, filename = argv[2] )
    ld2.setColor('brown')
    ld2.setWidth(5)
    ld2.setIterations(4)
    for i in range(5):
        ld2.draw( 200, -300, scale=1.0, zpos=-200+i*100)
    ld2.setWidth(2)

    def Sphere(event):
        # Extension: create Wire frame geodesic spheres
        Ball = 'C^'*12
        ti.place(0, -100, angle=0, roll=-90, zpos=100)
        ti.color('blue')
        ti.drawString(Ball, 100, 30)
        ti.place(100, -100, angle=90, roll=90, zpos=0)
        ti.color('green')
        ti.drawString(Ball, 100, 30)
    
    # Extension: Set right mouse call back
    ti.setRightMouseCallback(Sphere)

    ti.hold()

if __name__ == '__main__':
    main(sys.argv)