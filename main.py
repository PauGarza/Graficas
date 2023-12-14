import glfw
from OpenGL.GL import *
import time
from math import cos, sin, pi
import random

# Función para interpolar entre dos colores
def lerp_color(color_start, color_end, t):
    return tuple(color_start[i] + (color_end[i] - color_start[i]) * t for i in range(3))

# Colores para diferentes momentos del día
color_amanecer = (0.9, 0.5, 0.3)  # Colores del amanecer
color_dia = (0.54, 0.81, 0.92)    # Azul día claro
color_atardecer = (0.9, 0.6, 0.2) # Colores del atardecer
color_noche = (0.1, 0.1, 0.3)     # Azul oscuro de la noche

# Tiempos de inicio y duración de cada fase en segundos
duracion_amanecer = 5
duracion_dia = 10
duracion_atardecer = 5
duracion_noche = 10

def draw_rectangle(upper_left_x, upper_left_y, width, height, rotation, color):
    center_x = upper_left_x + width / 2
    center_y = upper_left_y + height / 2
    glPushMatrix()
    glTranslate(center_x, center_y, 0)
    glRotatef(rotation, 0, 0, 1)
    glColor4ub(color[0], color[1], color[2], color[3])  # Opacidad ya en el rango 0-255
    glBegin(GL_QUADS)
    glVertex2f(-width / 2, -height / 2)
    glVertex2f(width / 2, -height / 2)
    glVertex2f(width / 2, height / 2)
    glVertex2f(-width / 2, height / 2)
    glEnd()
    glPopMatrix()

def draw_circle(upper_left_x, upper_left_y, diameter, color):
    center_x = upper_left_x + diameter / 2
    center_y = upper_left_y + diameter / 2
    radius = diameter / 2
    num_segments = 100
    glPushMatrix()
    glTranslate(center_x, center_y, 0)
    glColor4ub(color[0], color[1], color[2], color[3])  # Opacidad ya en el rango 0-255
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)
    for i in range(num_segments + 1):
        angle = 2 * pi * i / num_segments
        glVertex2f(radius * cos(angle), radius * sin(angle))
    glEnd()
    glPopMatrix()

color_gold = (234, 185, 65, 255)

color_white = (255, 255, 255, 255)

def crea_sol(window_width, window_height, tiempo_actual):
    diametro_sol = 441  # El diámetro del sol según tu especificación
    color_gold = (234, 185, 65, 255)  # Asumiendo que ya tienes esta variable definida
    color_white = (255, 255, 255, 255)  # Asumiendo que ya tienes esta variable definida

    # No hacer nada durante los primeros 3 segundos
    if tiempo_actual <= 3:
        return
    
    # Ajustar el tiempo_actual para la lógica de animación después de los primeros 3 segundos
    tiempo_ajustado = tiempo_actual -3

    # Elige el color basado en el tiempo ajustado
    color_actual = color_gold if tiempo_ajustado <= 15 else color_white
    
    y_inicial = window_height  # Iniciar desde abajo
    y_final = -diametro_sol  # Mover hacia arriba más allá del límite superior para que desaparezca

    # Calcular la posición y en función del tiempo ajustado
    # Asegurarse de que el tiempo se reinicie después de cada ciclo de 15 segundos
    t = (tiempo_ajustado % 15) / 15  # Normalizar tiempo para el ciclo actual de 15 segundos
    y_actual = lerp(y_inicial, y_final, t)

    # Posición x del sol será el centro del cuadro
    x_actual = window_width / 2 - diametro_sol / 2

    # Dibuja el sol con la posición y color actuales
    draw_circle(x_actual, y_actual, diametro_sol, color_actual)

def lerp(start, end, t):
    # Interpolación lineal entre dos valores
    return start + t * (end - start)

bici_solida = (62,82,117,255) #3E5275
bici_pedal = (201, 84, 126,200) #C9547E
bici_llantas = (62, 53, 58,225) #3E353A

def crear_bici():
    # Rectángulos basados en los parámetros de las imágenes subidas
    # (x, y, ancho, alto, rotación, (color))
    rect_params = [
            (573.9, 454, 223.1, 13.4, 13.4, bici_solida),
            (738, 533.9, 138.1, 8.5, 67.9, bici_solida),
            (678.9, 523.2, 122.1, 9.8, 129.8, bici_solida),
            (691.2, 576.4, 139.3, 9.8, -166.6, bici_solida),
            (545.8, 501.9, 191.3, 14, 43.7, bici_solida),
            (553.3, 416.2, 50.4, 11.6, 102.3, bici_solida),
            (484.2, 481.8, 110.3, 10.5, -50, bici_solida),
            (765.7, 456.3, 50.4, 11.6, 102.3, bici_solida),
            (741.4, 426, 91.1, 24.5, 13.4, bici_solida),
            (683.3, 520.6, 18.6, 6.8, 13.4, bici_solida),
            (680.5, 543.3, 48.7, 6.7, 71.7, bici_solida),
            (568.1, 378.8, 33.8, 5.8, 102.3, bici_solida),
            (583.2, 349.6, 56.6, 6.7, 148.4, bici_solida),
            (632.2, 340.8, 56.6, 6.6, -168.6, bici_solida),
            # ... Añade aquí los demás parámetros de las imágenes restantes ...  
        ]
    #draw_circle(x, y, ancho, rotation, color)
    circ_params = [
            (412.7, 438.7, 174.3,  bici_llantas),
            (748.6, 518.7, 174.3,  bici_llantas),
            (681.5, 547.6, 52.6,  bici_pedal)
    ]
    # Dibujar todos los rectángulos
    for x, y, ancho, alto, rotar, color in rect_params:
        draw_rectangle(x, y, ancho, alto, rotar, color)
    # Dibujar todos los circulos
    for x, y, ancho, color in circ_params:
        draw_circle(x, y, ancho, color)

def lerp(start, end, t):
    return start + t * (end - start)

def crear_bici_animada(pos_inicial, tiempo_actual, tiempo_total=30):
    rect_params = [
            (573.9, 454, 223.1, 13.4, 13.4, bici_solida),
            (738, 533.9, 138.1, 8.5, 67.9, bici_solida),
            (678.9, 523.2, 122.1, 9.8, 129.8, bici_solida),
            (691.2, 576.4, 139.3, 9.8, -166.6, bici_solida),
            (545.8, 501.9, 191.3, 14, 43.7, bici_solida),
            (553.3, 416.2, 50.4, 11.6, 102.3, bici_solida),
            (484.2, 481.8, 110.3, 10.5, -50, bici_solida),
            (765.7, 456.3, 50.4, 11.6, 102.3, bici_solida),
            (741.4, 426, 91.1, 24.5, 13.4, bici_solida),
            (683.3, 520.6, 18.6, 6.8, 13.4, bici_solida),
            (680.5, 543.3, 48.7, 6.7, 71.7, bici_solida),
            (568.1, 378.8, 33.8, 5.8, 102.3, bici_solida),
            (583.2, 349.6, 56.6, 6.7, 148.4, bici_solida),
            (632.2, 340.8, 56.6, 6.6, -168.6, bici_solida),
            # ... Añade aquí los demás parámetros de las imágenes restantes ...  
        ]
    #draw_circle(x, y, ancho, rotation, color)
    circ_params = [
            (412.7, 438.7, 174.3,  bici_llantas),
            (748.6, 518.7, 174.3,  bici_llantas),
            (681.5, 547.6, 52.6,  bici_pedal)
    ]

    t = min(tiempo_actual / tiempo_total, 1)  # Asegurar que t está entre 0 y 1

    for params in rect_params:
        x_final, y_final = params[0], params[1]
        x = lerp(pos_inicial[0], x_final, t)
        y = lerp(pos_inicial[1], y_final, t)
        draw_rectangle(x, y, *params[2:])

    for params in circ_params:
        x_final, y_final = params[0], params[1]
        x = lerp(pos_inicial[0], x_final, t)
        y = lerp(pos_inicial[1], y_final, t)
        draw_circle(x, y, *params[2:])

def fig_random():
    figura = random.choice([True, False]) #0
    x_ini = random.uniform(0, 1366) #1
    y_ini = random.uniform(0, 1004) #2
    x_fin = random.uniform(0, 1366) #3
    y_fin = random.uniform(0, 1004) #4
    ancho = random.uniform(50, 100)   #5
    alto = random.uniform(50, 100)    #6
    rotar = random.uniform(-360, 360) #7   
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) #8 
    tiempo_ini =  random.uniform(1, 30) #9
    duracion =  30 - tiempo_ini
    return (figura, x_ini, y_ini, x_fin, y_fin, ancho, alto, rotar, color, tiempo_ini, duracion)
    
def trasladar_rectangulo(figura, x_inicial, y_inicial, x_final, y_final, ancho, alto, rotar, color, tiempo_inicio, tiempo_actual, duracion):

    if tiempo_actual < tiempo_inicio:
        # Si el tiempo actual es menor al tiempo de inicio, no hacer nada.
        return

    # Calcular el tiempo transcurrido desde el inicio de la animación.
    tiempo_transcurrido = tiempo_actual - tiempo_inicio
    
    # Normalizar el tiempo transcurrido a un valor entre 0 y 1.
    t = max(0, min(1, tiempo_transcurrido / duracion))

    # Calcular la nueva posición x e y del rectángulo mediante interpolación lineal.
    x_actual = x_inicial + (x_final - x_inicial) * t
    y_actual = y_inicial + (y_final - y_inicial) * t

    # Dibujar el figura en la nueva posición.
    if figura:
        draw_circle(x_actual, y_actual, ancho, color)
        if t >= 1:
            draw_circle(x_final, y_final, ancho, alto, rotar, color)
    else:
        draw_rectangle(x_actual, y_actual, ancho, alto, rotar, color)
        # Si la animación ha terminado, asegurarse de que el rectángulo esté en la posición final.
        if t >= 1:
            draw_rectangle(x_final, y_final, ancho, alto, rotar, color)

# Inicialización de GLFW
if not glfw.init():
    exit()

# Creación de la ventana con las dimensiones deseadas
window = glfw.create_window(1366, 1004, "Simulación del Cielo", None, None)



if not window:
    glfw.terminate()
    exit()

glfw.make_context_current(window)

# Configuración de la proyección ortográfica
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, 1366, 1004, 0, -1, 1)  # Se invierte el eje Y para que 0,0 esté en la esquina superior izquierda
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Habilitar blending para transparencia
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

start_time = time.time()

n = 40 
figuras = [0]*n

for i in range(n):
    figuras[i] = fig_random()

# Loop principal
while not glfw.window_should_close(window):
    glfw.poll_events()
    
    # Calcular el tiempo transcurrido
    current_time = time.time() - start_time
    t = current_time / 30  # Normalizar el tiempo para la duración total de la animación
    

    # Interpolación de colores para el fondo
    if current_time <= duracion_amanecer:
        color_actual = lerp_color(color_noche, color_amanecer, current_time / duracion_amanecer)
    elif current_time <= duracion_amanecer + duracion_dia:
        color_actual = lerp_color(color_amanecer, color_dia, (current_time - duracion_amanecer) / duracion_dia)
    elif current_time <= duracion_amanecer + duracion_dia + duracion_atardecer:
        color_actual = lerp_color(color_dia, color_atardecer, (current_time - duracion_amanecer - duracion_dia) / duracion_atardecer)
    else:
        color_actual = lerp_color(color_atardecer, color_noche, (current_time - duracion_amanecer - duracion_dia - duracion_atardecer) / duracion_noche)

    # Establecer el color de fondo actual
    glClearColor(*color_actual, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    crea_sol(1366, 1004, current_time)

    # Dibuja el rectángulo para el piso
    # x, y, ancho, alto, rotation, color
    draw_rectangle(106.8, 598.4, 1152.5, 187.4, 12.9, (122, 124, 49, 255) )

    crear_bici_animada((0, 271.2), current_time, 3)

    for fig in figuras:
        #(figura, x_ini, y_ini, x_fin, y_fin, ancho, alto, rotar, color, tiempo_ini, duracion)
        trasladar_rectangulo(
        figura=fig[0],
        x_inicial=fig[1], y_inicial=fig[2], 
        x_final=fig[3], y_final=fig[4], 
        ancho=fig[5], alto=fig[6], 
        rotar=fig[7],
        color=fig[8], 
        tiempo_inicio=fig[9], 
        tiempo_actual=current_time, 
        duracion=fig[10]
    )

    glfw.swap_buffers(window)

    # Terminar la animación después de 30 segundos
    if current_time >= 30:
        break

glfw.terminate()