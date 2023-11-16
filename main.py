import glfw
from OpenGL.GL import *
import time

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
def draw_rectangle(x, y, width, height, rotation, color):
    glPushMatrix()
    glTranslate(x + width / 2, y + height / 2, 0)  # Mover al centro del rectángulo
    glRotatef(rotation, 0, 0, 1)  # Rotar alrededor del centro del rectángulo
    glColor3ub(*color)
    
    # Dibujar rectángulo
    glBegin(GL_QUADS)
    glVertex2f(-width / 2, -height / 2)
    glVertex2f(width / 2, -height / 2)
    glVertex2f(width / 2, height / 2)
    glVertex2f(-width / 2, height / 2)
    glEnd()
    
    glPopMatrix()

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
    draw_rectangle(683 - 1570.2 / 2, 502 - 617.4 / 2, 1570.2, 617.4, 15.6, (122, 124, 49))

    glfw.swap_buffers(window)

    # Terminar la animación después de 30 segundos
    if current_time >= 30:
        break

glfw.terminate()
