# collage.py
# Di Luo
# CS 151 Fall 2018
# Project 5: Cover Photos

import graphics
import filter
import sys

#variable for each of the picture parameters: filename, X offset, Y offset, filter, alpha, NoBkg and Image
IDXFilename = 0
IDXXoffset = 1
IDXYoffset = 2
IDXFilter = 3
IDXAlpha = 4
IDXMirror = 5
IDXScale2 = 6
IDXNoBkg = -2
IDXImage = -1


# reads in the files in the collage and stores the Image objects in the list
def readImages( cList ):
	
	print('Read in the files in the collage and stores the Image objects in the list')
	for picParams in cList:
		filename = picParams[IDXFilename]
		src = graphics.Image(graphics.Point(picParams[IDXXoffset],picParams[IDXYoffset]), filename)
		picParams[IDXImage] = src

#determine how big the background image should be to contain all the images
def getImageSize( cList ):
	
	print('Determine how big the background image should be to contain all the images')
	rows = 0
	cols = 0
	for picParams in cList:
		x0 = picParams[IDXXoffset]
		y0 = picParams[IDXYoffset]
		src = picParams[IDXImage]
		scale2 = picParams[IDXScale2]
		if scale2:
			dx = x0 + (picParams[IDXImage].getWidth())*2
			print('pic', picParams[IDXFilename], ' Width: ', (picParams[IDXImage].getWidth())*2)
		else:
			dx = x0 + picParams[IDXImage].getWidth()
			print('pic', picParams[IDXFilename], ' Width: ', picParams[IDXImage].getWidth())

		if dx > cols:
			cols = dx

		if scale2:
			dy = y0 + (picParams[IDXImage].getHeight())*2
			print('pic', picParams[IDXFilename], ' Height: ', (picParams[IDXImage].getHeight())*2)
		else:
			dy = y0 + picParams[IDXImage].getHeight()
			print('pic', picParams[IDXFilename], ' Height: ', picParams[IDXImage].getHeight())

		if dy > rows:
			rows = dy

	return cols, rows

#put each image that is modified by alpha bleed, filters and other elements into the background to create a collage
def buildCollage( cList ):
	
	print('put each image that is modified by alpha bleed, filters and other elements into the background to create a collage')
	cols, rows = getImageSize( cList )
	dst = graphics.Image(graphics.Point(0,0), cols, rows)
	for picParams in cList:
		x0 = picParams[IDXXoffset]
		y0 = picParams[IDXYoffset]
		operator = picParams[IDXFilter]
		alpha = picParams[IDXAlpha]
		noBkg = picParams[IDXNoBkg]
		mirror = picParams[IDXMirror]
		scale2 = picParams[IDXScale2]
		src = picParams[IDXImage]
		
		#check if the image needs to be mirrored
		width = src.getWidth()
		height = src.getHeight()
		if mirror:
			for i in range(int(height)):
				for j in range(int(width/2)):
					(r1, g1, b1) = src.getPixel(j, i)
					(r2, g2, b2) = src.getPixel(width-1-j, i)
					src.setPixel(width-1-j, i, graphics.color_rgb(r1, g1, b1))
					src.setPixel(j, i, graphics.color_rgb(r2, g2, b2))
		
		#pick specific effects for each image
		if operator == 'swapRGB':
			filter.swapRGB(src)
		elif operator == 'grayScale':
			filter.grayScale(src)
		elif operator == 'inverse':
			filter.inverse(src)
		elif operator == 'darker':
			filter.darker(src)
		
		#check if the image needs to have its green background being removed when placing in to the collage
		if noBkg:
			filter.placeImageNoBkg(dst, src, x0, y0, alpha, scale2)
		else:
			filter.placeImage(dst, src, x0, y0, alpha, scale2)

	return dst