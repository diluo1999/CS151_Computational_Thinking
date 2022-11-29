# scene.py
# Di Luo
# CS 151 Fall 2018
# Project 8: Better Trees

import sys
import turtle_interpreter
import lsystem

def main(argv):
    '''Draw an countryside scene'''

    if len(argv) < 4:
        print('usage: %s system3.txt system4.txt house.txt roof.txt' % (argv[0]) )
        exit()
    
    tree1 = lsystem.Lsystem( argv[1] )
    tree2 = lsystem.Lsystem( argv[2] )
    house = lsystem.Lsystem( argv[3] )
    roof = lsystem.Lsystem( argv[4] )

    tstr1 = tree1.buildString(3)
    tstr2 = tree2.buildString(4)
    housestr = house.buildString(4)
    roofstr = roof.buildString(4)

    sx = 800
    sy = 600
    terp = turtle_interpreter.TurtleInterpreter(sx, sy)
    
    terp.place( -400, -300, 0 )
    terp.drawString( '<w(FFFFFFFF+FFF+FFFFFFFF+FFF)>', 100, 90 )

    terp.place( -400, 0, 0 )
    terp.drawString( '<s(FFFFFFFF+FFF+FFFFFFFF+FFF)>', 100, 90 )

    terp.color( 'black' )
    terp.place( -250, -300, 0 )
    terp.drawString( '(FF++F+F+F)', 250, 60 )

    terp.place( -75, 100, 0 )
    terp.drawString( housestr, 2, 90 )

    terp.color( 'red' )
    terp.place( -120, 100, 0 )
    terp.drawString( roofstr, 3, 90 )

    terp.color( (0.5, 0.4, 0.3 ) )

    for i in range(4):
        terp.color( (0.5+i*0.02, 0.4-i*0.02, 0.3+i*0.02 ) )
        terp.place( -350+i*60, -250+i*75, 90 )
        terp.drawString( tstr1, 10-i*2, 20 )
        terp.color( (0.5-i*0.02, 0.4+i*0.02, 0.3-i*0.02 ) )
        terp.place( 300-i*50, -250+i*75, 90 )
        terp.drawString( tstr2, 8-i*2, 33 )
        
    terp.hold()

if __name__ == "__main__":
    main( sys.argv )