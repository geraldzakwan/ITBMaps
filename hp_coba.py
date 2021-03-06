#! /usr/bin/env python
# -*- coding: utf-8 -*-
""" Tutorial 6: keyboard and mouse
"""

from __future__ import print_function

from OpenGL.GL import *
from OpenGL.GL.ARB import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLUT.special import *
from OpenGL.GL.shaders import *
from glew_wish import *
from csgl import *
from PIL.Image import open as pil_open
from createVertexBuilding import createBuilding, createAllBuilding, list_of_gedung

import common
import glfw
import sys
import os
import controls
import TextureLoader
# Global window
window = None
null = c_void_p(0)
jumlah_tempat = 0

CUBE_DEG_PER_S = 30.0
LIGHT_DEG_PER_S = 90.0
CUBE_SIZE = 9.0
flashLightPos = [ 0.0, 0.0, 0.0];
flashLightDir = [ 0.0, 0.0, -1.0 ];
flashLightColor = [ 0.2, 0.2, 0.2 ];

redLightColor = [ 0.5, 0.1, 0.2 ];
redLightPos = [ 10.0, 0.0, 5.0, 1.0 ];

greenLightColor = [ 0.1, 0.6, 0.2 ];
greenLightPos = [ 0.0, 0.0, 10.0, 1.0 ];
m_pSphere = gluNewQuadric()
m_cubeAngle = 0.0
m_lightAngle = 0.0
m_flashlightOn = True    

def Display():
    global m_cubeAngle, m_flashlightOn, m_lightAngle, m_pSphere, CUBE_SIZE
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT);
    
    glLoadIdentity();
    gluLookAt(0.0, 0.0, 20.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
    
    if (m_flashlightOn):
        glEnable(GL_LIGHT0);
    else:
        glDisable(GL_LIGHT0);
    
    # position the red light
    glLightfv(GL_LIGHT1, GL_POSITION, redLightPos);
    
    # draw the red light
    glPushMatrix();
    glDisable(GL_LIGHTING);
    glTranslatef(redLightPos[0], redLightPos[1], redLightPos[2]);
    glColor3fv(redLightColor);
    gluSphere(m_pSphere, 0.2, 10, 10);
    glEnable(GL_LIGHTING);
    glPopMatrix();
    
    # position and draw the green light
    glPushMatrix();
    glDisable(GL_LIGHTING);
    glRotatef(m_lightAngle, 1.0, 0.0, 0.0);
    glRotatef(m_lightAngle, 0.0, 1.0, 0.0);
    glLightfv(GL_LIGHT2, GL_POSITION, greenLightPos);
    glTranslatef(greenLightPos[0], greenLightPos[1], greenLightPos[2]);
    glColor3fv(greenLightColor);
    gluSphere(m_pSphere, 0.2, 10, 10);
    glEnable(GL_LIGHTING);
    glPopMatrix();
    

def OpenglInit():
    global m_pSphere
    glClearColor(0.0, 0.0, 0.0, 0.0);
    glEnable(GL_DEPTH_TEST)
    #glDepthFunc(GL_LEQUAL)              ### test
    glEnable(GL_LIGHT0);
    glLightfv(GL_LIGHT0, GL_POSITION, flashLightPos);
    glLightfv(GL_LIGHT0, GL_AMBIENT, flashLightColor);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, flashLightColor);
    glLightfv(GL_LIGHT0, GL_SPECULAR, flashLightColor);
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, flashLightDir);
    glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 12.0);
    
    # set up static red light
    glEnable(GL_LIGHT1);
    glLightfv(GL_LIGHT1, GL_AMBIENT, redLightColor);
    glLightfv(GL_LIGHT1, GL_DIFFUSE, redLightColor);
    glLightfv(GL_LIGHT1, GL_SPECULAR, redLightColor);
    
    # set up moving green light
    glEnable(GL_LIGHT2);
    glLightfv(GL_LIGHT2, GL_AMBIENT, greenLightColor);
    glLightfv(GL_LIGHT2, GL_DIFFUSE, greenLightColor);
    glLightfv(GL_LIGHT2, GL_SPECULAR, greenLightColor);
    
    # get a quadric object for the light sphere
    m_pSphere = gluNewQuadric()    

def load_gedung(filename):
    x = 0
    with open(filename) as file:
        for line in file:
            titik = [int(n) for n in line.strip().split(',')]
            list_of_gedung[x//4][x%4] = titik
            x = x + 1
    global jumlah_tempat
    jumlah_tempat = x // 4

    for i in range(0,  jumlah_tempat):
        for j in range(0, 4):
            for k in range(0, 3):
                # print( str(i) +" " +str(j)+ " " +str(k)+ " " + str(type(list_of_gedung[i][j][k])))
                list_of_gedung[i][j][k] = float(list_of_gedung[i][j][k]) / 50.0

    for i in range(0,  jumlah_tempat):
        for j in range(0, 4):
            list_of_gedung[i][j][0] = -1 * (list_of_gedung[i][j][0] - 318.0/50.0) + 318.0/50.0

    print( list_of_gedung)
def opengl_init():
    global window
    # Initialize the library
    if not glfw.init():
        print("Failed to initialize GLFW\n",file=sys.stderr)
        return False

    # Open Window and create its OpenGL context
    window = glfw.create_window(1024, 768, "HP", None, None) #(in the accompanying source code this variable will be global)
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    if not window:
        print("Failed to open GLFW window. If you have an Intel GPU, they are not 3.3 compatible. Try the 2.1 version of the tutorials.\n",file=sys.stderr)
        glfw.terminate()
        return False

    # Initialize GLEW
    glfw.make_context_current(window)
    glewExperimental = True

    # GLEW is a framework for testing extension availability.  Please see tutorial notes for
    # more information including why can remove this code.a
    if glewInit() != GLEW_OK:
        print("Failed to initialize GLEW\n",file=sys.stderr);
        return False
    return True

def createUVData():
    uv_data = []
    for i in range(0,jumlah_tempat):
        uv_data +=  [0.000059, 1.0-0.000004,
            0.000103, 1.0-0.336048,
            0.335973, 1.0-0.335903,
            1.000023, 1.0-0.000013,
            0.667979, 1.0-0.335851,
            0.999958, 1.0-0.336064,
            0.667979, 1.0-0.335851,
            0.336024, 1.0-0.671877,
            0.667969, 1.0-0.671889,
            1.000023, 1.0-0.000013,
            0.668104, 1.0-0.000013,
            0.667979, 1.0-0.335851,
            0.000059, 1.0-0.000004,
            0.335973, 1.0-0.335903,
            0.336098, 1.0-0.000071,
            0.667979, 1.0-0.335851,
            0.335973, 1.0-0.335903,
            0.336024, 1.0-0.671877,
            1.000004, 1.0-0.671847,
            0.999958, 1.0-0.336064,
            0.667979, 1.0-0.335851,
            0.668104, 1.0-0.000013,
            0.335973, 1.0-0.335903,
            0.667979, 1.0-0.335851,
            0.335973, 1.0-0.335903,
            0.668104, 1.0-0.000013,
            0.336098, 1.0-0.000071,
            0.000103, 1.0-0.336048,
            0.000004, 1.0-0.671870,
            0.336024, 1.0-0.671877,
            0.000103, 1.0-0.336048,
            0.336024, 1.0-0.671877,
            0.335973, 1.0-0.335903,
            0.667969, 1.0-0.671889,
            1.000004, 1.0-0.671847,
            0.667979, 1.0-0.335851]
    return uv_data

def main():
    if not opengl_init():
        return

    OpenglInit()

    load_gedung("itb_coordinate.txt")

    # Enable key events
    glfw.set_input_mode(window,glfw.STICKY_KEYS,GL_TRUE)
    glfw.set_cursor_pos(window, 1024/2, 768/2)

    # Set opengl clear color to something other than red (color used by the fragment shader)
    glClearColor(0.0,0.0,0.0,0.0)

    # Enable depth test
    glEnable(GL_DEPTH_TEST)
    # Accept fragment if it closer to the camera than the former one
    glDepthFunc(GL_LESS);
    glEnable(GL_CULL_FACE)

    vertex_array_id = glGenVertexArrays(1)
    glBindVertexArray( vertex_array_id )

    program_id = common.LoadShaders( ".\\shaders\\Tutorial6\\TransformVertexShader.vertexshader",
        ".\\shaders\\Tutorial6\\TextureFragmentShader.fragmentshader" )

    vertex_data = createAllBuilding()

    # Two UV coordinatesfor each vertex. They were created withe Blender.
    uv_data = createUVData()

    # Get a handle for our "MVP" uniform
    matrix_id = glGetUniformLocation(program_id, "MVP");

    texture = []
    texture_id = []

    texture_id.append(glGetUniformLocation(program_id, "myTextureSampler"))
    texture_id.append(glGetUniformLocation(program_id, "myTextureSampler2"))

    tex1 = TextureLoader.load_texture("res/crate.jpg")
    tex2 = TextureLoader.load_texture("res/metal.jpg")
    # Our vertices. Tree consecutive floats give a 3D vertex; Three consecutive vertices give a triangle.
    # A cube has 6 faces with 2 triangles each, so this makes 6*2=12 triangles, and 12*3 vertices



    vertex_buffer = glGenBuffers(1);
    array_type = GLfloat * len(vertex_data)
    glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)
    glBufferData(GL_ARRAY_BUFFER, len(vertex_data) * 4, array_type(*vertex_data), GL_STATIC_DRAW)

    uv_buffer = glGenBuffers(1);
    array_type = GLfloat * len(uv_data)
    glBindBuffer(GL_ARRAY_BUFFER, uv_buffer)
    glBufferData(GL_ARRAY_BUFFER, len(uv_data) * 4, array_type(*uv_data), GL_STATIC_DRAW)

    # vsync and glfw do not play nice.  when vsync is enabled mouse movement is jittery.
    common.disable_vsyc()

    glUseProgram(program_id)

    #1rst attribute buffer : vertices
    glEnableVertexAttribArray(0)
    glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer);
    glVertexAttribPointer(
        0,                  # attribute 0. No particular reason for 0, but must match the layout in the shader.
        3,                  # len(vertex_data)
        GL_FLOAT,           # type
        GL_FALSE,           # ormalized?
        0,                  # stride
        null                # array buffer offset (c_type == void*)
        )

    # 2nd attribute buffer : colors
    glEnableVertexAttribArray(1)
    glBindBuffer(GL_ARRAY_BUFFER, uv_buffer);
    glVertexAttribPointer(
        1,                  # attribute 1. No particular reason for 1, but must match the layout in the shader.
        2,                  # len(vertex_data)
        GL_FLOAT,           # type
        GL_FALSE,           # ormalized?
        0,                  # stride
        null                # array buffer offset (c_type == void*)
        )

    glActiveTexture(GL_TEXTURE0);

    currentTexture = []
    for i in range(1, jumlah_tempat+1):
        currentTexture.append(TextureLoader.load_texture("img/building"+str(i)+".jpg"))

    while glfw.get_key(window,glfw.KEY_ESCAPE) != glfw.PRESS and not glfw.window_should_close(window):
        # Clear old render result
        glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)

        controls.computeMatricesFromInputs(window)
        ProjectionMatrix = controls.getProjectionMatrix();
        ViewMatrix = controls.getViewMatrix();
        ModelMatrix = mat4.identity();
        mvp = ProjectionMatrix * ViewMatrix * ModelMatrix;

        Display()

        ##################################################################### SET TEXTURE 1

        # Send our transformation to the currently bound shader,
        # in the "MVP" uniform
        # draws Aula barat, timur ; CC barat, timur

        # glBindTexture(GL_TEXTURE_2D, tex1);
        # glUniformMatrix4fv(matrix_id, 1, GL_FALSE,mvp.data)

        # # Draw the shapes
        # glDrawArrays(GL_TRIANGLES, 0, 12*3*4) #3 indices starting at 0 -> 1 triangle


        # ####################################################################### SET TEXTURE 2
        # #draws 4 labtek kembar + perpus, pau

        # glBindTexture(GL_TEXTURE_2D, tex2);
        # glUniformMatrix4fv(matrix_id, 1, GL_FALSE, mvp.data)

        # # Draw the shapes
        # glDrawArrays(GL_TRIANGLES, 12*3*4, 12*3*6) #3 indices starting at 0 -> 1 triangle
        # print (jumlah_tempat)

        for i in range(0, jumlah_tempat):
            # Send our transformation to the currently bound shader,
            # in the "MVP" uniform
            # draws Aula barat, timur ; CC barat, timur

            glBindTexture(GL_TEXTURE_2D, currentTexture[i]);
            glUniformMatrix4fv(matrix_id, 1, GL_FALSE,mvp.data)

            # # Draw the shapes
            glDrawArrays(GL_TRIANGLES, 12*3*i, 12*3) #3 indices starting at 0 -> 1 triangle

        ################################################### FINALIZE

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    # Not strictly necessary because we only have
    glDisableVertexAttribArray(0)
    glDisableVertexAttribArray(1)
    # !Note braces around vertex_buffer and uv_buffer.
    # glDeleteBuffers expects a list of buffers to delete
    glDeleteBuffers(1, [vertex_buffer])
    glDeleteBuffers(1, [uv_buffer])
    glDeleteProgram(program_id)
    glDeleteTextures([texture_id])
    glDeleteVertexArrays(1, [vertex_array_id])

    glfw.terminate()

if __name__ == "__main__":
    main()
