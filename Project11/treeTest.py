# treeTest.py
# Di Luo
# CS 151 Fall 2018
# Project 11: 3D Scenes

import tree
import turtle_interpreter as it
import shapes
import random
import sys

def main( argv ):

    if len(argv) < 2:
        print('usage: %s <l-system file> <opt: iterations>' % (argv[0]))
        exit()

    iterations = 6
    if len(argv) > 2:
        iterations = int(argv[2])

    x = it.TurtleInterpreter()

    ld = tree.Tree( 10, filename = argv[1] )

    ld.setColor( (0.5, 0.4, 0.2) )
    ld.setWidth(2)
    ld.setIterations( iterations )
    ld.draw( 0, -200, scale=1.0, zpos=0)

    x.hold()

if __name__ == '__main__':
    main(sys.argv)
