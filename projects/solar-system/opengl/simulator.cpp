#include <GL/glew.h>

#ifdef __APPLE_CC__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

#include <iostream>
#include <sstream>
#include <fstream>
#include <cstring>
#include <cmath>

#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"

using namespace std;

int Loc3, Loc4, Loc5;

float rotationX = 0.0f, rotationY = 0.0f;
float zoomLevel = 20.0f;
int lastMouseX, lastMouseY;
bool isRotating = false;

class Vector 
{
    float values[4];
public:
    Vector(float a=0.0, float b=0.0, float c=0.0, float d=0.0) 
    {
        values[0] = a; values[1] = b; values[2] = c; values[3] = d;
    }
    float x() const { return values[0]; }
    float y() const { return values[1]; }
    float z() const { return values[2]; }
    float r() const { return values[0]; }
    float g() const { return values[1]; }
    float b() const { return values[2]; }
};

void setUniforms() 
{
    glUniform3f(Loc4, -2.0, -2.0, 1.0); // Light location
    glUniform3f(Loc5, 1.0, 0.84, 0.0); // Light color
}

GLuint loadTexture(const char* path) 
{
    GLuint texture;
    int width, height, nrChannels;
    stbi_set_flip_vertically_on_load(true);
    glGenTextures(1, &texture);

    glBindTexture(GL_TEXTURE_2D, texture);
    glActiveTexture(GL_TEXTURE_2D);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);

    unsigned char *data = stbi_load(path, &width, &height, &nrChannels, 0);

    if (data)
    {
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, data);
        glGenerateMipmap(GL_TEXTURE_2D);
    }
    else
    {
        cout << "Failed to load texture" << endl;
    }
    stbi_image_free(data);
    return texture;
}

class Body 
{
    const char* path;
    float r;
    float lum;
    unsigned int texture;
    Vector pos;
    Vector c;
    GLUquadric* quadric;

public:
    Body(const char* imgpath = "maps/earth.jpg",
         float radius = 1.0,
         float luminosity = 0.0,
         Vector position = Vector(0.0, 0.0, 0.0),
         Vector color = Vector(0.25, 0.25, 0.25)) {
        path = imgpath;
        r = radius;
        lum = luminosity;
        pos = position;
        c = color;
    }

    void render() 
    {
        glPushMatrix();
        glTranslatef(pos.x(), pos.y(), pos.z());

        GLuint texture = loadTexture(path);
        glRotatef(175.0f, 0.0f, 1.0f, 1.0f);
        glRotatef(90.f, 0.0f, 0.0f, 1.0f);

        quadric = gluNewQuadric();
        gluQuadricDrawStyle(quadric, GLU_FILL);
        gluQuadricTexture(quadric, GL_TRUE);
        gluQuadricNormals(quadric, GLU_SMOOTH);
        gluSphere(quadric, r, 40, 40);

        glPopMatrix();
    }

    ~Body() 
    {
        gluDeleteQuadric(quadric);
    }
};

Body sun("maps/sun.jpg", 2.0, 1.0, Vector(0.0, 0.0, 0.0), Vector(1.0, 0.84, 0.0));
Body earth("maps/earth.jpg", 1.0, 0.0, Vector(0.0, 0.0, 7.0), Vector(0.0, 0.25, 0.5));
Body moon("maps/moon.jpg", 0.3, 0.0, Vector(0.0, 0.0, 10.0), Vector(0.5, 0.5, 0.5));

void keyboard(unsigned char key, int x, int y) 
{
    if (key == 'w') 
    {
        zoomLevel -= 1.0f; // Zoom in
        if (zoomLevel < 2.0f) 
        {
            zoomLevel = 2.0f;
        }
    }
    if (key == 's') 
    {
        zoomLevel += 1.0f; // Zoom out
    }
    glutPostRedisplay();
}

void mouseButton(int button, int state, int x, int y) 
{
    if (button == GLUT_LEFT_BUTTON) 
    {
        isRotating = (state == GLUT_DOWN);
        lastMouseX = x;
        lastMouseY = y;
    }
}

void mouseMove(int x, int y) 
{
    if (isRotating) 
    {
        rotationX += (y - lastMouseY) * 0.5f;
        rotationY += (x - lastMouseX) * 0.5f;
        lastMouseX = x;
        lastMouseY = y;
        glutPostRedisplay();
    }
}

void setupProjection(float zoomLevel) 
{
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45.0, 800.0/600.0, 1.0, 200.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(0.0, 0.0, zoomLevel,
              0.0, 0.0, 0.0,
              0.0, 1.0, 0.0);
}

void display() 
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glLoadIdentity();
    gluLookAt(0.0, 0.0, zoomLevel,
              0.0, 0.0, 0.0,
              0.0, 1.0, 0.0);

    setupProjection(zoomLevel);

    glRotatef(rotationX, 1.0, 0.0, 0.0); // Rotate around x-axis
    glRotatef(rotationY, 0.0, 1.0, 0.0); // Rotate around y-axis

    setUniforms();

    sun.render();
    earth.render();
    moon.render();

    glFlush();
}

int main(int argc, char** argv) 
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowPosition(80, 80);
    glutInitWindowSize(800, 600);
    glutCreateWindow("Solar System Simulator");

    GLenum err = glewInit();
    if (err != GLEW_OK)
        exit(1);

    glutDisplayFunc(display);
    glutMouseFunc(mouseButton);
    glutMotionFunc(mouseMove);
    glutKeyboardFunc(keyboard);

    glEnable(GL_DEPTH_TEST);
    glEnable(GL_TEXTURE_2D);

    glutMainLoop();

    return 0;
}