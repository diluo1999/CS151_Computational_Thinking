'''task2.py
Di Luo
CS 151, Fall 2018
Sept. 25 2018
Project 3: Scenes within Scenes
'''

import turtle
import better_shapelib as bsl
import sys


def chairAndTable( x, y, scale, fill, color3 ):
	'''Draw chairs and tables at (x, y) of the given scale with a color of color3'''

	# Reset the direction of turtle to the North
	turtle.setheading(0)
	
	print('chairAndTable(): draw chairs and tables at (x, y) of the given scale with a color of color3')
	# Draw the first chair
	bsl.block( x, y, 20*scale, 100*scale, fill, color1 = color3 )
	bsl.block( x + 20*scale, y + 30*scale, 30*scale, 20*scale, fill, color1 = color3 )
	bsl.block( x + 50*scale, y, 20*scale, 50*scale, fill, color1 = color3 )
	# Draw the table
	bsl.block( x + 90*scale, y, 20*scale, 50*scale, fill, color1 = color3 )
	bsl.block( x + 110*scale, y + 30*scale, 60*scale, 20*scale, fill, color1 = color3 )
	bsl.block( x + 170*scale, y, 20*scale, 50*scale, fill, color1 = color3 )
	# Draw the second chair
	bsl.block( x + 210*scale, y, 20*scale, 50*scale, fill, color1 = color3 )
	bsl.block( x + 230*scale, y + 30*scale, 30*scale, 20*scale, fill, color1 = color3 )
	bsl.block( x + 260*scale, y, 20*scale, 100*scale, fill, color1 = color3 )
	
	
def gallery( x, y, scale, fill, color3 ):
	'''Draw the scene of gallery with the scece of 
	desert1 inside at ( x, y ) of the given scale. 
	And the color of the chairs and tables is color3'''
	
	# Reset the direction of turtle to the West
	turtle.setheading(0)
	
	print('gallery(): draw the scene of gallery with the scece of desert1 inside at ( x, y ) of the given scale')
	# Draw the black ground
	bsl.block( x - 500*scale, y - 500*scale, 1000*scale, 500*scale, fill, color1 = 'black' )
	# Draw the blue wall
	bsl.block( x - 500*scale, y, 1000*scale, 500*scale, fill, color1 = 'blue' )
	# Draw two groups of chairs and tables
	chairAndTable( x - 400*scale, y - 200*scale, 1*scale, fill, color3 )
	chairAndTable( x + 100*scale, y - 200*scale, 1.2*scale, fill, color3 )
	# Draw the frame of the paint
	bsl.block( x - 105*scale, y + 95*scale, 210*scale, 210*scale, fill, color1 = 'brown' )
	bsl.block( x - 100*scale, y + 100*scale, 200*scale, 200*scale, fill, color1 = 'white' )
	# Draw the paint of desert1
	bsl.desert1( x, y + 200*scale, 0.2*scale, fill )

def main():
	'''Make the color of chairs and tables as the color input from command line if there is a input,
	Otherwise set the color as 'brown'
	'''
	if len( sys.argv ) > 1:
		color3 = sys.argv[1]
	else:
		color3 = 'brown'
	# Fill color for the basic shapes
	fill = True
	# Speed up drawing
	turtle.speed(0)
	# Draw scene of gallery with the scene of desert1 inside
	gallery( 0, 0, 1, fill, color3 )
	
# Make task2.py only be able to run on the command line
if __name__ == '__main__':
	main()
	
	# Keep the scene up until the user clicks on the window
	turtle.exitonclick()
