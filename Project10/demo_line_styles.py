# demo_line_styles.py
# Di Luo
# CS 151 Fall 2018
# Project 10: Non-Photorealistic Rendering

import turtle_interpreter as ti
import shapes

'''
Draw four groups of rhombus, each group has two rhombi 
and the four group use the style 'normal', 'jitter', 
'jitter3' and 'dotted' respectively. In each group the
width, jitterSigma or dotSize is different.
'''

r = shapes.Rhombus(60)

r.setStyle('normal')
r.draw(-300, 100)
r.setWidth(2)
r.draw(-200, 100)
r.setWidth(1)

r.setStyle('jitter')
r.draw(-50, 100)
r.setJitter(4)
r.draw(50, 100)
r.setJitter(2)

r.setStyle('jitter3')
r.draw(-300, -100)
r.setJitter(4)
r.draw(-200, -100)
r.setJitter(2)

r.setStyle('dotted')
r.draw(-50, -100)
r.setDotSize(4)
r.draw(50, -100)

#extensions
r.setStyle('angledLines')
r.draw(200, -100)
r.setLineSize(10)
r.draw(300, -100)

r.setStyle('brush')
r.setColor('green')
r.draw(200, 100)
r.setWidth(3)
r.draw(300, 100)

ti.TurtleInterpreter().hold()