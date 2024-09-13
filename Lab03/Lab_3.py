from OpenGL.GL import *
from OpenGL.GLUT import *

def drawPoints(x, y):
    glPointSize(2.0)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def MidPoint_Circle(X, Y, r):
    d = 1 - r
    x = 0
    y = r
    while x <= y:
        x += 1
        if d < 0:
            d += 2 * x + 3
        else:
            y -= 1
            d += 2 * (x - y) + 5

        # Zone conversion
        drawPoints(X + x, Y + y) # Zone 0
        drawPoints(X - x, Y + y) # Zone 1
        drawPoints(X + x, Y - y) # Zone 2
        drawPoints(X - x, Y - y) # Zone 3
        drawPoints(X + y, Y + x) # Zone 4
        drawPoints(X - y, Y + x) # Zone 5
        drawPoints(X + y, Y - x) # Zone 6
        drawPoints(X - y, Y - x) # Zone 7


def drawCircles(X, Y, R):
    MidPoint_Circle(X, Y, R) # Parent circle
    MidPoint_Circle(X + R/2, Y, R/2) # Right Child Circle
    MidPoint_Circle(X - R/2, Y, R/2) # Left Child Circle
    MidPoint_Circle(X, Y + R/2, R/2) # Top Child Circle
    MidPoint_Circle(X, Y - R/2, R/2) # Bottom Child Circle
    MidPoint_Circle(X + R/3 + 4, Y + R/3 + 4, R/2) # Middle Child of Top Right
    MidPoint_Circle(X - R/3 - 4, Y + R/3 + 4, R/2) # Middle Child of Top Left
    MidPoint_Circle(X + R/3 + 4, Y - R/3 - 4, R/2) # Middle Child of Bottom Right
    MidPoint_Circle(X - R/3 - 4, Y - R/3 - 4, R/2) # Middle Child of Bottom Left


# --------------------------------------------------------
def iterate():
    glViewport(0, 0, 600, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600, 0.0, 600, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, .5, .5)
    drawCircles(300, 300, 230)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 3 Task")
glutDisplayFunc(showScreen)

glutMainLoop()