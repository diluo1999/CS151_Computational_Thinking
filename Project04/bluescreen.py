# bluescreen.py
# Di Luo
# CS 151 Fall 2018
# Project 4: The Warhol Project

import graphics
import display
import sys

def turnBlue(src):
	'''In the image src, convert any pixel that is green/very green to blue in order to change the background to blue'''
	for row_idx in range(src.getHeight()):	
		for col_idx in range(src.getWidth()):
			(r,g,b) = src.getPixel(col_idx, row_idx)
			#check if the pixel is green
			if g > 2.3*r and g > b:
				src.setPixel(col_idx, row_idx, graphics.color_rgb(0, 0, 255))

def placeImageWithoutGreen(dstImage, srcImage, x, y):
	'''For extension: Place the part of srcImage that is not green into dstImage at the upper left at position(x, y)'''
	
	rows = srcImage.getHeight()
	cols = srcImage.getWidth()
	for i in range(rows):
		for j in range(cols):
			(r,g,b) = srcImage.getPixel(j, i)
			#check if the pixel is not green
			if g < 2.3*r:
				dstImage.setPixel(x + j, y + i, graphics.color_rgb(r, g, b))

def main(argv):
	'''main code'''
	
	#see if the length of argv is less than 2, if so print a usage statement
	if len(argv) < 2:
		print('python3 bluecreen.py greenDi.ppm')
		exit()

	#change the background from green to blue
	img = graphics.Image(graphics.Point(0,0), argv[1])
	turnBlue(img)
	# save the new image to the file blueDi.ppm
	img.save( 'blueDi.ppm' )
	print("Saved the new image to blueDi.ppm")

	'''For extension: put myself in a scene'''
	#put myself in a scene if the length of argv is three
	if len(argv) == 3:
		scene = graphics.Image(graphics.Point(0,0), argv[2])
		placeImageWithoutGreen(scene, img, 0, 0)
		# save the new image to the file sceneWithDi.ppm
		scene.save( 'sceneWithDi.ppm' )
		print("Saved the new image to sceneWithDi.ppm")

# Make main() only be able to run on the command line
if __name__ == '__main__':
	main(sys.argv)
