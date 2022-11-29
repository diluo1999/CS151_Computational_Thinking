# growth.py
# Di Luo
# CS 151 Fall 2018
# Project 8: Better Trees

import sys
import turtle_interpreter
import lsystem

def main(argv):
    '''create an image of a scene of trees using variation L-systems 
    in system1.txt and system2.txt after 2, 3, and 4 iterations'''

    if len(argv) < 3:
        print('usage: %s system1.txt system2.txt' % (argv[0]) )
        exit()
    
    tree1 = lsystem.Lsystem( argv[1] )
    tree2 = lsystem.Lsystem( argv[2] )

    sx = 800
    sy = 450
    terp = turtle_interpreter.TurtleInterpreter(sx, sy)

    terp.color( (0.5, 0.4, 0.3 ) )

    for i in range(3):
        tstr1 = tree1.buildString(i+2)
        tstr2 = tree2.buildString(i+2)

        terp.place( -300+i*100, 100-i*100, 90 )
        terp.drawString( tstr1, 5, 20 )
        terp.place( +300-i*100, 100-i*100, 90 )
        terp.drawString( tstr2, 5, 17 )
        
    terp.hold()

if __name__ == "__main__":
    main( sys.argv )