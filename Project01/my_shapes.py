#shapeThree
from turtle import *

def cross():
	left(30)
	forward(100)
	penup()
	right(120)
	forward(50)
	pendown()
	right(120)
	forward(100)

def box():
	forward(100)
	left(90)
	forward(57.8)
	left(90)
	forward(100)
	left(90)
	forward(57.8)

box()
left(120)
penup()
forward(7.8)
pendown()
right(30)
cross()

input("Press Enter When Ready")

penup()
forward(200)
pendown()

#shapeFour

def square(sideLength):
	forward(sideLength)
	left(90)
	forward(sideLength)
	left(90)
	forward(sideLength)
	left(90)	
	forward(sideLength)

square(50)

input("Press Enter When Ready")

#shapeFive

square(75)
square(100)
square(125)

input("Press Enter When Ready")


