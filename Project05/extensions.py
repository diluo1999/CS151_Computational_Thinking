# extensions.py
# Di Luo
# CS 151 Fall 2018
# Project 5: Cover Photos

import graphics
import sys
import filter
import collage
import random

def main(argv):

	if len(argv) < 5:
		print( 'Usage: coverphoto.py <ppm image 1> <ppm image 2> <ppm image 3> <ppm image 4>' )
		print( '\n		 Reads in the four images and builds a collage')
		print( '	   using an alpha blend of 0.6')
		print( '\n		 The output image is called triangle.ppm')
		print("\n")
		exit()
	
	filters = ['swapRGB', 'grayScale', 'original', 'inverse', 'darker']
	oneFilter1 = random.choice(filters)
	oneFilter2 = random.choice(filters)
	oneFilter3 = random.choice(filters)
	
	# create the collage list with the five images
	cList = [
			[ argv[1], 0, 0, oneFilter1, 0.6, True, True, False, None ],
			[ argv[2], 0, 0, oneFilter2, 0.6, True, True, False, None ],
			[ argv[3], 0, 0, oneFilter3, 0.6, True, True, False, None ],
			[ argv[4], 0, 0, 'original', 0.6, True, False, True, None],
			[ argv[4], 0, 0, 'original', 0.6, False, True, True, None]
			]

	# call readImages
	collage.readImages( cList )
	
	dynHeight = cList[0][-1].getHeight()*2
	dynWidth = cList[0][-1].getWidth()*2
	cList[0][1] = int(dynWidth/2)
	cList[1][2] = dynHeight
	cList[2][1] = dynWidth
	cList[2][2] = dynHeight
	cList[3][2] = dynHeight
	cList[3][1] = int(dynWidth/2)
	cList[4][2] = int(dynHeight/2)
	cList[4][1] = int(dynWidth/2)

	collage.readImages( cList )
	
	# call buildCollage
	dst = collage.buildCollage( cList )

	# save the image
	print("Writing triangle.ppm")
	dst.save( 'triangle.ppm' )

if __name__ == "__main__":
	main( sys.argv )

