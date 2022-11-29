'''extensions.py
Di Luo
CS 151, Fall 2018
Sept. 25 2018
Project 3: Scenes within Scenes
'''

import turtle
import better_shapelib as bsl
import task2 as t2
import sys
	
def gallery2( x, y, scale, fill, color3 ):
	'''Draw the scene of gallery with the scenes of 
	desert1 inside at ( x, y ) of the given scale. 
	And the color of the chairs and tables is color3'''
	
	# Reset the direction of turtle to the West
	turtle.setheading(0)
	
	print('gallery(): draw the scene of gallery with the sceces of desert1 and desert2 inside at ( x, y ) of the given scale')
	# Draw the black ground
	bsl.block( x - 500*scale, y - 500*scale, 1000*scale, 500*scale, fill, color1 = 'black' )
	# Draw the blue wall
	bsl.block( x - 500*scale, y, 1000*scale, 500*scale, fill, color1 = 'blue' )
	# Draw two groups of chairs and tables
	t2.chairAndTable( x - 400*scale, y - 200*scale, 1, fill, color3 )
	t2.chairAndTable( x + 100*scale, y - 200*scale, 1.2, fill, color3 )
	# Draw the frames of the paintings
	bsl.block( x - 305*scale, y + 95*scale, 210*scale, 210*scale, fill, color1 = 'brown' )
	bsl.block( x - 300*scale, y + 100*scale, 200*scale, 200*scale, fill, color1 = 'white' )
	bsl.block( x + 95*scale, y + 95*scale, 210*scale, 210*scale, fill, color1 = 'brown' )
	bsl.block( x + 100*scale, y + 100*scale, 200*scale, 200*scale, fill, color1 = 'white' )
	# Draw the painting of desert1
	bsl.desert1( x - 200*scale, y + 200*scale, 0.2*scale, fill )
	# Draw the painting of desert2
	bsl.desert2( x + 200*scale, y + 200*scale, 0.2*scale, fill )

def gallery3( x, y, scale, fill, color3 ):
	'''Draw the scene of gallery with the scenes of 
	desert1 inside at ( x, y ) of the given scale. 
	And the color of the chairs and tables is color3'''
	
	# Reset the direction of turtle to the West
	turtle.setheading(0)
	
	print('gallery(): draw the scene of gallery3 with the scece of gallery inside at ( x, y ) of the given scale')
	# Draw the black ground
	bsl.block( x - 500*scale, y - 500*scale, 1000*scale, 500*scale, fill, color1 = 'black' )
	# Draw the blue wall
	bsl.block( x - 500*scale, y, 1000*scale, 500*scale, fill, color1 = 'blue' )
	# Draw two groups of chairs and tables
	t2.chairAndTable( x - 400*scale, y - 200*scale, 1, fill, color3 )
	t2.chairAndTable( x + 100*scale, y - 200*scale, 1.2, fill, color3 )
	# Draw the frame of the paint
	bsl.block( x - 157.5*scale, y + 45*scale, 315*scale, 315*scale, fill, color1 = 'brown' )
	bsl.block( x - 150*scale, y + 50*scale, 300*scale, 300*scale, fill, color1 = 'white' )
	# Draw the paint of gallery
	t2.gallery( x, y + 200*scale, 0.3*scale, fill, color3)
	
def main():
	'''Make the color of chairs and tables as the color input from command line if there is a input,
	Otherwise set the color as 'brown'
	'''
	if len( sys.argv ) > 1:
		color3 = sys.argv[1]
	else:
		color3 = 'brown'
	
	# Determine if the scenes are filled on arguments from command line
	if len( sys.argv ) == 3:
		fill = False
	else:
		fill = True

	# Speed up drawing
	turtle.speed(0)
	# Draw scene of gallery2 with the scene of desert1 inside (delete the next line if run gallery3)
	gallery2( 0, 0, 1, fill, color3 )
	# Draw scene of gallery3 with the scene of gallery inside (delete the next line if run gallery2)
	gallery3( 0, 0, 1, fill, color3 )
	
# Make task2.py only be able to run on the command line
if __name__ == '__main__':
	main()
	
	# Keep the scene up until the user clicks on the window
	turtle.exitonclick()
