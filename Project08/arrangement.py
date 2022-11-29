# arrangement.py
# Di Luo
# CS 151 Fall 2018
# Project 8: Better Trees

import sys
import turtle_interpreter
import lsystem

def main(argv):
    '''Draw an arrangement of trees'''

    if len(argv) < 4:
        print('usage: %s systemEL.txt systemFL.txt systemGL.txt' % (argv[0]) )
        exit()
    
    tree1 = lsystem.Lsystem( argv[1] )
    tree2 = lsystem.Lsystem( argv[2] )
    tree3 = lsystem.Lsystem( argv[3] )

    sx = 800
    sy = 450
    terp = turtle_interpreter.TurtleInterpreter(sx, sy)

    for i in range(3):
        tstr1 = tree1.buildString(i+4)
        tstr2 = tree2.buildString(i+4)
        tstr3 = tree3.buildString(i+6)

        terp.color( (0.6+i*0.1, 0.4-i*0.1, 0.3+i*0.1 ) )

        terp.place( -150, 200-i*200, 90 )
        terp.drawString( tstr1, 2, 10+i*5 )

        terp.color( (0.3-i*0.1, 0.6+i*0.1, 0.5+i*0.2 ) )

        terp.place( 0, 200-i*200, 90 )
        terp.drawString( tstr2, 2, 20+i*10 )

        terp.color( (0.4-i*0.1, 0.3+i*0.2, 0.5+i*0.1 ) )

        terp.place( +150, 200-i*200, 90 )
        terp.drawString( tstr3, 2, 15+i*15 )
        
    terp.hold()

if __name__ == "__main__":
    main( sys.argv )