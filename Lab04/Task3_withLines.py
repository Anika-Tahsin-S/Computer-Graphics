from OpenGL.GL import *
from OpenGL.GLUT import *
import random as rd

def draw_LINES_For2():
    glPointSize(6000)
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)
    # upper line
    glVertex2f(122, 192)
    glVertex2f(50, 192)
    # right line
    glVertex2f(122, 140)
    glVertex2f(122, 192)
    # middle line
    glVertex2f(122, 140)
    glVertex2f(50, 140)
    # # left line 2
    glVertex2f(50, 90)
    glVertex2f(50, 140)
    # lower line
    glVertex2f(50, 90)
    glVertex2f(122, 90)
    glEnd()

def draw_LINES_For3():
    glPointSize(6000)
    glBegin(GL_LINES)
    glColor3f(1.0, 0.5, 0.0)
    # upper line
    glVertex2f(222, 192)
    glVertex2f(150, 192)
    # right line
    glVertex2f(222, 192)
    glVertex2f(222, 90)
    # middle line
    glVertex2f(222, 140)
    glVertex2f(150, 140)
    # lower line
    glVertex2f(150, 90)
    glVertex2f(222, 90)
    glEnd()

def draw_QUADS_For1A():
    glPointSize(1)
    glBegin(GL_QUADS)
    glColor3f(2.0, 0.5, 1.0)
    # First 1------------------------
    # For 1
    glVertex2f(270, 90) # (250, 300)
    glVertex2f(275, 90) # (300, 300)
    glVertex2f(275, 192) #(300, 400)
    glVertex2f(270, 192) #(250, 400)
    # the hand of 1
    glVertex2f(270, 192)  # (250, 300)
    glVertex2f(275, 187)  # (300, 300)
    glVertex2f(255, 176)  # (300, 400)
    glVertex2f(250, 170)  # (250, 400)
    glEnd()

def draw_QUADS_For4():
    glPointSize(1)
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    # For 4
    # Stand
    glVertex2f(360, 90)  # (250, 300)
    glVertex2f(365, 90)  # (300, 300)
    glVertex2f(365, 192)  # (300, 400)
    glVertex2f(360, 192)  # (250, 400)
    # Hand
    glVertex2f(300, 192)  # (250, 300)
    glVertex2f(300, 140)  # (300, 300)
    glVertex2f(305, 140)  # (300, 400)
    glVertex2f(305, 192)  # (250, 400)
    # middle line
    glVertex2f(300, 140)
    glVertex2f(300, 143)
    glVertex2f(365, 140)
    glVertex2f(365, 143)
    glEnd()

def draw_QUADS_For1B():
    glPointSize(1)
    glBegin(GL_QUADS)
    glColor3f(0.0, 1.0, 2.0)
    # First 1------------------------
    # For 1
    glVertex2f(420, 90) # (250, 300)
    glVertex2f(425, 90) # (300, 300)
    glVertex2f(425, 192) #(300, 400)
    glVertex2f(420, 192) #(250, 400)
    # the hand of 1
    glVertex2f(420, 192)  # (250, 300)
    glVertex2f(425, 187)  # (300, 300)
    glVertex2f(405, 176)  # (300, 400)
    glVertex2f(400, 170)  # (250, 400)
    glEnd()


def draw_LINES_For0():
    glPointSize(6000)
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    # upper line
    glVertex2f(542, 192)
    glVertex2f(470, 192)
    # right line
    glVertex2f(542, 192)
    glVertex2f(542, 90)
    # # left line 2
    glVertex2f(470, 90)
    glVertex2f(470, 192)
    # lower line
    glVertex2f(470, 90)
    glVertex2f(542, 90)
    glEnd()

def draw_LINES_For5():
    glPointSize(6000)
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)
    # upper line
    glVertex2f(642, 192)
    glVertex2f(570, 192)
    # right line
    glVertex2f(642, 90)
    glVertex2f(642, 140)
    # middle line
    glVertex2f(642, 140)
    glVertex2f(570, 140)
    # # left line 2
    glVertex2f(570, 192)
    glVertex2f(570, 140)
    # lower line
    glVertex2f(570, 90)
    glVertex2f(642, 90)
    glEnd()

def draw_LINES_For8():
    glPointSize(6000)
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 0.0)
    # upper line
    glVertex2f(742, 192)
    glVertex2f(670, 192)
    # right line
    glVertex2f(742, 192)
    glVertex2f(742, 90)
    # middle line
    glVertex2f(742, 140)
    glVertex2f(670, 140)
    # # left line 2
    glVertex2f(670, 90)
    glVertex2f(670, 192)
    # lower line
    glVertex2f(742, 90)
    glVertex2f(670, 90)
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
    #call the draw methods here
    # draw_points(250, 250)
    draw_LINES_For2()
    draw_LINES_For3()
    # draw_LINES_For5()
    draw_QUADS_For1A()
    draw_QUADS_For4()
    draw_QUADS_For1B()
    draw_LINES_For0()
    draw_LINES_For5()
    draw_LINES_For8()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 300) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()