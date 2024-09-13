from OpenGL.GL import *
from OpenGL.GLUT import *

def convToZero(x11, y11, addX, addY):
    x1 = y11 + addX
    y1 = x11 + addY
    return x1, y1
def convToOne(x11, y11, addX, addY):
    x1 = x11 + addX
    y1 = y11 + addY
    return x1, y1
def convToTwo(x11, y11, addX, addY):
    x1 = -x11 + addX
    y1 = y11 + addY
    return x1, y1
def convToThree(x11, y11, addX, addY):
    x1 = -y11 + addX
    y1 = x11 + addY
    return x1, y1
def convToFour(x11, y11, addX, addY):
    x1 = -y11 + addX
    y1 = -x11 + addY
    return x1, y1
def convToFive(x11, y11, addX, addY):
    x1 = -x11 + addX
    y1 = -y11 + addY
    return x1, y1
def convToSix(x11, y11, addX, addY):
    x1 = x11 + addX
    y1 = -y11 + addY
    return x1, y1
def convToSeven(x11, y11, addX, addY):
    x1 = y11 + addX
    y1 = -x11 + addY
    return x1, y1

def drawCircleMidPoint(rad, cenX, cenY):
    d = 1 - rad
    x = 0
    y = rad



    while(x<y):
        if(d<0):
            d = d + 2*x + 3
            x = x + 1
        else:
            d = d + 2*x - 2*y + 5
            x = x + 1
            y = y - 1

        x0, y0 = convToZero(x, y, cenX, cenY)
        draw_points(x0, y0)

        x1, y1 = convToOne(x, y, cenX, cenY)
        draw_points(x1, y1)

        x2, y2 = convToTwo(x, y, cenX, cenY)
        draw_points(x2, y2)

        x3, y3 = convToThree(x, y, cenX, cenY)
        draw_points(x3, y3)

        x4, y4 = convToFour(x, y, cenX, cenY)
        draw_points(x4, y4)

        x5, y5 = convToFive(x, y, cenX, cenY)
        draw_points(x5, y5)

        x6, y6 = convToSix(x, y, cenX, cenY)
        draw_points(x6, y6)

        x7, y7 = convToSeven(x, y, cenX, cenY)
        draw_points(x7, y7)


def draw_points(x, y):
    glPointSize(1) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()
def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1000, 1000, -1000, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    drawCircleMidPoint(980, 0, 0) #(radius, Center coodinate of x, Center coodinate of x)

    drawCircleMidPoint(490, 0, 490) #upper circle
    drawCircleMidPoint(490, 0, -490)#lower circle

    drawCircleMidPoint(490, 490, 0) #right circle
    drawCircleMidPoint(490, -490, 0) # left circle

    drawCircleMidPoint(490, 350, 350)  # upper right circle
    drawCircleMidPoint(490, -350, 350)  # upper left circle

    drawCircleMidPoint(490, 350, -350)  # lower right circle
    drawCircleMidPoint(490, -350, -350)  # lower left circle
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000) #window size
glutInitWindowPosition(50, 50)
wind = glutCreateWindow(b"Lab 3 (ID:19301051)") #window name
glutDisplayFunc(showScreen)

glutMainLoop()