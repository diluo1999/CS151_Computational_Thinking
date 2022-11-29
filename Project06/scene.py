# scene.py
# Di Luo
# CS 151 Fall 2018
# Project 6: Animated Scene

import time
import graphicsPlus as gr
import complex_shape as cs

def main():
    '''Create a scene containing buildings and cars'''
    win = gr.GraphWin( 'Car', 600, 600, False )

    b1 = cs.building_init( 120, 200, 1.0 )
    b2 = cs.building_init( 250, 125, 1.5 )
    b3 = cs.building_init( 430, 50, 2 )

    buildings = [b1, b2, b3]

    for building in buildings:
        cs.draw( building, win )

    c1 = cs.car_init( 50, 400, 1.0 )
    c2 = cs.car_init( 50, 450, 1.5 )
    c3 = cs.car_init( 50, 550, 2 )

    cars = [c1, c2, c3]

    for car in cars:
        cs.draw( car, win )
    
    t = 0
    while True:
        time.sleep(0.25)

        for car in cars:
            cs.car_animate( car, t, win, 0 )

        t += 1
        
        win.update()
        
        if win.checkMouse():
            break

    win.close()

if __name__ == "__main__":
    main()