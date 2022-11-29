# extension.py
# Di Luo
# CS 151 Fall 2018
# Project 6: Animated Scene

import time
import random
import graphicsPlus as gr
import complex_shape as cs

def draw( objlist, win ):
    """ Draw all of the objects in objlist in the window (win) """
    for i in objlist:
        i.draw(win)

def move( objlist, dx, dy ):
    """ Draw all of the objects in objlist by dx in the x-direction
    and dy in the y-direction """
    for i in objlist:
        i.move(dx, dy)

def undraw( objlist ):
    """ Undraw all of the objects in objlist """
    for i in objlist:
        i.undraw()

def car_animate1( shapes, frame_num, win ):
    '''given the car list, a frame number, and a window, it draws the car in the window for the given frame number'''
    
    p1 = shapes[0].getP1()
    p2 = shapes[0].getP2()
    dx = p2.getX() - p1.getX()

    for i in shapes:
        i.move(-dx*0.1, 0)

def cloud_init(x, y, scale):
    '''Creates and returns a list of graphics objects to make up a cloud'''

    shapes = []

    r = gr.Rectangle( gr.Point(x-scale*15, y-scale*5), gr.Point(x+scale*15, y+scale*5) )
    color = gr.color_rgb(100, 100, 200)
    r.setFill(color)
    r.setOutline(color)
    shapes.append(r)

    c = gr.Circle( gr.Point(x-scale*15, y), 5*scale)
    c.setFill(color)
    c.setOutline(color)
    shapes.append(c)

    c = gr.Circle( gr.Point(x+scale*15, y), 5*scale)
    c.setFill(color)
    c.setOutline(color)
    shapes.append(c)

    c = gr.Circle( gr.Point(x-scale*10, y-scale*5), 5*scale)
    c.setFill(color)
    c.setOutline(color)
    shapes.append(c)

    c = gr.Circle( gr.Point(x, y-scale*5), 5*scale)
    c.setFill(color)
    c.setOutline(color)
    shapes.append(c)

    c = gr.Circle( gr.Point(x+scale*10, y-scale*5), 5*scale)
    c.setFill(color)
    c.setOutline(color)
    shapes.append(c)

    return shapes

def light_init(x, y, scale):
    '''Creates and returns a list of graphics objects to make up a traffic light'''

    shapes = []
    
    r = gr.Rectangle( gr.Point(x, y), gr.Point(x+scale*20, y-scale*100) )
    color = gr.color_rgb(150, 150, 150)
    r.setFill(color)
    shapes.append(r)

    p = gr.Polygon( gr.Point(x+scale*20, y-scale*100), gr.Point(x, y-scale*100), gr.Point(x-scale*50, y-scale*150), gr.Point(x-scale*30, y-scale*150) )
    color = gr.color_rgb(150, 150, 150)
    p.setFill(color)
    shapes.append(p)

    c = gr.Circle( gr.Point(x-scale*25, y-scale*125), 5*scale)
    color = gr.color_rgb(0, 255, 0)
    c.setFill(color)
    shapes.append(c)

    return shapes

def cloud_animate(cloud, frame_num, win, currDX):
    '''Moves the cloud along x direction (currDX)
    until it leaves the window, in which case we'll move it in the opposite
    direction
    '''
    xCent1 = cloud[1].getCenter().getX()-5
    xCent2 = cloud[2].getCenter().getX()+5
    # If the ball x coordinate out of bounds, reverse its DX
    if xCent1 < 0 or xCent2 > 800:
        currDX = -currDX
    
    for i in cloud:
        i.move(currDX, 0)

    return currDX

def light_animate(light, frame_num, win):
    color = gr.color_rgb(255, 0, 0)
    light[-1].setFill(color)

def smoke_animate(x, y, shapes, frame_num, win):

    shapes = []

    for i in range(2):
        # assign to c a new circle located at newx, newy with a radius of 0.4*dx
        c = gr.Circle(gr.Point(x, y), 0.4*dx)
        # use the setFill method of c to color the circle bright light yellow (250, 250, 200), you can add some randomness
        c.setFill(gr.color_rgb(100, 100, 100))
        # use the draw method of c to draw the circle into the window
        c.draw(win)
        # append to the shapes list the circle c
        shapes.append(c)
    # assign to count the value 4
    count = 4

    # for the remaining items in the shapes list (index 4 and above)
    for i in shapes:
        # assign to c the result of calling the getCenter method of item
        c = i.getCenter()
        # if the y value of c is less than the y value of p1 plus 5*dx
        if c.getY() < y + 50:
            # if count is even  (use the modulo operator to calculate this)
            if count % 2 == 0:
                # move the item in X by a small negative random amount and in Y by dx * 0.5
                i.move( random.randint(0, 3), -random.randint(0, 3) )
            #else
            else:
                # move the item in X by a small positive random amount and in Y by dx * 0.
                i.move( -random.randint(0, 3), -random.randint(0, 3) )
        # else
        else:
            # undraw the item
            i.undraw()
            # remove the shape from the shapes list using the pop method of shapes with the argument count
            shapes.pop(count)
            # decrement count by 1
            count -= 1
            
        # increment count
        count += 1
    
def main():
    '''Create a scene containing buildings and cars'''
    win = gr.GraphWin( 'Car', 800, 600, False )

    b1 = cs.building_init( 120, 200, 1.0 )
    b2 = cs.building_init( 250, 125, 1.5 )
    b3 = cs.building_init( 430, 50, 2 )

    buildings = [b1, b2, b3]

    for b in buildings:
        draw( b, win )

    c1 = cs.car_init( 50, 400, 1.0 )
    c2 = cs.car_init( 50, 550, 1.5 )
    c3 = cs.car_init( 700, 550, 2 )

    cars = [c1, c2]

    for c in cars:
        draw( c, win )
    draw(c3, win)
    
    cloud1 = cloud_init(400, 20, 1.0)
    cloud2 = cloud_init(100, 30, 1.4)
    cloud3 = cloud_init(700, 40, 1.2)

    clouds = [cloud1, cloud2, cloud3]

    for c in clouds:
        draw( c, win )
    
    light = light_init(600, 600, 1.0)
    draw (light, win)

    t = 0
    currDX = 20

    while True:   
        while t < 20:
            time.sleep(0.25)

            for car in cars:
                cs.car_animate( car, t, win )
            car_animate1( c3, t, win )
        
            for cloud in clouds:
                currDX = cloud_animate( cloud, t, win, currDX ) 
    
            t += 1
        
            win.update()
            if t == 20:
                light_animate(light, t, win)

        if win.checkMouse():
            break

    win.close()

if __name__ == "__main__":
    main()
