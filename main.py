import glfw
from OpenGL.GL import *
import time
from math import cos, sin, pi

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

# Función para dibujar un rectángulo
def draw_rectangle(upper_left_x, upper_left_y, width, height, rotation, color):
    # Calcular el centro del rectángulo
    center_x = upper_left_x + width / 2
    center_y = upper_left_y + height / 2

    glPushMatrix()
    # Trasladar al centro para rotación
    glTranslate(center_x, center_y, 0)
    # Rotar alrededor del centro del rectángulo
    glRotatef(rotation, 0, 0, 1)
    # Establecer color y opacidad
    glColor4ub(color[0], color[1], color[2], int(color[3] * 255 / 100))
    # Dibujar rectángulo con el centro en el origen
    glBegin(GL_QUADS)
    glVertex2f(-width / 2, -height / 2)
    glVertex2f(width / 2, -height / 2)
    glVertex2f(width / 2, height / 2)
    glVertex2f(-width / 2, height / 2)
    glEnd()

    glPopMatrix()



# Función para dibujar un círculo
def draw_circle(x, y, ancho, rotation, color):
    radius = ancho/2
    num_segments = 100  # Cantidad de triángulos para aproximar el círculo
    angle = 2 * pi / num_segments  # Ángulo entre cada segmento

    glPushMatrix()
    glTranslate(x, y, 0)  # Mover al centro del círculo
    glRotatef(rotation, 0, 0, 1)  # Rotar alrededor del centro del círculo
    glColor4ub(*color)

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)  # Centro del círculo
    for i in range(num_segments + 1):
        glVertex2f(radius * cos(i * angle), radius * sin(i * angle))
    glEnd()

    glPopMatrix()

def crear_bici():
    # Rectángulos basados en los parámetros de las imágenes subidas
    # (x, y, ancho, alto, rotación, (color))
    rect_params = [
        (586.3, 428.2, 215.6, 9.9, 13.4, (0,0,0, 100)),
        (785, 472.5, 138.1, 8.5, 67.9, (0,0,0, 255)),
        (782.8, 484.3, 122.1, 9.8, 129.8, (0,0,0, 255)),
        (827.4, 602.2, 139.3, 9.8, -166.6, (0,0,0, 255)),
        (588.5, 448.6, 175.6, 11.2, 43.7, (0,0,0, 255)),
        (589.6, 398.6, 50.4, 11.6, 102.3, (0,0,0, 255)),
        (499.9, 525.9, 110.3, 10.5, -50, (0,0,0, 255)),
        (802, 437.7, 50.4, 11.6, 102.3, (0,0,0, 255)),
        (745.5, 415.7, 91.1, 24.5, 13.4, (0,0,0, 255)),
        (684.4, 518.5, 18.6, 6.8, 13.4, (0,0,0, 255)),
        (700.5, 522.5, 48.7, 6.7, 71.7, (0,0,0, 255)),
        (591.4, 365.8, 33.8, 5.8, 102.3, (0,0,0, 255)),
        (637.4, 341, 56.6, 6.7, 148.4, (0,0,0, 255)),
        (687.6, 352.9, 56.6, 6.6, -168.6, (0,0,0, 255)),
        # ... Añade aquí los demás parámetros de las imágenes restantes ...
      
    ]
      # Dibujar todos los rectángulos
    for x, y, ancho, alto, rotar, color in rect_params:
        draw_rectangle(x, y, ancho, alto, rotar, color)



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

start_time = time.time()

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

    # Dibuja el rectángulo para el piso
    # x, y, ancho, alto, rotation, color
    draw_rectangle(142.3, 472, 1152.5, 187.4, 12.9, (122, 124, 49, 255) )

    crear_bici()

    glfw.swap_buffers(window)

    # Terminar la animación después de 30 segundos
    if current_time >= 30:
        break

glfw.terminate()
