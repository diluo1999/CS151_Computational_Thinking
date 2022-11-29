'''Create two desert scenes
Di Luo
CS 151, Fall 2018
September 18 2018
Project 2: A Shape Collection
'''

import turtle
import random

def goto( x, y ):
	'''Move the turtle to the position (x, y)'''
	
	print('goto(): going to', x, y)
	turtle.up()
	turtle.goto( x, y )
	turtle.down()

def block( x, y, width, height ):
	'''Draws a block at (x, y) of the given width and height'''
	
	goto( x, y )

	print('block(): drawing block of the width', width, 'the height', height)
	# Draw block
	turtle.forward( width )
	turtle.left(90)
	turtle.forward( height )
	turtle.left(90)
	turtle.forward( width )
	turtle.left(90)
	turtle.forward( height )
	turtle.left(90)
	
def triangle( x, y, sideLength ):
	'''Draws a triangle at (x, y) of the given side length'''
	
	goto( x, y )
	
	print('triangle(): drawing triangle of the side length', sideLength)
	# Draw triangle
	turtle.forward( sideLength )
	turtle.left(120)
	turtle.forward( sideLength )
	turtle.left(120)
	turtle.forward( sideLength )
	turtle.left(120)

def cactus( x, y, scale ):
	'''Draws a green cactus with dark green outline that is combined 
	with five triangles at (x, y) of the given scale'''
	goto( x, y )

	# Reset the direction of turtle to the West
	turtle.setheading(0)
	
	print('cactus(): drawing green cactus of scale', scale)
	# Define colors
	turtle.color('dark green', 'green')
	# Draw five blocks to create a cactus and add colors for each of them
	turtle.begin_fill()
	block( x, y, 10*scale , 50*scale )
	turtle.end_fill()
	turtle.begin_fill()
	block( x+10*scale, y+15*scale, 20*scale , 5*scale )
	turtle.end_fill()
	turtle.begin_fill()
	block( x+20*scale, y+20*scale, 10*scale , 20*scale )
	turtle.end_fill()
	turtle.begin_fill()
	block( x-15*scale, y+20*scale, 15*scale , 5*scale )
	turtle.end_fill()
	turtle.begin_fill()
	block( x-15*scale, y+25*scale, 10*scale , 20*scale )
	turtle.end_fill()
	
def stone( x, y, scale ):
	'''Draws a brown stone that is combined with 
	two triangles at (x, y) of the given scale'''
	goto( x, y )

	# Reset the direction of turtle to the West
	turtle.setheading(0)
	
	print('stone(): drawing brown stone of scale', scale)
	# Define colors
	turtle.color('brown', 'brown')
	# Draw two triangles and add color for each of them
	turtle.begin_fill()
	triangle( x, y, 10*scale )
	turtle.end_fill()
	turtle.begin_fill()
	triangle( x+5*scale, y, 10*scale )
	turtle.end_fill()
	
def rhombus1( x, y, sideLength ):
	'''Draws a rhombus at (x, y) of the given side length'''
	
	goto( x, y )
	
	print('rhombus(): drawing rhombus1 of side length', sideLength)
	# Draw rhombus1
	turtle.forward( sideLength )
	turtle.left(30)
	turtle.forward( sideLength )
	turtle.left(150)
	turtle.forward( sideLength )
	turtle.left(30)
	turtle.forward( sideLength )
	turtle.left(150)

def rhombus2( x, y, sideLength ):
	'''Draws another rhombus that is symmetrical to 
	rhombus1 at (x, y) of the given side length'''
	
	goto( x, y )
	
	print('rhombus2(): drawing rhombus2 of side lenght', sideLength)
	# Draw rhombus2
	turtle.forward( sideLength )
	turtle.right(30)
	turtle.forward( sideLength )
	turtle.right(150)
	turtle.forward( sideLength )
	turtle.right(30)
	turtle.forward( sideLength )
	turtle.right(150)

def moon( x, y, scale ):
	'''Draws a yellow moon with gold outline that is combined 
	with a block and two rhombuses at (x, y) of the given scale'''
	goto( x, y )

	# Reset the direction of turtle to the West
	turtle.setheading(0)
	
	print('moon(): drawing yellow moon of scale', scale)
	# Define colors
	turtle.color( 'gold', 'yellow' )
	turtle.begin_fill()
	# Draw shapes for moon
	block( x, y, 25*scale , 50*scale )
	rhombus1( x, y+50*scale, 25*scale )
	rhombus2( x, y, 25*scale )
	turtle.end_fill()
	
def grass( x, y, scale ):
	'''Draws a spring green grass that is combined with 
	five to ten lines at (x, y) of the given scale'''
	goto( x, y )

	# Reset the direction of turtle to the West
	turtle.setheading(0)
	
	print('grass(): drawing spring green grass combined with n lines of scale', scale)
	# Define colors
	turtle.color('spring green')
	turtle.begin_fill()
	# Use random to make n (loop index) a integral variable varying from 5 to 10
	n = random.randint(5,10)
	# Create loop to draw n equallong lines which separate 180 degree into equally n+1 part to create a grass
	for i in range(n):
		turtle.left(180/(n+1))
		turtle.forward(10*scale)
		turtle.back(10*scale)
	turtle.end_fill()
		
def sun( x, y ):
	'''Draw a red circle with orange red outline at 
	(x, y) with a radius of 50 as the sun'''
	goto( x, y )

	# Reset the direction of turtle to the West
	turtle.setheading(0)
	
	print('sun(): drawing a red circle with a radius of 50 as the sun')
	# Define colors
	turtle.color('orange red', 'red')
	turtle.begin_fill()
	# Draw the circle
	turtle.circle(50)
	turtle.end_fill()
	
def star( x, y, scale ):
	'''Draw a yellow star at (x, y) of give scale'''
	goto( x, y )

	# Reset the direction of turtle to the West
	turtle.setheading(0)

	print('star(): drawing a yellow star of scale', scale)
	# Define colors
	turtle.color('yellow', 'yellow')
	turtle.begin_fill()
	# Create loop to draw 5 angles of a star to create a star
	for i in range(5):
		turtle.forward(10*scale)
		turtle.right(144)
		turtle.forward(10*scale)
		turtle.left(72)
	turtle.end_fill()
		
def ground():
	'''Draw an orange block at (-500, -500) with given width and length
	to represent the ground with the color of orange'''

	print('ground(): drawing the orange block representing the ground')
	# Define colors
	turtle.color('orange', 'orange')
	turtle.begin_fill()
	# Draw the block
	block( -500, -500, 1000, 500 )
	turtle.end_fill()

def sky():
	'''Draw a black block at (-500, 0) with given width and length
	to represent the sky with the color of black'''
	
	print('sky(): drawing the black block representing the sky')
	# Define colors
	turtle.color('black', 'black')
	turtle.begin_fill()
	# Draw the block
	block( -500, 0, 1000, 500 )
	turtle.end_fill()	
