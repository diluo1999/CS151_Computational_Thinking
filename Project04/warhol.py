# warhol.py
# Di Luo
# CS 151 Fall 2018
# Project 4: The Warhol Project

import graphics
import display
import sys
import filter as f

def placeImage(dstImage, srcImage, x, y):
	'''Place srcImage into dstImage at the upper left at position(x, y)'''
	
	rows = srcImage.getHeight()
	cols = srcImage.getWidth()
	# Nested for loops
	for i in range(rows):
		for j in range(cols):
			(r,g,b) = srcImage.getPixel(j, i)
			dstImage.setPixel(x + j, y + i, graphics.color_rgb(r, g, b))

def main(argv):
	'''main code'''

	#see if the length of argv is less than 2, if so print a usage statement
	if len(argv) < 2:
		print('python3 warhol.py miller.ppm')
		exit()
	
	#create the collage image composed by four edited images under different filters
	img = graphics.Image(graphics.Point(0,0), argv[1])
	
	#make copies
	imgCopy1 = img.clone()
	imgCopy2 = img.clone()
	imgCopy3 = img.clone()
	imgCopy4 = img.clone()
	
	#change the copies with filters
	f.swapRedBlue(imgCopy1)
	f.grayScale(imgCopy2)
	f.setBlueAs0(imgCopy3)
	f.darker(imgCopy4)
	
	#place images
	collage = graphics.Image(graphics.Point(0, 0), 2*img.getWidth(), 2*img.getHeight())
	placeImage(collage, imgCopy1, 0, 0)
	placeImage(collage, imgCopy2, img.getWidth(), 0)
	placeImage(collage, imgCopy3, 0, img.getHeight())
	placeImage(collage, imgCopy4, img.getWidth(), img.getHeight())
	# save the new image to the file collage.ppm
	collage.save( 'collage.ppm' )
	print("Saved the new image to collage.ppm")
	
	'''For extension: Create a more complex Warhol style collage, and place images'''
	collage1 = graphics.Image(graphics.Point(0, 0), 5*img.getWidth(), 5*img.getHeight())
	placeImage(collage1, img, 2*img.getWidth(), 2*img.getHeight())
	placeImage(collage1, imgCopy1, 0, 0)
	placeImage(collage1, imgCopy1, img.getWidth(), img.getHeight())
	placeImage(collage1, imgCopy1, 0, 2*img.getHeight())
	placeImage(collage1, imgCopy2, 3*img.getWidth(), img.getHeight())
	placeImage(collage1, imgCopy2, 2*img.getWidth(), 0)
	placeImage(collage1, imgCopy2, 4*img.getWidth(), 0)
	placeImage(collage1, imgCopy3, 0, 4*img.getHeight())
	placeImage(collage1, imgCopy3, img.getWidth(), 3*img.getHeight())
	placeImage(collage1, imgCopy3, 2*img.getWidth(), 4*img.getHeight())
	placeImage(collage1, imgCopy4, 4*img.getWidth(), 2*img.getHeight())
	placeImage(collage1, imgCopy4, 4*img.getWidth(), 4*img.getHeight())
	placeImage(collage1, imgCopy4, 3*img.getWidth(), 3*img.getHeight())
	# save the new image to the file collage1.ppm
	collage1.save( 'collage1.ppm' )
	print("Saved the new image to collage1.ppm")
	
	'''For extension: Enable my Warhol program to read in multiple images from 
	the command line and make a collage for each one, 
	or a collage that integrates several images.'''
	#create collage2 if the length of argv equals to 6
	if len(argv) == 6:
		img2 = graphics.Image(graphics.Point(0,0), argv[2])
		img3 = graphics.Image(graphics.Point(0,0), argv[3])
		img4 = graphics.Image(graphics.Point(0,0), argv[4])
		img5 = graphics.Image(graphics.Point(0,0), argv[5])
		collage2 = graphics.Image(graphics.Point(0, 0), 2*img2.getWidth(), 2*img2.getHeight())
		placeImage(collage2, img2, 0, 0)
		placeImage(collage2, img3, img2.getWidth(), 0)
		placeImage(collage2, img4, 0, img2.getHeight())
		placeImage(collage2, img5, img2.getWidth(), img2.getHeight())
		# save the new image to the file collage2.ppm
		collage2.save( 'collage2.ppm' )
		print("Saved the new image to collage2.ppm")

# Make main() only be able to run on the command line
if __name__ == "__main__":
	main(sys.argv)
