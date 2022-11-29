# complex_shape.py
# Di Luo
# CS 151 Fall 2018
# Project 6: Animated Scene

import time
import graphicsPlus as gr

def draw( objlist, win ):
    """ Draw all of the objects in objlist in the window (win) """
    for i in objlist:
        i.draw(win)

def building_init(x, y, scale):
    '''Creates and returns a list of graphics objects to make up a building'''

    shapes = []

    r = gr.Rectangle( gr.Point(x-scale*50, y+scale*150), gr.Point(x+scale*50, y) )
    color = gr.color_rgb(200, 170, 150)
    r.setFill(color)
    shapes.append(r)

    r = gr.Rectangle( gr.Point(x-scale*40, y+scale*45), gr.Point(x-scale*10, y+scale*15) )
    color = gr.color_rgb(150, 170, 200)
    r.setFill(color)
    shapes.append(r)

    r = gr.Rectangle( gr.Point(x-scale*40, y+scale*90), gr.Point(x-scale*10, y+scale*60) )
    r.setFill(color)
    shapes.append(r)

    r = gr.Rectangle( gr.Point(x+scale*10, y+scale*45), gr.Point(x+scale*40, y+scale*15) )
    r.setFill(color)
    shapes.append(r)

    r = gr.Rectangle( gr.Point(x+scale*10, y+scale*90), gr.Point(x+scale*40, y+scale*60) )
    r.setFill(color)
    shapes.append(r)

    r = gr.Rectangle( gr.Point(x-scale*10, y+scale*150), gr.Point(x+scale*10, y+scale*105) )
    color = gr.color_rgb(175, 175, 175)
    r.setFill(color)
    shapes.append(r)

    return shapes

def car_init(x, y, scale):
    '''Creates and returns a list of graphics objects to make up a car'''

    shapes = []

    r = gr.Rectangle( gr.Point(x-scale*25, y), gr.Point(x+scale*25, y-scale*20) )
    color = gr.color_rgb(100, 100, 200)
    r.setFill(color)
    shapes.append(r)

    r = gr.Rectangle( gr.Point(x-scale*15, y-scale*20), gr.Point(x+scale*15, y-scale*40) )
    color = gr.color_rgb(150, 100, 200)
    r.setFill(color)
    shapes.append(r)

    c = gr.Circle( gr.Point(x-scale*10, y), 8*scale)
    color = gr.color_rgb(0, 0, 0)
    c.setFill(color)
    shapes.append(c)

    c = gr.Circle( gr.Point(x+scale*10, y), 8*scale)
    c.setFill(color)
    shapes.append(c)

    return shapes

def car_animate( shapes, frame_num, win ):
    '''given the car list, a frame number, and a window, it draws the car in the window for the given frame number'''
    
    p1 = shapes[0].getP1()
    p2 = shapes[0].getP2()
    dx = p2.getX() - p1.getX()
    
    for i in shapes:
        i.move(dx*0.1, 0)

def test_car():
    '''Create a window, draw the car into the window'''
    win = gr.GraphWin( 'Car', 400, 400, False )

    c1 = car_init( 100, 100, 1.0 )
    c2 = car_init( 150, 200, 1.5 )
    c3 = car_init( 200, 300, 2 )

    cars = [c1, c2, c3]

    for car in cars:
        draw( car, win )
    
    for frame_num in range(100):
        time.sleep( 0.25 )
        for car in cars:
            car_animate( car, frame_num, win,0 )
        win.update()
        if win.checkMouse():
            break

    win.getMouse()
    win.close()

def test_building():
    '''Create a window, draw the building into the window'''
    win = gr.GraphWin( 'Building', 600, 600, False )

    b1 = building_init( 100, 100, 1.0 )
    b2 = building_init( 300, 150, 1.2 )
    b3 = building_init( 500, 200, 1.4 )

    buildings = [b1, b2, b3]

    for building in buildings:
        draw( building, win )
    
    win.getMouse()
    win.close()

if __name__ == "__main__":
    test_car()
    test_building()