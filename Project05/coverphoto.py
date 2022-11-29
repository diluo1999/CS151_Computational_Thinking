# coverphoto.py
# Di Luo
# CS 151 Fall 2018
# Project 5: Cover Photos

import graphics
import sys
import filter
import collage
import random

# main function
def main(argv):

	if len(argv) < 4:
		print( 'Usage: coverphoto.py <ppm image 1> <ppm image 2> <ppm image 3>' )
		print( '\n		 Reads in the three images and builds a collage')
		print( '	   using an alpha blend of 0.6')
		print( '\n		 The output image is called coverphoto.ppm')
		print("\n")
		exit()
	
	filters = ['swapRGB', 'grayScale', 'original', 'inverse', 'darker']
	oneFilter1 = random.choice(filters)
	oneFilter2 = random.choice(filters)
	oneFilter3 = random.choice(filters)
	
	# create the collage list with the three images
	cList = [
			[ argv[1], 0, 0, oneFilter1, 0.6, False, False, False, None ],
			[ argv[2], 500, 0, oneFilter2, 0.6, True, False, False, None ],
			[ argv[3], 250, 0, oneFilter3, 0.6, False, False, False, None ]
			]

	# call readImages
	collage.readImages( cList )
	
	# call buildCollage
	dst = collage.buildCollage( cList )

	# save the image
	print("Writing coverphoto.ppm")
	dst.save( 'coverphoto.ppm' )

if __name__ == "__main__":
	main( sys.argv )
