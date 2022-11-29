# tree.py
# Di Luo
# CS 151 Fall 2018
# Project 11: 3D Scenes

import sys
import shapes as s
import lsystem
import turtle_interpreter as ti

class Tree(s.Shape):
    def __init__(self, distance=5, angle=22.5, color=(0.5, 0.4, 0.3), iterations=3, filename=None):
        '''Initialize the Tree class as the child class of Shape'''
        s.Shape.__init__(self, distance, angle, color)
        self.iterations = iterations
        self.lsystem = lsystem.Lsystem(filename)

    def setIterations(self, iterations):
        '''Set iterations field to iterations'''
        self.iterations = iterations
    
    def read(self, filename):
        '''run the read method in lsystem field with parameter filename'''
        self.lsystem.read(filename)

    def draw(self, xpos, ypos, scale=1.0, orientation=90, pitch=0, roll=0, zpos=0):
        '''build the Lsystem string and draw the tree'''
        tstr = self.lsystem.buildString(self.iterations)
        self.string = tstr
        s.Shape.draw(self, xpos, ypos, scale, orientation, pitch, roll, zpos)