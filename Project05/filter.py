# filter.py
# Di Luo
# CS 151 Fall 2018
# Project 5: Cover Photos

import graphics

def swapRGB(src):
	'''In the image src, exchange the red, green, blue channels of each pixel'''

	print('exchange the red, green, blue channels')
	for row_idx in range(src.getHeight()):	
		for col_idx in range(src.getWidth()):
			(r, g, b) = src.getPixel(col_idx, row_idx)
			src.setPixel(col_idx, row_idx, graphics.color_rgb(b, r, g))

def grayScale(src):
	'''Extension: In the image src, convert each pixel from color to an appropriate shade of gray'''

	print('convert each pixel from color to an appropriate shade of gray')
	#Nested for loops
	for row_idx in range(src.getHeight()):	
		for col_idx in range(src.getWidth()):
			r, g, b = src.getPixel(col_idx, row_idx)
			gray_set = int(round(0.299*r + 0.587*g + 0.114*b))
			src.setPixel(col_idx, row_idx, graphics.color_rgb(gray_set, gray_set, gray_set))
			
def inverse(src):
	'''In the image src, change the three channels of each pixel from (r, g, b) to (255-r, 255-g, 255-b)'''

	print('change the three channels of each pixel from (r, g, b) to (255-r, 255-g, 255-b)')
	#Nested for loops
	for row_idx in range(src.getHeight()):	
		for col_idx in range(src.getWidth()):
			(r, g, b) = src.getPixel(col_idx, row_idx)
			(r, g, b) = (255-r, 255-g, 255-b)
			src.setPixel(col_idx, row_idx, graphics.color_rgb(r, 0, b))

def darker(src):
	'''In the image src, shrink the red, green, blue channels of each pixel to make the image darker'''

	print('change the red, green, blue channels of each pixel by different fraction')
	#Nested for loops
	for row_idx in range(src.getHeight()):	
		for col_idx in range(src.getWidth()):
			(r, g, b) = src.getPixel(col_idx, row_idx)
			(r, g, b) = (int(0.8*r), int(0.7*g), int(0.6*b))
			src.setPixel(col_idx, row_idx, graphics.color_rgb(r, g, b))

def placeImage(dstImage, srcImage, x, y, alpha, scale2):
	'''Place srcImage into dstImage at the upper left at position(x, y)'''
	
	print('place srcImage into dstImage at the upper left at position(x, y)')
	for i in range(srcImage.getHeight()):
		for j in range(srcImage.getWidth()):
			(r1, g1, b1) = srcImage.getPixel(j, i)
			(r2, g2, b2) = dstImage.getPixel(j+x, i+y)
			rnew = int(r1 * alpha + r2 * (1.0 - alpha))
			gnew = int(g1 * alpha + g2 * (1.0 - alpha))
			bnew = int(b1 * alpha + b2 * (1.0 - alpha))
			if scale2:
				dstImage.setPixel(2*j+x, 2*i+y, graphics.color_rgb(rnew, gnew, bnew))
				dstImage.setPixel(2*j+1+x, 2*i+y, graphics.color_rgb(rnew, gnew, bnew))
				dstImage.setPixel(2*j+x, 2*i+1+y, graphics.color_rgb(rnew, gnew, bnew))
				dstImage.setPixel(2*j+1+x, 2*i+1+y, graphics.color_rgb(rnew, gnew, bnew))
			else:
				dstImage.setPixel(j+x, i+y, graphics.color_rgb(rnew, gnew, bnew))

def placeImageNoBkg(dstImage, srcImage, x, y, alpha, scale2):
	'''Place srcImage without the green/blue background into dstImage at the upper left at position(x, y)'''

	print('place srcImage without the green/blue background into dstImage at the upper left at position(x, y)')
	for i in range(srcImage.getHeight()):
		for j in range(srcImage.getWidth()):
			(r1, g1, b1) = srcImage.getPixel(j, i)
			(r2, g2, b2) = dstImage.getPixel(j+x, i+y)
			(r0, g0, b0) = srcImage.getPixel(0, 0) 
			#check if the pixel is not the part of green/blue background
			if g0 > 2.3*r0:
				if g1 < 2.3*r1:
					rnew = int(r1 * alpha + r2 * (1.0 - alpha))
					gnew = int(g1 * alpha + g2 * (1.0 - alpha))
					bnew = int(b1 * alpha + b2 * (1.0 - alpha))
					if scale2:
						dstImage.setPixel(2*j+x, 2*i+y, graphics.color_rgb(rnew, gnew, bnew))
						dstImage.setPixel(2*j+1+x, 2*i+y, graphics.color_rgb(rnew, gnew, bnew))
						dstImage.setPixel(2*j+x, 2*i+1+y, graphics.color_rgb(rnew, gnew, bnew))
						dstImage.setPixel(2*j+1+x, 2*i+1+y, graphics.color_rgb(rnew, gnew, bnew))
					else:
						dstImage.setPixel(j+x, i+y, graphics.color_rgb(rnew, gnew, bnew))
			elif b0 > 2.3*r0:
				if b1 < 2.3*r1:
					rnew = int(r1 * alpha + r2 * (1.0 - alpha))
					gnew = int(g1 * alpha + g2 * (1.0 - alpha))
					bnew = int(b1 * alpha + b2 * (1.0 - alpha))
					if scale2:
						dstImage.setPixel(2*j+x, 2*i+y, graphics.color_rgb(rnew, gnew, bnew))
						dstImage.setPixel(2*j+1+x, 2*i+y, graphics.color_rgb(rnew, gnew, bnew))
						dstImage.setPixel(2*j+x, 2*i+1+y, graphics.color_rgb(rnew, gnew, bnew))
						dstImage.setPixel(2*j+1+x, 2*i+1+y, graphics.color_rgb(rnew, gnew, bnew))
					else:
						dstImage.setPixel(j+x, i+y, graphics.color_rgb(rnew, gnew, bnew))
