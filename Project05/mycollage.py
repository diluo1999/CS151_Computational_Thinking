# mycollage.py
# Di Luo
# CS 151 Fall 2018
# Project 5: Cover Photos

import sys
import graphics
import collage

# main function
def main(argv):
	if len(argv) < 7:
		print( 'Usage: mycollage.py <ppm image 1> <ppm image 2> <ppm image 3> <ppm image 4> <ppm image 5> <ppm image 6>' )
		print( '\n		 Reads in the six images and builds a collage')
		print( '	   using an alpha blend of 0.8')
		print( '\n		 The output image is called mycollage.ppm')
		print("\n")
		exit()

	# create the collage list with the six images
	cList = [
			[ argv[1], 0, 0, 'swapRGB', 0.8, False, False, False, None ],
			[ argv[2], 400, 0, 'grayScale', 0.8, True, False, False, None ],
			[ argv[3], 0, 300, 'inverse', 0.8, False, False, False, None ],
			[ argv[5], 400, 300, 'darker', 0.8, False, False, False, None ],
			[ argv[4], 400, 150, 'original', 0.5, False, False, False, None ],
			[ argv[6], 0, 150, 'original', 0.8, True, False, True, None ]
			]

	# call readImages
	collage.readImages( cList )
	
	# call buildCollage
	dst = collage.buildCollage( cList )

	# save the image
	print("Writing mycollage.ppm")
	dst.save( 'mycollage.ppm' )

if __name__ == '__main__':
	main(sys.argv)