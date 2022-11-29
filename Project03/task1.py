'''task1.py
Di Luo
CS 151, Fall 2018
Sept. 25 2018
Project 3: Scenes within Scenes
'''

import turtle
import better_shapelib as bsl

# Main code setup
# Fill color for the basic shapes
fill = True
# Speed up drawing
turtle.speed(0)
# Draw three desert1 in three different positions with different scales
bsl.desert1( -400, 0, 0.2, fill )
bsl.desert1( 0, 0, 0.25, fill )
bsl.desert1( 400, 0, 0.3, fill )
# Keep the scene up until the user clicks on the window
turtle.exitonclick()