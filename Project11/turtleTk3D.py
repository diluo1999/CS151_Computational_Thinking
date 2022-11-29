# Implements a 3D turtle class using the Tk library
# Implements an orthographic transformation with no scaling (yet)
# Bruce Maxwell
# Updated Spring 2011
# Updated Spring 2015, BAM
# Updated Fall 2017 for Python 3, BAM

import tkinter
import math
import random

tk = tkinter

# return the average z coordinate of the points for the polygon
def _zkey(a):
    asum = 0.0
    for item in a[0]:
        asum += item[2]
    az = asum/float( len( a[0] ) )

    return az

# compare the average z-value for the points on the polygon
def _zsort(a, b):
    asum = 0.0
    for item in a[0]:
        asum += item[2]
    az = asum/float( len( a[0] ) )

    bsum = 0.0;
    for item in b[0]:
        bsum += item[2]
    bz = bsum/float( len( b[0] ) )
    
    if az < bz:
        return -1
    elif az == bz:
        return 0
    return 1

# copies a 3-element vector
def copyVec( vecTo, vecFrom ):
    vecTo[0] = vecFrom[0]
    vecTo[1] = vecFrom[1]
    vecTo[2] = vecFrom[2]

def length( vec ):
    return math.sqrt( vec[0]*vec[0] + vec[1]*vec[1] + vec[2]*vec[2])

# vec /= len(vec)
def normalize( vec ):
    length = math.sqrt(vec[0]*vec[0] + vec[1]*vec[1] + vec[2]*vec[2])
    vec[0] /= length
    vec[1] /= length
    vec[2] /= length
    return

# vecC = vecA x vecB
def cross( vecA, vecB, vecC ):
    vecC[0] = vecA[1]*vecB[2] - vecA[2]*vecB[1]
    vecC[1] = vecA[2]*vecB[0] - vecA[0]*vecB[2]
    vecC[2] = vecA[0]*vecB[1] - vecA[1]*vecB[0]
    return

# dot product of vecA and vecB
def dot( vecA, vecB ):
    return vecA[0]*vecB[0] + vecA[1]*vecB[1] + vecA[2]*vecB[2]

# transforms v in place
def xform( M, v ):
    t = [0.0, 0.0, 0.0]
    for i in range(3):
        t[i] = M[i][0]*v[0] + M[i][1]*v[1] + M[i][2]*v[2]

    v[0] = t[0]
    v[1] = t[1]
    v[2] = t[2]
    return

# matrix multiplication, returns a new matrix
def mtxmul( A, B ):
    C = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
    for i in range(3):
        for j in range(3):
            C[i][j] = 0.0
            for k in range(3):
                C[i][j] += A[i][k] * B[k][j]

    return C

# clones a 3x3 matrix
def mtxclone( A ):
    return [ [A[0][0], A[0][1], A[0][2]],
             [A[1][0], A[1][1], A[1][2]],
             [A[2][0], A[2][1], A[2][2]] ]

# utility class to mirror the standard turtle fields
class RawPen3D():

    def __init__(self):
        self.penDown = True
        self._color = 'black'
        self._width = 1
        self.fill = False
        self.fillPoints = []
        

# the main turtle class
class Turtle3D:
    frameid = 0

    def __init__(self, 
                 winx = 800, 
                 winy = 800, 
                 title = "Turtle 3D",
                 position = (0.0, 0.0, 0.0),
                 heading = (1.0, 0.0, 0.0),
                 up = (0.0, 0.0, 1.0) ):

        # windowing stuff
        self.root = tk.Tk()
        self.root.geometry( "%dx%d+200+30" % (winx, winy) )
        self.root.title(title)
        self.root.maxsize( 1024, 1024 )
        self.root.lift()

        self.winx = winx
        self.winy = winy

        # build the menus
        # print 'Building menus'
        self.buildMenus()

        # print 'Building canvas'
        self.buildCanvas()

        # print 'Setting bindings'
        self.setBindings()

        ### turtle stuff

        # position of the turtle in 3D space
        self.iposition = [position[0], position[1], position[2]]

        # orientation as a coordinate system
        self.x = [heading[0], heading[1], heading[2]]
        self.y = [up[0], up[1], up[2]]
        self.z = [0, 0, 0]

        # the overall rotation matrix for the 'view'
        self.rotation = [[ 1.0, 0.0, 0.0 ],
                         [ 0.0, 1.0, 0.0 ],
                         [ 0.0, 0.0, 1.0 ] ]

        # set up the orthonormal system
        normalize(self.x)
        cross( self.x, self.y, self.z )
        normalize(self.z)
        cross( self.z, self.x, self.y )
        normalize(self.y)

        # other state variables
        self._pen = RawPen3D()

        # list of drawn stuff
        self.shapes = []

    def setup(self, width=None, height=None):
        # placeholder, doesn't do anything
        return

    def buildMenus(self):

        self.menu = tk.Menu(self.root)
        self.root.config(menu = self.menu)
        self.menulist = []

        menu = tk.Menu( self.menu )
        self.menu.add_cascade(label="File", menu=menu )
        self.menulist.append(menu)

        menu = tk.Menu( self.menu )
        self.menu.add_cascade(label="View", menu=menu )
        self.menulist.append(menu)


        menutext = [ [ '-', 'Quit  \xE2\x8C\x98-Q' ],
                     [ 'Reset View  \xE2\x8C\x98-R'] ]
        menucmd = [ [ None, self.handleQuit ],
                    [ self.handleReset ] ]
                     
        for i in range( len(self.menulist) ):
            for j in range( len(menutext[i]) ):
                if menutext[i][j] != '-':
                    self.menulist[i].add_command( label=menutext[i][j], command=menucmd[i][j] )
                else:
                    self.menulist[i].add_separator()

    def buildCanvas(self):
        self.canvas = tk.Canvas( self.root, width=self.winx, height=self.winy )
        self.canvas.pack( expand=tk.YES, fill=tk.BOTH )

    def setBindings(self):
        self.root.bind( '<Button-1>', self.handleButton1 )
        self.root.bind( '<B1-Motion>', self.handleButton1Motion )
        self.root.bind( '<Command-q>', self.handleModQ )
        self.root.bind( '<Configure>', self.handleConfigure )
        self.root.bind( 'q', self.handleModQ )
        self.root.bind( 'r', self.resetView )
        self.root.bind( '<Command-r>', self.resetView )

    def setRightMouseCallback(self, func):
        self.root.bind( '<Button-2>', func )

    def handleButton1(self, event):
        self.baseClick = (event.x, event.y)
        self.R0 = mtxclone(self.rotation)

    def viewXform(self, x):
        xform( self.rotation, x )
        x[0] = x[0] + self.winx/2
        x[1] = -x[1] + self.winy/2

    def handleButton1Motion(self, event):
        diff = [ event.x - self.baseClick[0], event.y - self.baseClick[1] ]
        

        anglex = math.pi * diff[0] / 200.0
        angley = math.pi * diff[1] / 200.0

        cth = math.cos( anglex )
        sth = math.sin( anglex )

        Ry = [ [cth, 0.0, sth], 
               [0.0, 1.0, 0.0 ],
               [-sth, 0.0, cth ] ]

        cth = math.cos( angley )
        sth = math.sin( angley )

        Rx = [ [1.0, 0.0, 0.0 ],
               [0.0, cth, -sth ],
               [0.0, sth, cth] ]

        # rotation matrix relative to the original orientation
        Rmtx = mtxmul( Rx, Ry )
        self.rotation = mtxmul( Rmtx, self.R0 )

        # redraw
        self.updateShapes()
        return

    def reset(self):
        for item in self.shapes:
            self.canvas.delete( item[1] )

        # position of the turtle in 3D space
        self.iposition = [0.0, 0.0, 0.0]

        # orientation as a coordinate system
        self.x = [1.0, 0.0, 0.0]
        self.y = [0.0, 0.0, 1.0]
        self.z = [0, 0, 0]

        # the overall rotation matrix for the 'view'
        self.rotation = [[ 1.0, 0.0, 0.0 ],
                         [ 0.0, 1.0, 0.0 ],
                         [ 0.0, 0.0, 1.0 ] ]

        return

    def resetView(self, event=None):
        # position of the turtle in 3D space
        self.iposition = [0.0, 0.0, 0.0]

        # orientation as a coordinate system
        self.x = [1.0, 0.0, 0.0]
        self.y = [0.0, 0.0, 1.0]
        self.z = [0, 0, 0]

        # the overall rotation matrix for the 'view'
        self.rotation = [[ 1.0, 0.0, 0.0 ],
                         [ 0.0, 1.0, 0.0 ],
                         [ 0.0, 0.0, 1.0 ] ]

        self.updateShapes()

        return

    def updateCanvas(self):
        self.canvas.update()

    def updateShapes(self):

        # need to sort the shapes by z value
        # need to transform the points by the current view, first
        # make a list of the z coordinates
        zlist = []
        for i in range(len(self.shapes)):
            item = self.shapes[i]
            if item[0] == 'line':
                x0 = [ item[2], item[3], item[4] ]
                x1 = [ item[5], item[6], item[7] ]

                # view transform
                self.viewXform( x0 )
                self.viewXform( x1 )

                vertices = [x0, x1]

                zlist.append( (vertices, i) ) 

            elif item[0] == 'polygon':

                # make a list of vertices
                vertices = []
                for pt in item[2]:
                    v = [pt[0], pt[1], pt[2]]
                    # transform the original vertex points by the view
                    self.viewXform( v )
                    vertices.append( (v[0], v[1], v[2]) )

                zlist.append( (vertices, i) )

        # python 3 doesn't support a comparison function any more, just keys
        zlist.sort(key=_zkey)

        # need to update all of the drawn lines
        for i in range(len(self.shapes)):

            ix = zlist[i][1]

            if self.shapes[ix][0] == 'line':
                line = self.shapes[ix]
                # edit coordinates
                x0 = zlist[i][0][0]
                x1 = zlist[i][0][1]
                self.canvas.coords( line[1], 
                                    x0[0], x0[1],
                                    x1[0], x1[1] )

            elif self.shapes[ix][0] == 'polygon':

                self.canvas.delete( self.shapes[ix][1] )

                # make a list of vertices
                vertices = []
                for item in zlist[i][0]:
                    vertices.append( (item[0], item[1]) )

                tpoly = self.canvas.create_polygon( vertices,
                                                    fill = self.shapes[ix][3],
                                                    width = self.shapes[ix][4],
                                                    outline = self.shapes[ix][3] )

                self.shapes[ix] = ('polygon', 
                                   tpoly, 
                                   self.shapes[ix][2], 
                                   self.shapes[ix][3],
                                   self.shapes[ix][4] )

            self.canvas.lift( self.shapes[ix][1] )

        return


    def handleReset(self):
        self.rotation = [ [1.0, 0.0, 0.0],
                          [0.0, 1.0, 0.0],
                          [0.0, 0.0, 1.0] ]
        self.updateShapes()
        return


    def handleModQ(self, event):
        self.handleQuit()

    def handleConfigure(self, event):

        # resize the screen
        self.winx = event.width
        self.winy = event.height

        # update the view?

    def handleQuit(self):
        print('Terminating')
        self.root.destroy()

    def cube(self, distance = 100):
        # draw a cube using relative commands
        for i in range(4):
            self.forward(distance)
            self.left(90)

        self.up()
        self.pitch(90)
        self.forward(distance)
        self.pitch(-90)
        self.down()

        for i in range(4):
            self.forward(distance)
            self.pitch(-90)
            self.forward(distance)

            self.up()
            self.forward(-distance)
            self.pitch(90)
            self.down()

            self.left(90)
    
    # probably want a clone method

    def testCallback(self, event):
        self.setheading( ( (1.0, 0.0, 0.0), (0.0, 0.0, 1.0) ) )
        self.yaw(30)
        self.roll(30)
        
        # screen coordinates to world coords?
        x = ( event.x - self.winx/2, -event.y + self.winy/2, 0.0 )
        self.up()
        self.goto( x )
        self.down()

        self.cube()

    def test(self):

        tc = ['red', 'green', 'blue', 'yellow' ]

        self.width(3)
        self.up()
        self.goto(0,0,0)
        self.down()
        self.color('red')
        self.goto(200, 0, 0)

        self.up()
        self.goto(0,0,0)
        self.down()
        self.color('green')
        self.goto(0, 200, 0)
        
        self.up()
        self.goto(0,0,0)
        self.down()
        self.color('blue')
        self.goto(0, 0, 200)

        self.up()
        self.goto(0, 0, 0)
        self.setheading( ( (1.0, 0.0, 0.0), (0.0, 0.0, 1.0) ) )
        self.color('yellow')
        self.down()
        self.cube()

        self.up()
        self.goto(-200, 200, 100)
        self.setheading(0)
        self.down()
        self.roll(30)
        self.color('purple')
        self.fill(True)
        for i in range(8):
            self.forward(50)
            self.left(45)
        self.fill(False)


        self.setRightMouseCallback( self.testCallback )

    def testCircle(self):
        self.up()
        self.goto( 0, 0, 0)
        self.setheading(0)
        self.down()

        for i in range(10):
            self.color( random.random(), random.random(), random.random()  )
            self.up()
            self.goto( 0, i*5, i*30 )
            self.setheading(0)
            self.down()
            self.fill(True)
            self.circle( 110 - i*10, 360 - i*30)
            self.fill(False)


    def wait(self):
        self.main()

    def mainloop(self):
        self.main()

    def main(self):
        # print 'Entering main loop'
        self.root.mainloop()

    # begin turtle commands
    def backward(self, distance):
        self.forward(-distance)

    def forward(self, distance):
        # move along the local x axis by distance
        xnew = self.iposition[0] + distance * self.x[0]
        ynew = self.iposition[1] + distance * self.x[1]
        znew = self.iposition[2] + distance * self.x[2]

        if self._pen.penDown:

            # coordinate system convert (turtle to Tk)
            x0 = [ self.iposition[0], self.iposition[1], self.iposition[2] ]
            xn = [ xnew, ynew, znew ]

            self.viewXform( x0 )
            self.viewXform( xn )

            # create a line object from the current to the new position
            lt = self.canvas.create_line( x0[0], x0[1], xn[0], xn[1],
                                          width=self._pen._width,
                                          fill=self._pen._color)

        
            # store the shape reference and its coordinates in world space
            self.shapes.append( ('line', lt, self.iposition[0], self.iposition[1], self.iposition[2], xnew, ynew, znew ) )

            # see if the fill flag is on and we need to store the point
            if self._pen.fill:
                #print 'adding point: (%d %d)' % (int(xn), int(yn))
                self._pen.fillPoints.append( ( xnew, ynew, znew ) )

        # update the turtle location
        self.iposition[0] = xnew
        self.iposition[1] = ynew
        self.iposition[2] = znew
        
        return

    def goto(self, xnew, ynew=None, znew=0.0 ):

        if ynew == None:
            if len(xnew) == 2:
                ynew = xnew[1]
                xnew = xnew[0]
            elif len(xnew) == 3:
                ynew = xnew[1]
                znew = xnew[2]
                xnew = xnew[0]

        if self._pen.penDown:

            x0 = [ self.iposition[0], self.iposition[1], self.iposition[2] ]
            xn = [ xnew, ynew, znew ]

            self.viewXform( x0 )
            self.viewXform( xn )

            lt = self.canvas.create_line( x0[0], x0[1], xn[0], xn[1],
                                          width=self._pen._width,
                                          fill=self._pen._color)

            # store the shape reference
            self.shapes.append( ('line', lt, self.iposition[0], self.iposition[1], self.iposition[2], xnew, ynew, znew ) )

            # see if the fill flag is on and we need to store the point
            if self._pen.fill:
                self._pen.fillPoints.append( ( xnew, ynew, znew ) )

        # update the turtle location
        self.iposition[0] = xnew
        self.iposition[1] = ynew
        self.iposition[2] = znew

#        print 'position %.2f %.2f %.2f' % (self.iposition[0], self.iposition[1], self.iposition[2])
        
        return

    # adds an offset to the x vector, then renormalizes and rebuilds the turtle orientation coordinates
    def nudge(self, direction):
        self.x[0] += direction[0]
        self.x[1] += direction[1]
        self.x[2] += direction[2]

        # if a nudge sets the x vector to zero, then set it back to the default X direction
        if length(self.x) == 0.0:
            self.x[0] = 1.0

        # set up the orthonormal system
        normalize(self.x)
        cross( self.x, self.y, self.z )
        normalize(self.z)
        cross( self.z, self.x, self.y )
        normalize(self.y)

    def left(self, angle):
        # temporary versions of x and z
        tmpx = [ self.x[0], self.x[1], self.x[2] ]
        tmpy = [ self.y[0], self.y[1], self.y[2] ]
        tmpz = [ self.z[0], self.z[1], self.z[2] ]

        # align the current axes with the base axes
        M = [ [self.x[0], self.x[1], self.x[2]],
              [self.y[0], self.y[1], self.y[2]],
              [self.z[0], self.z[1], self.z[2]] ]

        xform( M, tmpx )
        xform( M, tmpy )
        xform( M, tmpz )

        # rotate left around the Y axis
        radangle = angle * math.pi / 180.0
        cth = math.cos(radangle)
        sth = math.sin(radangle)
        R = [ [ cth, 0, sth ],
              [ 0, 1, 0 ],
              [ -sth, 0, cth ] ]
        xform( R, tmpx )
        xform( R, tmpy )
        xform( R, tmpz )

        # unalign
        MInv = [ [self.x[0], self.y[0], self.z[0]],
                 [self.x[1], self.y[1], self.z[1]],
                 [self.x[2], self.y[2], self.z[2]] ]
        xform( MInv, tmpx )
        xform( MInv, tmpy )
        xform( MInv, tmpz )
        
        # copy
        copyVec( self.x, tmpx )
        copyVec( self.y, tmpy )
        copyVec( self.z, tmpz )

        # set up the orthonormal system
        normalize(self.x)
        cross( self.x, self.y, self.z )
        normalize(self.z)
        cross( self.z, self.x, self.y )
        normalize(self.y)

    def right(self, angle):
        self.left( -angle )

    def yaw(self, angle):
        self.left( angle )

    def width(self, w=None):
        if w != None:
            self._pen._width = w

        return self._pen._width

    def color(self, r=None, g=None, b=None):
        if r == None:
            if self._pen._color[0] == '#':
                tr = eval( '0x' + self._pen._color[1:3] )
                tg = eval( '0x' + self._pen._color[3:5] )
                tb = eval( '0x' + self._pen._color[5:7] )
                return (tr/255.0, tg/255.0, tb/255.0)
            else:
                return self._pen._color

        if r != None and (g == None and b == None):
            try:
                v = len(r)
                self._pen._color = "#%02X%02X%02X" % ( int(255*r[0]), int(255*r[1]), int(255*r[2]) )
            except:
                self._pen._color = r;
        elif g != None and b != None and 0 <= r <= 1.0 and 0 <= g <= 1.0 and 0 <= b <= 1.0:
            self._pen._color = "#%02X%02X%02X" % ( int(255*r), int(255*g), int(255*b) )
        elif g != None and b != None and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            self._pen._color = "#%02X%02X%02X" % (int(r), int(g), int(b))

        return


    def pitch(self, angle ):
        # temporary versions of x and y
        tmpx = [ self.x[0], self.x[1], self.x[2] ]
        tmpy = [ self.y[0], self.y[1], self.y[2] ]
        tmpz = [ self.z[0], self.z[1], self.z[2] ]

        # align the current axes with the base axes
        M = [ [self.x[0], self.x[1], self.x[2]],
              [self.y[0], self.y[1], self.y[2]],
              [self.z[0], self.z[1], self.z[2]] ]

        xform( M, tmpx )
        xform( M, tmpy )
        xform( M, tmpz )

        # rotate around the Z axis
        radangle = angle * math.pi / 180.0
        cth = math.cos(radangle)
        sth = math.sin(radangle)
        R = [ [ cth, sth, 0 ],
              [ -sth, cth, 0 ],
              [ 0, 0, 1 ] ]
        xform( R, tmpx )
        xform( R, tmpy )
        xform( R, tmpz )

        # unalign
        MInv = [ [self.x[0], self.y[0], self.z[0]],
                 [self.x[1], self.y[1], self.z[1]],
                 [self.x[2], self.y[2], self.z[2]] ]
        xform( MInv, tmpx )
        xform( MInv, tmpy )
        xform( MInv, tmpz )
        
        # copy
        copyVec( self.x, tmpx )
        copyVec( self.y, tmpy )
        copyVec( self.z, tmpz )

        # set up the orthonormal system
        normalize(self.x)
        cross( self.x, self.y, self.z )
        normalize(self.z)
        cross( self.z, self.x, self.y )
        normalize(self.y)

    def roll(self, angle ):
        # temporary versions of y and z
        tmpx = [ self.x[0], self.x[1], self.x[2] ]
        tmpz = [ self.z[0], self.z[1], self.z[2] ]
        tmpy = [ self.y[0], self.y[1], self.y[2] ]

        # align the current axes with the base axes
        M = [ [self.x[0], self.x[1], self.x[2]],
              [self.y[0], self.y[1], self.y[2]],
              [self.z[0], self.z[1], self.z[2]] ]

        xform( M, tmpx )
        xform( M, tmpz )
        xform( M, tmpy )

        # rotate around the X axis
        radangle = angle * math.pi / 180.0
        cth = math.cos(radangle)
        sth = math.sin(radangle)
        R = [ [ 1, 0, 0 ],
              [ 0,  cth, -sth ],
              [ 0, sth, cth ] ]
        xform( R, tmpx )
        xform( R, tmpy )
        xform( R, tmpz )

        # unalign
        MInv = [ [self.x[0], self.y[0], self.z[0]],
                 [self.x[1], self.y[1], self.z[1]],
                 [self.x[2], self.y[2], self.z[2]] ]
        xform( MInv, tmpx )
        xform( MInv, tmpy )
        xform( MInv, tmpz )
        
        # copy
        copyVec( self.x, tmpx )
        copyVec( self.y, tmpy )
        copyVec( self.z, tmpz )
        
        # set up the orthonormal system
        normalize(self.x)
        cross( self.x, self.y, self.z )
        normalize(self.z)
        cross( self.z, self.x, self.y )
        normalize(self.y)

    def up(self):
        self._pen.penDown = False
        return

    def isdown(self):
        return self._pen.penDown

    def down(self):
        self._pen.penDown = True
        return

    def tracer(self, blah):
        return

    def hideturtle(self):
        return

    def showturtle(self):
        return

    def circle(self, r, theta = 360):
        # have the turtle make a circle going forward and left

        #1/r radians per step
        radPerStep = 3.0/r

        steps = int ((math.pi * theta / 180.0) / radPerStep)

        # check if steps is zero
        if steps == 0:
            p = self.position()
            self.forward(1)
            self.up()
            self.goto(p)
            return

        dxPerStep = (math.pi * 2.0 * r) * theta/360.0 / float(steps)
        daPerStep = float(theta) / float(steps)

        for i in range(steps):
            self.forward(dxPerStep)
            self.left(daPerStep)

        return
    
    def position(self):
        return (self.iposition[0], self.iposition[1], self.iposition[2])

    def heading(self):
        return ( (self.x[0], self.x[1], self.x[2]), (self.y[0], self.y[1], self.y[2]) )

    def seth(self, head):
        self.setheading(head)

    # assumes heading is given as two vectors representing x (forward) and y (up)
    def setheading(self, head):
        # should check if this is a single value
        try:
            a = len(head)
        except:
            a = head * math.pi / 180.0
            ca = math.cos( a )
            sa = math.sin( a )
            head = ( ( ca, sa, 0.0 ), (0.0, 0.0, 1.0) )

        # if not a single value
        self.x[0] = head[0][0]
        self.x[1] = head[0][1]
        self.x[2] = head[0][2]

        self.y[0] = head[1][0]
        self.y[1] = head[1][1]
        self.y[2] = head[1][2]

        # set up the orthonormal system
        normalize(self.x)
        cross( self.x, self.y, self.z )
        normalize(self.z)
        cross( self.z, self.x, self.y )
        normalize(self.y)

#        print '(%.2f %.2f %.2f) (%.2f %.2f %.2f) (%.2f %.2f %.2f)' % (self.x[0], self.x[1], self.x[2],
#                                                                      self.y[0], self.y[1], self.y[2],
#                                                                      self.z[0], self.z[1], self.z[2] )

    def begin_fill(self):
        self.fill(True)
        return

    def end_fill(self):
        self.fill(False)
        return

    def fill(self, dowhat):

        if dowhat:

            # set the fill state to true
            #print 'Setting fill state to true'
            self._pen.fill = True

            # add the current location to the fill list (polygon starts here)
            self._pen.fillPoints = [ ( self.iposition[0], self.iposition[1], self.iposition[2]) ]

        else:

            # set the fill state to false
            self._pen.fill = False

            # need at least 3 points to make a polygon
            if len(self._pen.fillPoints) < 3:
                return

            # create and color/fill the polygon
            vertices = []
            for pt in self._pen.fillPoints:
                v = [pt[0], pt[1], pt[2]]
                self.viewXform(v)
                vertices.append( (v[0], v[1]) )

            tpoly = self.canvas.create_polygon( vertices,
                                                fill = self._pen._color, 
                                                width = self._pen._width,
                                                outline = self._pen._color )

            # add the shape to shape list for the turtle
            self.shapes.append( ('polygon', tpoly, self._pen.fillPoints, self._pen._color, self._pen._width) )

        return

    def save(self, filename=''):
        if filename == '':
            filename = "frame%03d.ps" % Turtle3D.frameid
            Turtle3D.frameid += 1
        
        self.canvas.postscript(file=filename, colormode = 'color')
        return

    def update(self):
        self.updateCanvas()

    def window2turtle(self, x, y ):
        return ( x - self.winx/2, -y + self.winy/2, 0)

if __name__ == "__main__":
    print("starting")
    t = Turtle3D(800, 800, 'Turtle 3D Test' )
    print("turtle created")
    t.test()
    print("turtle tested")
    t.main()
