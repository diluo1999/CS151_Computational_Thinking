# Bruce Maxwell
# spring 2013
# lsystem and interpreter class test function

import sys
import random
import turtle_interpreter
import lsystem

def main(argv):
    """
    Test the ability of the TurtleInterpreter to draw trees.
    The program expects the name of an L-system filename and then
    draws several trees in the screen, using 3-5 iterations
    of the rule to generate the string.
    If the TurtleInterpreter draws leaves using the L symbol, then
    the program also draws piles of leaves at the base of each tree.
    """

    if len(argv) < 2:
        print('usage: %s <lsystem file 1>' % (argv[0]) )
        exit()

    tree = lsystem.Lsystem( argv[1] )

    sx = 800
    sy = 450
    terp = turtle_interpreter.TurtleInterpreter(sx, sy)

    N = 10

    for i in range( N ):
        x0 = -sx/3 + i*0.75*sx/(N+1) + random.randint( -sx//(3*N), sx//(3*N) )
        y0 = -sy/4 + random.randint( -sy//20, sy//20 )

        tstr = tree.buildString( random.randint(3, 5) )

        terp.color( (0.5, 0.4, 0.3 ) )
        terp.place( x0, y0, random.randint( 85, 95 ) )
        terp.drawString( tstr, random.randint( 3, 6 ), random.randint( 18, 30 ) * random.choice( [1, -1] ) )

        for j in range( random.randint(20, 40) ):
            terp.color( (random.random(), random.random(), 0.1) )
            terp.place( x0 + random.gauss( 0, 40 ), y0 + random.gauss( 0, 5 ), random.randint(0, 360) )
            terp.drawString( 'L', random.randint( 3, 5 ), 90 )

    terp.hold()


if __name__ == "__main__":
    main( sys.argv )
