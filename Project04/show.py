# show.py
# Di Luo
# CS 151 Fall 2018
# Sept 27 2018
# Lab 4/Project 4: Images

import graphics
import display
import sys

def main(argv):
	'''main code, replace ???.ppm with the filename of the image that you want to check.'''
	
	#see if the length of argv is less than 2, if so print a usage statement
	if len(argv) < 2:
		print('python3 show.py ???.ppm')
		exit()
	img = graphics.Image( graphics.Point(0,0), argv[1] )
	win = display.displayImage( img, argv[1] )
	# display image ???.ppm until we get a mouse click
	win.getMouse()

# Make main() only be able to run on the command line
if __name__ == '__main__':
	main(sys.argv)