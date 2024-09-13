from OpenGL.GL import *
from OpenGL.GLUT import *
import random as rd

def draw_LINES():
    glPointSize(3)
    glBegin(GL_LINES)
    # lower line
    glVertex2f(100, 100)
    glVertex2f(450, 100)
    # upper line
    glVertex2f(100, 400)
    glVertex2f(450, 400)
    # left line
    glVertex2f(100, 100)
    glVertex2f(100, 400)
    # right line
    glVertex2f(450, 400)
    glVertex2f(450, 100)
    glEnd()

def draw_TRI_LINES():
    glPointSize(3)
    glBegin(GL_LINE_STRIP)
    # roof
    # right points
    glVertex2f(100, 400)
    glVertex2f(275, 550)
    # left points
    glVertex2f(450, 400)
    glVertex2f(275, 550)
    glEnd()

def draw_QUADS():
    glPointSize(3)
    glBegin(GL_QUADS)

    # Window Left filled
    # a,b x = +200 - 100, y = +50 +100
    glVertex2f(150, 300)  # (250, 300)
    glColor3f(1.0, 1.0, 1.0)
    # b to c
    glVertex2f(200, 300)  # (300, 300)
    glColor3f(0.0, 1.0, 1.0)
    # c to d
    glVertex2f(200, 350)  # (300, 400)
    glColor3f(1.0, 0.0, 1.0)
    # a to d
    glVertex2f(150, 350)  # (250, 400)
    #------------------------------------
    # Window Right filled
    # a,b x = +200 - 100, y = +50 +100
    glVertex2f(350, 300)  # (250, 300)
    glColor3f(1.0, 1.0, 1.0)
    # b to c
    glVertex2f(400, 300)  # (300, 300)
    glColor3f(0.0, 1.0, 1.0)
    # c to d
    glVertex2f(400, 350)  # (300, 400)
    glColor3f(1.0, 0.0, 1.0)
    # a to d
    glVertex2f(350, 350)  # (250, 400)


    # Door filled
    # a,b x = +200, y = +50
    glVertex2f(250, 150) # (250, 300)
    glColor3f(1.0, 1.0, 1.0)
    # b to c
    glVertex2f(300, 150) # (300, 300)
    glColor3f(0.0, 1.0, 1.0)
    # c to d
    glVertex2f(300, 250) #(300, 400)
    glColor3f(1.0, 0.0, 1.0)
    # a to d
    glVertex2f(250, 250) #(250, 400)
    glEnd()

# ============================================================
# View on screen
def iterate():
    glViewport(0, 0, 550, 550)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600, 0.0, 600, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 1.0, 1.0)
    #call the draw methods here
    draw_LINES()
    draw_QUADS()
    draw_TRI_LINES()

    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(550, 550) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()