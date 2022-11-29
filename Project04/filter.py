# filter.py
# Di Luo
# CS 151 Fall 2018
# Project 4: The Warhol Project

import graphics
import display
import sys

def swapRedBlue(src):
	'''In the image src, exchange the red channel of each pixel with the blue channel'''
	
	print('exchange the red channel with the blue channel')
	for row_idx in range(src.getHeight()):	
		for col_idx in range(src.getWidth()):
			(r, g, b) = src.getPixel(col_idx, row_idx)
			src.setPixel(col_idx, row_idx, graphics.color_rgb(b, g, r))

def grayScale(src):
	'''Extension: In the image src, convert each pixel from color to an appropriate shade of gray'''
	
	print('convert each pixel from color to an appropriate shade of gray')
	#Nested for loops
	for row_idx in range(src.getHeight()):	
		for col_idx in range(src.getWidth()):
			r, g, b = src.getPixel(col_idx, row_idx)
			gray_set = int(round(0.299*r + 0.587*g + 0.114*b))
			src.setPixel(col_idx, row_idx, graphics.color_rgb(gray_set, gray_set, gray_set))
			
def setBlueAs0(src):
	'''In the image src, change the blue channel of each pixel to 0'''
	
	print('change the blue channel of all the pixels to 0')
	#Nested for loops
	for row_idx in range(src.getHeight()):	
		for col_idx in range(src.getWidth()):
			(r, g, b) = src.getPixel(col_idx, row_idx)
			src.setPixel(col_idx, row_idx, graphics.color_rgb(r, g, 0))

def darker(src):
	'''In the image src, change the red, green, blue channels of each pixel by half to make the image darker'''
	
	print('change the red, green, blue channels of each pixel by half')
	#Nested for loops
	for row_idx in range(src.getHeight()):	
		for col_idx in range(src.getWidth()):
			(r, g, b) = src.getPixel(col_idx, row_idx)
			(r, g, b) = (int(0.5*r), int(0.5*g), int(0.5*b))
			src.setPixel(col_idx, row_idx, graphics.color_rgb(r, g, b))
