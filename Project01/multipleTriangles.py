from turtle import *

def triangle():
	forward(10)
	left(120)
	forward(10)
	left(120)
	forward(10)
	left(120)

triangle()

input("Press Enter When Ready")

penup()
forward(100)
pendown()

def biggerTriangle():
	triangle()
	penup()
	forward(10)
	pendown()
	triangle()
	penup()
	left(120)
	forward(10)
	right(120)
	pendown()
	triangle()

biggerTriangle()

input("Press Enter When Ready")

penup()
forward(100)
pendown()

def multipleTriangles():
	biggerTriangle()
	penup()
	right(60)
	forward(10)
	left(60)
	forward(10)
	pendown()
	biggerTriangle()
	penup()
	backward(10)
	left(120)
	forward(10)
	right(120)
	pendown()
	biggerTriangle()

multipleTriangles()

input("Press Enter When Ready")