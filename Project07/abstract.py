# abstract.py
# Di Luo
# CS 151 Fall 2018
# Project 7: Fractals and Trees

import sys
import turtle
import lsystem as ls
import turtle_interpreter as ti

def four( lstr, x, y, dist, angle ):
    ''' Draws four l-system strings forming a cross given an (x,y) anchor, distance and angle '''
    oldheading = turtle.heading()

    turtle.color( 'green' )
    turtle.width( 1 )

    for i in range(4):
        turtle.penup()
        turtle.goto( x, y )
        turtle.pendown()
        turtle.setheading( oldheading )
        turtle.left(i*90)
        ti.drawString( lstr, dist, angle )

    turtle.setheading( oldheading )

    return

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

def abstract(lstr1, lstr2, lstr3, x, y, scale):
    '''Draw the abstract image'''

    draw( lstr1, x-128*scale, y+128*scale, 1*scale, 90, 'black' )
    
    four( lstr2, x, y, 5*scale, 30 )

    draw( lstr3, x-23*scale, y+13*scale, 5*scale, 60, 'blue' )

def main(argv):
    '''Create an abstract picture'''

    if len(argv) < 4:
        print('usage: %s system1.txt system2.txt system3.txt' % (argv[0]))
        exit()

    lsys1 = ls.createLsystemFromFile( argv[1] )
    lsys2 = ls.createLsystemFromFile( argv[2] )
    lsys3 = ls.createLsystemFromFile( argv[3] )

    lstr1 = ls.buildString( lsys1, 4 )
    lstr2 = ls.buildString( lsys2, 3 )
    lstr3 = ls.buildString( lsys3, 2 )

    turtle.tracer(False)

    abstract(lstr1, lstr2, lstr3, 0, 0, 1)
    # Extensions below
    #abstract(lstr1, lstr2, lstr3, -200, 0, 2)
    #abstract(lstr1, lstr2, lstr3, 200, 0, 3)
    
    ti.hold()

if __name__ == "__main__":
    main( sys.argv )

