# -*- coding: utf-8 -*-
from OpenGL.GL import *
import time,sys, math
from math import sin,cos,sqrt
import random
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

fAspect = 1.0;
global aviao
aviao = [0,0]

global velocidade
velocidade = 0

global rotacao
rotacao = 0

global ponto_base
ponto_base = [500,200]

global viwer
viwer = [-100,250,1200]


def desenha_aviao3D():
    global aviao
    global rotacao
    global velocidade
    global ponto_base
    
    
    
    glTranslatef(ponto_base[0],ponto_base[1],0) 
    glRotatef(rotacao, 0, 0, 1)
    glTranslatef(-ponto_base[0],-ponto_base[1],0) 
    
    x = (velocidade*-1) * math.cos((rotacao*math.pi)/180)
    y = (velocidade*-1) * math.sin((rotacao*math.pi)/180)
    
    if int(ponto_base[1]+ y) in (range(-50,50)) and int(ponto_base[0]+ x) in (range(-50,50)):
        print 'colisao'
        
    else:
        ponto_base[0]+= x
        ponto_base[1]+= y
    
    glTranslatef(ponto_base[0],ponto_base[1],0) 
    
    glTranslatef(x,y,0) 
    
    
    glBegin(GL_QUADS)
    #/* Fundo */
    glColor3f(1, 0, 0);
    glVertex3f(0,0,-1);
    glVertex3f(0,0,1);
    glVertex3f(50,0,5);
    glVertex3f(50,0,-5);
    
    glColor3f(0,1,0);
    #frente superior
    glVertex3f(0,0,-1);
    glVertex3f(0,0,1);
    glVertex3f(10,10,4);
    glVertex3f(10,10,-4);
    
    #frente lateral esquerda
    glColor3f(1,1,0);
    glVertex3f(0,0,1);
    glVertex3f(9,0,1.7);
    glVertex3f(10,10,4);
    glVertex3f(0,0,1);
    
    #frente lateral direita
    glColor3f(1,1,0);
    glVertex3f(0,0,-1);
    glVertex3f(9,0,-1.7);
    glVertex3f(10,10,-4);
    glVertex3f(0,0,-1);
    
    #lateral esquerda
    glColor3f(0,0,1);
    glVertex3f(9,0,1.7);
    glVertex3f(50,0,5);
    glVertex3f(50,10,5);
    glVertex3f(10,10,4);
    
    #lateral esquerda
    glColor3f(0,0,1);
    glVertex3f(9,0,-1.7);
    glVertex3f(50,0,-5);
    glVertex3f(50,10,-5);
    glVertex3f(10,10,-4);
    
    #fundos
    glColor3f(0,1,0);
    glVertex3f(50,0,5);
    glVertex3f(50,0,-5);
    glVertex3f(50,10,-5);
    glVertex3f(50,10,5);
    
    #asas
    glColor3f(1,0,1);
    glVertex3f(10,10,-4);
    glVertex3f(10,10,4);
    glVertex3f(50,10,30);
    glVertex3f(50,10,-30);
    
    glEnd();
    
    
# Função callback de redesenho da janela de visualização
def Desenha():
    # Limpa a janela de visualização com a cor  
    # de fundo definida previamente
    glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT);
    
    # Altera a cor do desenho para preto
    glColor3f(0.5, 0.0, 1.0);
    glutSolidCube(100);
    glColor3f(1.0, 1.0, 0.0);
    
    
    glPushMatrix();
    desenha_aviao3D()
    glPopMatrix();
    
    # Função da GLUT para fazer o desenho de um cubo 
    # com a cor corrente
    
    
        
    # Executa os comandos OpenGL
    glutSwapBuffers();


# Função usada para especificar o volume de visualização
def EspecificaParametrosVisualizacao():

    # Especifica sistema de coordenadas de projeção
    glMatrixMode(GL_PROJECTION);
    # Inicializa sistema de coordenadas de projeção
    glLoadIdentity();

    # Especifica a projeção perspectiva(angulo,aspecto,zMin,zMax)
    gluPerspective(60,fAspect,100,1500);

    # Especifica sistema de coordenadas do modelo
    glMatrixMode(GL_MODELVIEW);
    # Inicializa sistema de coordenadas do modelo
    glLoadIdentity();
    # Especifica posição do observador e do alvo
    global viwer
    gluLookAt(viwer[0],viwer[1],viwer[2], 0,0,0, 0,1,0);


# Função callback chamada quando o tamanho da janela é alterado 
def AlteraTamanhoJanela( w, h):

    # Para previnir uma divisão por zero
    if ( h == 0 ):
        h = 1;

    # Especifica as dimensões da viewport
    glViewport(0, 0, w, h);
 
    # Calcula a correção de aspecto
    fAspect = w/h;

    EspecificaParametrosVisualizacao();


# Função callback chamada para gerenciar eventos de teclas
def Teclado (key,  x,  y):
    if (key == 'e'):
        exit(0);
    global rotacao
    global velocidade
    global viwer
    
    if key == 'w':
        rotacao += 1
    if key == 's':
        rotacao -= 1
    if key == 'd':
        velocidade += 1
    if key == 'a' and velocidade > 0:
        velocidade -= 1    
    
    if key == 'u':
        viwer[0] +=10
    if key == 'i':
        viwer[1] +=10
    if key == 'o':
        viwer[2] +=10
    
    if key == 'j':
        viwer[0] -=10
    if key == 'k':
        viwer[1] -=10
    if key == 'l':
        viwer[2] -=10
    
      


# Função responsável por inicializar parâmetros e variáveis
def Inicializa (void):
   
    # Define a cor de fundo da janela de visualização como preto
    glClearColor(0.0, 0.0, 0.0, 0.0);
    glLineWidth(2.0);

# Função callback chamada pela GLUT a cada intervalo de tempo
def Animacao(value):
    EspecificaParametrosVisualizacao()
    glutPostRedisplay();
    glutTimerFunc(60,Animacao, 1);

# Programa Principal 
def main(void):
    glutInit(sys.argv)
    # Define do modo de operação da GLUT
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH); 

    # Especifica a posição inicial da janela GLUT
    glutInitWindowPosition(5,5); 

    # Especifica o tamanho inicial em pixels da janela GLUT
    glutInitWindowSize(1000,600); 
 
    # Cria a janela passando como argumento o título da mesma
    glutCreateWindow("Avião 3D");

    # Registra a função callback de redesenho da janela de visualização
    glutDisplayFunc(Desenha);
    glEnable(GL_DEPTH_TEST);
    #Registra a função callback que será chamada a cada intervalo de tempo
    glutTimerFunc(60, Animacao, 1);

    # Registra a função callback de redimensionamento da janela de visualização
    glutReshapeFunc(AlteraTamanhoJanela);

    # Registra a função callback para tratamento das teclas ASCII
    glutKeyboardFunc (Teclado);

    # Chama a função responsável por fazer as inicializações 
    Inicializa(1);
 
    # Inicia o processamento e aguarda interações do usuário
    glutMainLoop()
    
    glutLeaveMainLoop()

    return 0;

main(1)
