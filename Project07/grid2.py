# grid2.py
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

def grid(listLstr, x, y, scale):
    ''' Draw the grid'''

    for x0 in [x-60*scale, x, x+80*scale]:
        angle = [60, 46, 22]
        for y0 in [y+120*scale, y, y-120*scale]:
            a = angle.pop()
            lstr = listLstr.pop()
            draw( lstr, x0, y0, 5*scale, a, 'black' )

def main(argv):
    '''Create and order the 9 trees as a 3x3 grid, 
    From left to right the number of iterations of the L-system goes from 1 to 3. 
    From top to bottom, the angles of the L-system are 22, 46, and 60
    '''

    if len(argv) < 4:
        print('usage: %s systemS.txt systemF.txt systemW.txt' % (argv[0]))
        exit()

    lsys = ls.createLsystemFromFile( argv[1] )
    lstr1 = ls.buildString( lsys, 1 )
    lstr4 = ls.buildString( lsys, 2 )
    lstr7 = ls.buildString( lsys, 3 )
    lsys = ls.createLsystemFromFile( argv[2] )
    lstr2 = ls.buildString( lsys, 1 )
    lstr5 = ls.buildString( lsys, 2 )
    lstr8 = ls.buildString( lsys, 3 )
    lsys = ls.createLsystemFromFile( argv[3] )
    lstr3 = ls.buildString( lsys, 1 )
    lstr6 = ls.buildString( lsys, 2 )
    lstr9 = ls.buildString( lsys, 3 )

    turtle.tracer(False)

    turtle.left(90)

    listLstr = [lstr9, lstr8, lstr7, lstr6, lstr5, lstr4, lstr3, lstr2, lstr1]

    grid(listLstr, 0, 0, 1)
    
    ti.hold()

if __name__ == "__main__":
    main( sys.argv )

