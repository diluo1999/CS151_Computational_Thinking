'''Create two desert scenes
Di Luo
CS 151, Fall 2018
September 18 2018
Project 2: A Shape Collection
'''

import shapelib
import turtle
import random

def desert1():
	'''Draw the first scene of desert which includes 
	the ground, a sun, stones, grasses, and cacti'''
	
	#Draw the background
	shapelib.ground()
	# Draw the sun
	shapelib.sun( 200, 200 )
	# Make 20 stones with random position in the ground
	for i in range(20):
		shapelib.stone( random.randint(-400, 400), 
		random.randint(-300, 0), random.randint(1, 5) )
	# Make 15 grasses with random position in the ground
	for i in range(15):
		shapelib.grass( random.randint(-400, 400), 
		random.randint(-300, 0), random.randint(1, 3) )
	# Make 10 cacti with random position in the ground
	for i in range(10):
		shapelib.cactus( random.randint(-400, 400), 
		random.randint(-300, 0), random.randint(1, 2) )

def desert2():
	'''Draw the second scene of desert which includes 
	the ground, the sky, a moon, stars, stones, grasses, 
	and cacti'''
	
	# Draw the background
	shapelib.ground()
	shapelib.sky()
	# Draw the moon
	shapelib.moon( 350, 200, 1 )
	# Make 20 stars with random position in the sky
	for i in range(20):
		shapelib.star( random.randint(-400, 300), 
		random.randint( 30, 300 ), random.randint(1, 3) )
	# Make 20 stones with random position in the ground
	for i in range(20):
		shapelib.stone( random.randint(-400, 400), 
		random.randint(-300, -20), random.randint(1, 5) )
	# Make 15 grasses with random position in the ground
	for i in range(15):
		shapelib.grass( random.randint(-400, 400), 
		random.randint(-300, -20), random.randint(1, 3) )
	# Make 15 cacti with random position in the ground
	for i in range(15):
		shapelib.cactus( random.randint(-400, 400), 
		random.randint(-300, -100), random.randint(1, 2) )


# Main code setup
# Speed up drawing
turtle.speed(0)
# Draw desert1
desert1()
# Draw desert2
desert2()
# Keep the scene up until the user clicks on the window
turtle.exitonclick()
