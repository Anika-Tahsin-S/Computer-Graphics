from OpenGL.GL import *
from OpenGL.GLUT import *
import random as rd

def drawPoints(x, y):
    glPointSize(5)
    glColor3f(1, 1, 0)
    glBegin(GL_POINTS)
    glVertex2f(x/1000, y/1000 )
    glEnd()

def Zone(dx, dy):
    if abs(dx) <= abs(dy):
        if dx >= 0 and dy >= 0:
            return 1
        elif dx <= 0 and dy >= 0:
            return 2
        elif dx >= 0 and dy <= 0:
            return 6
        elif dx <= 0 and dy <= 0:
            return 5
    else:
        if dx >= 0 and dy >= 0:
            return 0
        elif dx <= 0 and dy >= 0:
            return 3
        elif dx >= 0 and dy <= 0:
            return 7
        elif dx <= 0 and dy <= 0:
            return 4

def CVRT_Zone0(region, x, y):
    if region==0:
        return x, y
    if region==1:
        return y, x
    if region==2:
        return y, -x
    if region==3:
        return -x, y
    if region==4:
        return -x, -y
    if region==5:
        return -y, -x
    if region==6:
        return -y, x
    if region==7:
        return x, -y


def convert_original(region, x, y):
    if region == 0:
        return x, y
    if region == 1:
        return y, x
    if region == 2:
        return -y, x
    if region == 3:
        return -x, y
    if region == 4:
        return -x, -y
    if region == 5:
        return -y, -x
    if region == 6:
        return y, -x
    if region == 7:
        return x, -y

def midPointAlgo(x1, y1, x2, y2, z):
    dx = x2 - x1
    dy = y2 - y1

    d = (2 * dy) - dx
    e = 2 * dy
    ne = 2 * (dy - dx)

    x = x1
    y = y1

    while x < x2:
        x, y = convert_original(z, x, y)
        drawPoints(x, y)
        if d < 0:
            x += 1
            d += e
        else:
            x += 1
            y += 1
            d += ne

def Draw_Line(x1, y1, x2, y2):
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    dx = x2 - x1
    dy = y2 - y1
    zone = Zone(dx, dy)
    cx1, cy1 = CVRT_Zone0(zone, x1, y1)
    cx2, cy2 = CVRT_Zone0(zone, x2, y2)
    midPointAlgo(cx1, cy1, cx2, cy2, zone)
    glEnd()

def for5():
    glPointSize(6000)
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)

    Draw_Line(100, 350, 200, 350)
    Draw_Line(100, 250, 200, 250)
    Draw_Line(100, 350, 100, 250)
    Draw_Line(200, 250, 200, 150)
    Draw_Line(100, 150, 200, 150)
    glEnd()

def for8():
    glPointSize(6000)
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)

    Draw_Line(100, 350, 200, 350)
    Draw_Line(100, 150, 200, 150)
    Draw_Line(100, 150, 100, 350)
    Draw_Line(200, 150, 200, 350)
    Draw_Line(100, 250, 200, 250)
    Draw_Line(100,250,200,350)
    Draw_Line(100,150,200,250)
    glEnd()

# View on screen
def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    for5()
    for8()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 300) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()