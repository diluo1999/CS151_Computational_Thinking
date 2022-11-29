'''better_shapelib.py
Di Luo
CS 151, Fall 2018
Sept. 25 2018
Project 3: Scenes within Scenes
'''

import turtle
import random

def goto( x, y ):
	'''Move the turtle to the position (x, y)'''
	
	print('goto(): going to', x, y)
	turtle.up()
	turtle.goto( x, y )
	turtle.down()

def block( x, y, width, height, fill, color1 = 'green' ):
	'''Draws a block with color of color1 at (x, y) of the given width and height'''
	
	goto( x, y )
	
	# Reset the direction of turtle to the West
	turtle.setheading(0)

	print('block(): drawing color1 block of the width', width, 'the height', height)
	# If fill = True, draw block with color; if fill = False, draw block without color
	if fill:
		turtle.color( color1 )
		turtle.begin_fill()
	# Use for loop to repeat the motion of drawing one width and one height twice to get a block
	for i in range(2):
		turtle.forward( width )
		turtle.left(90)
		turtle.forward( height )
		turtle.left(90)
	if fill:
		turtle.end_fill()

def triangle( x, y, sideLength, fill, color2 = 'brown' ):
	'''Draws a triangle with a color of color2 at (x, y) of the given side length'''
	
	goto( x, y )
	
	# Reset the direction of turtle to the West
	turtle.setheading(0)
	
	print('triangle(): drawing color2 triangle of the side length', sideLength)
	# If fill = True, draw triangle with color; if fill = False, draw triangle without color
	if fill:
		turtle.color( color2 )
		turtle.begin_fill()
	# Use for loop to draw a side of triangle three times to get a triangle
	for i in range(3):
		turtle.forward( sideLength )
		turtle.left(120)
	if fill:
		turtle.end_fill()

def sun( x, y, scale, fill, suncolor = 'red' ):
	'''Draw a circle with color of suncolor at ( x, y ) with given scale as the sun'''
	goto( x, y )

	# Reset the direction of turtle to the West
	turtle.setheading(0)
	
	print('sun(): drawing a red circle at ( x, y ) with a radius of 50*scale as the sun')
	# If fill = True, draw circle with color; if fill = False, draw circle without color
	if fill:
		turtle.color( suncolor )
		turtle.begin_fill()
	# Draw the circle
	turtle.circle( 50*scale )
	if fill:
		turtle.end_fill()

def cactus( x, y, scale, fill ):
	'''Draws a cactus combined with five color1 blocks at (x, y) of the given scale'''
	goto( x, y )
	
	print('cactus(): drawing green cactus of scale', scale)
	# Draw five blocks to create a cactus and add colors for each of them
	block( x, y, 10*scale , 50*scale, fill )
	block( x+10*scale, y+15*scale, 20*scale , 5*scale, fill )
	block( x+20*scale, y+20*scale, 10*scale , 20*scale, fill )
	block( x-15*scale, y+20*scale, 15*scale , 5*scale, fill )
	block( x-15*scale, y+25*scale, 10*scale , 20*scale, fill )
	
def stone( x, y, scale, fill ):
	'''Draws a stone that is combined with two color2 triangles at (x, y) of the given scale'''
	goto( x, y )
	
	print('stone(): drawing brown stone of scale', scale)
	# Draw two brown triangles
	triangle( x, y, 10*scale, fill )
	triangle( x+5*scale, y, 10*scale, fill )

def ground( x, y, scale, fill ):
	'''Draw an orange block at ( x - 500*scale, y - 500*scale ) with given width and length
	to represent the ground with the color of orange'''
	
	print('ground(): drawing the orange block representing the ground')
	# Draw the block
	block( x - 500*scale, y - 500*scale, 1000*scale, 500*scale, fill, color1 = 'orange' )

def desert1( x, y, scale, fill ):
	'''Draw the first scene of desert at ( x, y ) of a given scale which includes 
	the ground, a sun, stones, and cacti'''
	
	print('desert1(): draw the first scene of desert at ( x, y ) of a given scale')
	# Draw the ground
	ground( x, y, scale, fill )
	# Draw the sun
	sun( x + 200*scale, y + 200*scale, scale, fill )
	# Make 10 stones with random position in the ground
	for i in range(10):
		stone( random.randint( x - 400*scale, x + 400*scale ), 
		random.randint( y - 300*scale, y ), random.randint(1, 5)*scale , fill )
	# Make 5 cacti with random position in the ground
	for i in range(5):
		cactus( random.randint( x - 400*scale, x + 400*scale ), 
		random.randint( y - 300*scale, y), random.randint(1, 2)*scale, fill )
		
def sky( x, y, scale, fill ):
	'''Draw an black block at ( x - 500*scale, y ) with given width and length
	to represent the sky with the color of black'''
	
	print('ground(): drawing the black block representing the ground')
	# Draw the block
	block( x - 500*scale, y , 1000*scale, 500*scale, fill, color1 = 'black' )

def star( x, y, scale, fill, starcolor = 'yellow' ):
	'''Draw a yellow star at (x, y) of give scale'''
	goto( x, y )

	# Reset the direction of turtle to the West
	turtle.setheading(0)

	print('star(): drawing a yellow star of scale', scale)
	# If fill = True, draw star with color; if fill = False, draw star without color
	if fill:
		turtle.color( starcolor )
		turtle.begin_fill()
	# Create loop to draw 5 angles of a star to create a star
	for i in range(5):
		turtle.forward(10*scale)
		turtle.right(144)
		turtle.forward(10*scale)
		turtle.left(72)
	if fill:
		turtle.end_fill()
		
def desert2( x, y, scale, fill ):
	'''Draw the second scene of desert at ( x, y ) of a given scale which includes 
	the ground, a sun, stones, and cacti'''
	
	print('desert2(): draw the second scene of desert at ( x, y ) of a given scale')
	# Draw the ground and the sky
	ground( x, y, scale, fill )
	sky( x, y, scale, fill )
	# Make 10 stones with random position in the ground
	for i in range(10):
		stone( random.randint( x - 400*scale, x + 400*scale ), 
		random.randint( y - 300*scale, y ), random.randint(1, 5)*scale , fill )
	# Make 5 cacti with random position in the ground
	for i in range(5):
		cactus( random.randint( x - 400*scale, x + 400*scale ), 
		random.randint( y - 300*scale, y), random.randint(1, 2)*scale, fill )
	# Make 20 stars with random position in the sky
	for i in range(10):
		star( random.randint( x - 400*scale, x + 300*scale ), 
		random.randint( y + 30*scale, y+ 300*scale ), random.randint(1, 3)*scale, fill )