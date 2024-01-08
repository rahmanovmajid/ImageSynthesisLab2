from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Draw X-Y axis system
def draw_axes():
    glColor3f(1.0, 0.0, 0.0)  # Red color for axes
    glBegin(GL_LINES)
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)  # X-axis
    glVertex2f(0.0, -1.0)
    glVertex2f(0.0, 1.0)  # Y-axis
    glEnd()

# Draw a yellow triangle using GL_LINE_LOOP
def draw_triangle():
    glColor3f(1.0, 1.0, 0.0)  # Yellow color for the triangle
    glBegin(GL_LINE_LOOP)
    glVertex2f(0.3, 0.2)
    glVertex2f(0.7, 0.5)
    glVertex2f(0.5, 0.7)
    glEnd()

    # Draw reflections in other quadrants
    glColor3f(1.0, 1.0, 0.0)  # Yellow color for the reflected triangles

    # Quadrant 2
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.3, 0.2)
    glVertex2f(-0.7, 0.5)
    glVertex2f(-0.5, 0.7)
    glEnd()

    # Quadrant 3
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.3, -0.2)
    glVertex2f(-0.7, -0.5)
    glVertex2f(-0.5, -0.7)
    glEnd()

    # Quadrant 4
    glBegin(GL_LINE_LOOP)
    glVertex2f(0.3, -0.2)
    glVertex2f(0.7, -0.5)
    glVertex2f(0.5, -0.7)
    glEnd()

def display():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    draw_axes()
    draw_triangle()

    glFlush()
    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow("Triangle and Reflections")
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
