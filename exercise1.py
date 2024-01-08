from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

# Global variables
center_x, center_y = 0.0, 0.0

def render_Scene():
    glBegin(GL_POINTS)
    for i in range(1, 11):
        angle = 2 * math.pi * i / 64
        radius = 0.5 * i / 10  # Increase radius progressively from 0.1 to 0.5
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)

        # Randomly choose point color
        glColor3f(random.random(), random.random(), random.random())
        # Increase point size progressively from 1 to 10
        glPointSize(i)
        glVertex2f(x, y)
    glEnd()

def display():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    render_Scene()
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
glutCreateWindow("Circle with Increasing Point Sizes")
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
