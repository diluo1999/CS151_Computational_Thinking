# scene.py
# Di Luo
# CS 151 Fall 2018
# Project 7: Fractals and Trees

import sys
import turtle
import lsystem as ls
import turtle_interpreter as ti

def draw( lstr, x, y, dist, angle, color):
    ''' Draws a l-system string given an (x,y) anchor, distance, angle and color '''

    oldheading = turtle.heading()

    turtle.penup()
    turtle.goto( x, y )
    turtle.pendown()
    turtle.color( color )
    turtle.width( 1 )

    ti.drawString( lstr, dist, angle )

    turtle.setheading( oldheading )

    return

def main(argv):
    ''' Create a scene including a black house with a brown roof and two green trees'''

    if len(argv) < 4:
        print('usage: %s house.txt roof.txt tree.txt' % (argv[0]))
        exit()

    lsys1 = ls.createLsystemFromFile( argv[1] )
    lsys2 = ls.createLsystemFromFile( argv[2] )
    lsys3 = ls.createLsystemFromFile( argv[3] )

    lstr1 = ls.buildString( lsys1, 4 )
    lstr2 = ls.buildString( lsys2, 4 )
    lstr3 = ls.buildString( lsys3, 4 )

    turtle.tracer(False)

    draw( lstr1, -100, 100, 2, 90, 'black' )
    draw( lstr2, -140, 100, 3, 90, 'brown' )
    turtle.left(90)
    draw( lstr3, 200, -100, 4, 25.7, 'green' )
    draw( lstr3, -200, -100, 4, 25.7, 'green' )

    ti.hold()

if __name__ == "__main__":
    main( sys.argv )