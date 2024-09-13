from OpenGL.GL import *
from OpenGL.GLUT import *

def draw_Points(x, y):
    glPointSize(5)
    glColor3f(0.0, 0.5, 0.5)
    glBegin(GL_POINTS)
    glVertex2f(x/1000, y/1000)
    glEnd()

def Zone_Assign(dx, dy):
    if abs(dx) <= abs(dy):
        if dx >= 0 and dy >= 0: return 1
        elif dx <= 0 and dy >= 0: return 2
        elif dx >= 0 and dy <= 0: return 6
        elif dx <= 0 and dy <= 0: return 5
    else:
        if dx >= 0 and dy >= 0: return 0
        elif dx <= 0 and dy >= 0: return 3
        elif dx >= 0 and dy <= 0: return 7
        elif dx <= 0 and dy <= 0: return 4


def Zone0(region, x, y):
    if region == 0: return x, y
    if region == 1: return y, x
    if region == 2: return y, -x
    if region == 3: return -x, y
    if region == 4: return -x, -y
    if region == 5: return -y, -x
    if region == 6: return -y, x
    if region == 7: return x, -y


def convert_original(region, x, y):
    if region == 0: return x, y
    if region == 1: return y, x
    if region == 2: return -y, x
    if region == 3: return -x, y
    if region == 4: return -x, -y
    if region == 5: return -y, -x
    if region == 6: return y, -x
    if region == 7: return x, -y


def midPointLineAlgorithm(x1, y1, x2, y2, z):
    # print("midpointLine", (x1,y1),(x2,y2))
    dx = x2 - x1
    dy = y2 - y1

    d = (2 * dy) - dx
    e = 2 * dy
    ne = 2 * (dy - dx)

    x = x1
    y = y1

    while x < x2:
        px, py = convert_original(z, x, y)
        draw_Points(px, py)
        if d < 0:
            x += 1
            d += e
        else:
            x += 1
            y += 1
            d += ne


def Draw_Line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    zone = Zone_Assign(dx, dy)
    cx1, cy1 = Zone0(zone, x1, y1)
    cx2, cy2 = Zone0(zone, x2, y2)
    midPointLineAlgorithm(cx1, cy1, cx2, cy2, zone)

#----------------------------------------------------
def draw_zero():
    Draw_Line(100, 350, 200, 350)
    Draw_Line(100, 150, 200, 150)
    Draw_Line(100, 150, 100, 350)
    Draw_Line(200, 150, 200, 350)


def draw_one():
    Draw_Line(200, 150, 200, 350)

def draw_two():
    Draw_Line(100, 350, 200, 350)
    Draw_Line(100, 150, 200, 150)
    Draw_Line(100, 250, 100, 150)
    Draw_Line(200, 250, 200, 350)
    Draw_Line(100, 250, 200, 250)

def draw_three():
    Draw_Line(100, 350, 200, 350)
    Draw_Line(100, 150, 200, 150)
    Draw_Line(100, 250, 200, 250)
    Draw_Line(200, 350, 200, 150)

def draw_four():
    Draw_Line(100, 350, 100, 250)
    Draw_Line(100, 250, 200, 250)
    Draw_Line(200, 350, 200, 150)

def draw_five():
    Draw_Line(100, 350, 200, 350)
    Draw_Line(100, 250, 200, 250)
    Draw_Line(100, 350, 100, 250)
    Draw_Line(200, 250, 200, 150)
    Draw_Line(100, 150, 200, 150)

def draw_six():
    Draw_Line(100, 350, 200, 350)
    Draw_Line(100, 350, 100, 150)
    Draw_Line(100, 250, 200, 250)
    Draw_Line(200, 250, 200, 150)
    Draw_Line(100, 150, 200, 150)

def draw_seven():
    Draw_Line(100, 350, 200, 350)
    Draw_Line(200, 350, 200, 150)

def draw_eight():
    Draw_Line(100, 350, 200, 350)
    Draw_Line(100, 150, 200, 150)
    Draw_Line(100, 150, 100, 350)
    Draw_Line(200, 150, 200, 350)
    Draw_Line(100, 250, 200, 250)

def draw_nine():
    Draw_Line(100, 350, 200, 350)
    Draw_Line(100, 250, 200, 250)
    Draw_Line(200, 350, 200, 150)
    Draw_Line(100, 350, 100, 250)

# q = second last digit
def for0():
    Draw_Line(300, 350, 400, 350)
    Draw_Line(300, 150, 400, 150)
    Draw_Line(300, 150, 300, 350)
    Draw_Line(400, 150, 400, 350)

def for1():
    Draw_Line(400, 150, 400, 350)

def for2():
    Draw_Line(300, 350, 400, 350)
    Draw_Line(300, 150, 400, 150)
    Draw_Line(300, 250, 300, 150)
    Draw_Line(400, 250, 400, 350)
    Draw_Line(300, 250, 400, 250)

def for3():
    Draw_Line(300, 350, 400, 350)
    Draw_Line(300, 150, 400, 150)
    Draw_Line(300, 250, 400, 250)
    Draw_Line(400, 350, 400, 150)

def for4():
    Draw_Line(300, 350, 300, 250)
    Draw_Line(300, 250, 400, 250)
    Draw_Line(400, 350, 400, 150)

def for5():
    Draw_Line(300, 350, 400, 350)
    Draw_Line(300, 250, 400, 250)
    Draw_Line(300, 350, 300, 250)
    Draw_Line(400, 250, 400, 150)
    Draw_Line(300, 150, 400, 150)

def for6():
    Draw_Line(300, 350, 400, 350)
    Draw_Line(300, 350, 300, 150)
    Draw_Line(300, 250, 400, 250)
    Draw_Line(400, 250, 400, 150)
    Draw_Line(300, 150, 400, 150)

def for7():
    Draw_Line(300, 350, 400, 350)
    Draw_Line(400, 350, 400, 150)

def for8():
    Draw_Line(300, 350, 400, 350)
    Draw_Line(300, 150, 400, 150)
    Draw_Line(300, 350, 300, 150)
    Draw_Line(400, 150, 400, 350)
    Draw_Line(300, 250, 400, 250)

def for9():
    Draw_Line(300, 350, 400, 350)
    Draw_Line(300, 250, 400, 250)
    Draw_Line(400, 350, 400, 150)
    Draw_Line(300, 350, 300, 250)


#----------------------------------------------------
def iterate():
    glViewport(0, 0, 550, 550)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    s = input("Enter your ID: ")
    p = (s[-2])
    q = (s[-1])
    if p == "0": draw_zero()
    elif p == "1": draw_one()
    elif p == "2": draw_two()
    elif p == "3": draw_three()
    elif p == "4": draw_four()
    elif p == "5": draw_five()
    elif p == "6": draw_six()
    elif p == "7": draw_seven()
    elif p == "8": draw_eight()
    elif p == "9": draw_nine()

    if q == "0": for0()
    elif q == "1": for1()
    elif q == "2": for2()
    elif q == "3": for3()
    elif q == "4": for4()
    elif q == "5": for5()
    elif q == "6": for6()
    elif q == "7": for7()
    elif q == "8": for8()
    elif q == "9": for9()

    glOrtho(0.0, 600, 0.0, 600, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 1.0, 1.0) #konokichur color set (RGB)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 2 OpenGL Window") #window name
glutDisplayFunc(showScreen)
glutMainLoop()