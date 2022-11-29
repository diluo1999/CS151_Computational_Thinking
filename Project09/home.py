# home.py
# Di Luo
# CS 151 Fall 2018
# Project 9: Unique Trees and Shapes
# Version 1

import sys
import shapes as s
import lsystem
import turtle_interpreter as ti
import tree as tr

def main(argv):
    '''create a scene near my home with Lsystem tree and other shapes with classes'''

    if len(argv) < 2:
        print('Usage: home.py systemJ.txt system1.txt system2.txt')
        exit()
    
    tree = tr.Tree(iterations = 5, filename = argv[1] )
    tree.draw(-100, 0)
    tree.draw(-200, 0)
    tree.draw(100, 0)
    tree.draw(200, 0)

    square = s.Square(distance=100, color=(0, 0, 0), fill=True)
    triangle = s.Triangle(distance=100, color='red', fill=True)
    star = s.Star(distance=100, color='yellow', fill=True)

    square.draw(-50, 100)
    triangle.draw(75, 100, 1.5, 180)
    star.draw(-25, 150, 0.5)
    square.setColor('brown')
    square.setDistance(25)
    square.setString('{F-FF-F-FF-}')
    square.draw(-13, 50)

    # extension
    tree1 = tr.Tree(iterations=3, filename=argv[2])
    tree2 = tr.Tree(iterations=4, filename=argv[3])
    tree1.draw(-300, -200)
    tree1.draw(-200, -200)
    tree1.draw(-100, -200)
    tree2.draw(100, -200)
    tree2.draw(200, -200)
    tree2.draw(300, -200)

    ti.TurtleInterpreter().hold()

if __name__ == '__main__':
    main(sys.argv)
