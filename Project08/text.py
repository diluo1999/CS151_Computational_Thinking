# text.py
# Di Luo
# CS 151 Fall 2018
# Project 8: Better Trees

import sys
import turtle_interpreter
import lsystem

def main(argv):
    '''Draw a tree from a L-system and print out base and rules in a dialog'''

    if len(argv) < 1:
        print('usage: %s systemEL.txt' % (argv[0]) )
        exit()
    
    tree = lsystem.Lsystem( argv[1] )
    
    sx = 300
    sy = 300
    terp = turtle_interpreter.TurtleInterpreter(sx, sy)

    terp.color( (0.5, 0.4, 0.3 ) )

    tstr = tree.buildString(6)
        
    terp.place( 0, 0, 90 )
    terp.drawString( tstr, 2, 10 )

    colorfulSquare = '<gF>-<yF>-<rF>-F'
    terp.place( -40, -50, 90 )
    terp.drawString( colorfulSquare, 20, 90 )
    dumbbell = '[<gF><rF>-F++++F++++F]-----F----F----F'
    terp.place( 30, -50, 0 )
    terp.drawString( dumbbell, 20, 30 )

    terp.text(tree)
 
    terp.hold()

if __name__ == "__main__":
    main( sys.argv )