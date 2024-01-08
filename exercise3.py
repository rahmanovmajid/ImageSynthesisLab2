from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Global variables
order = 8  # Number of sides in the polygon

def draw_regular_polygon_triangles():
    glColor3f(1.0, 0.0, 0.0)  # Red color for triangles
    glBegin(GL_TRIANGLES)
    for i in range(order):
        angle1 = 2 * math.pi * i / order
        angle2 = 2 * math.pi * (i + 1) / order

        x1, y1 = 0.0, 0.0  # Center of the polygon
        x2 = 0.5 * math.cos(angle1)
        y2 = 0.5 * math.sin(angle1)
        x3 = 0.5 * math.cos(angle2)
        y3 = 0.5 * math.sin(angle2)

        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glVertex2f(x3, y3)
    glEnd()

def draw_regular_polygon_triangle_strip():
    glColor3f(0.0, 1.0, 0.0)  # Green color for triangle strip
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(order + 1):
        angle = 2 * math.pi * i / order
        x = 0.5 * math.cos(angle)
        y = 0.5 * math.sin(angle)

        glVertex2f(x, y)
        glVertex2f(0.0, 0.0)  # Center of the polygon
    glEnd()

def draw_regular_polygon_triangle_fan():
    glColor3f(0.0, 0.0, 1.0)  # Blue color for triangle fan
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0.0, 0.0)  # Center of the polygon
    for i in range(order + 1):
        angle = 2 * math.pi * i / order
        x = 0.5 * math.cos(angle)
        y = 0.5 * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

def display():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    draw_regular_polygon_triangles()
    glTranslatef(1.5, 0.0, 0.0)  # Move to the right for the next polygon
    draw_regular_polygon_triangle_strip()
    glTranslatef(1.5, 0.0, 0.0)  # Move to the right for the next polygon
    draw_regular_polygon_triangle_fan()

    glFlush()
    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-2.0, 2.0, -1.0, 1.0)  # Adjust these values based on your preference
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 400)  # Adjust the window size as needed
glutCreateWindow("Regular Polygons")
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
