from turtle import *

def ngon(x, sideLength):
	angle = 360/x
	for y in range(x):
		forward(sideLength)
		right(angle)

speed(20)

ngon(3, 40)
ngon(4, 40)
ngon(5, 40)
ngon(6, 40)
ngon(7, 40)

penup()
forward(200)
pendown()

ngon(3, 50)
ngon(4, 55)
ngon(5, 60)
ngon(6, 65)
ngon(7, 70)



input("Press Enter When Ready")