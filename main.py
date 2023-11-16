import glfw
from OpenGL.GL import *
import time

#-----------------------------Fondo-------------------------------------------

# Función para interpolar entre dos colores
def lerp_color(color_start, color_end, t):
    return color_start[0] + (color_end[0] - color_start[0]) * t, \
           color_start[1] + (color_end[1] - color_start[1]) * t, \
           color_start[2] + (color_end[2] - color_start[2]) * t

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

#-------------------------Piso-----------------------------------------------

def draw_rectangle(x, y, width, height, rotation, color):
    glPushMatrix()  # Guarda la matriz de transformación actual
    glTranslate(x, y, 0)  # Traslada el rectángulo a su posición
    glRotate(rotation, 0, 0, 1)  # Rota el rectángulo
    glColor3ub(*color)  # Establece el color
    
    # Dibuja el rectángulo con el centro en la posición actual
    glBegin(GL_QUADS)
    glVertex2f(-width / 2, -height / 2)
    glVertex2f(width / 2, -height / 2)
    glVertex2f(width / 2, height / 2)
    glVertex2f(-width / 2, height / 2)
    glEnd()
    
    glPopMatrix()  # Restaura la matriz de transformación

# Inicialización de GLFW
if not glfw.init():
    exit()

# Creación de la ventana con las dimensiones deseadas
window = glfw.create_window(1366, 1004, "Simulación del Cielo", None, None)

if not window:
    glfw.terminate()
    exit()

glfw.make_context_current(window)

start_time = time.time()

glViewport(0, 0, 1366, 1004)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, 1366, 0, 1004, -1, 1)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Loop principal
while not glfw.window_should_close(window):
    glfw.poll_events()

    # Piso
    # Convertir el color hexadecimal a RGB
    color_rectangulo = (122, 124, 49)  # Color hexadecimal #7A7C31 convertido a RGB
    # Dibuja el rectángulo para el piso
    draw_rectangle(683, 502, 1570.2, 617.4, 15.6, (122, 124, 49))

    # Calcular el tiempo transcurrido
    current_time = time.time() - start_time
    t = current_time / 30 # Normalizar el tiempo para la duración total de la animación

    if current_time <= duracion_amanecer:
        # Interpolar colores para el amanecer
        t_amanecer = current_time / duracion_amanecer
        color_actual = lerp_color(color_noche, color_amanecer, t_amanecer)
    elif current_time <= duracion_amanecer + duracion_dia:
        # Interpolar colores para el día
        t_dia = (current_time - duracion_amanecer) / duracion_dia
        color_actual = lerp_color(color_amanecer, color_dia, t_dia)
    elif current_time <= duracion_amanecer + duracion_dia + duracion_atardecer:
        # Interpolar colores para el atardecer
        t_atardecer = (current_time - duracion_amanecer - duracion_dia) / duracion_atardecer
        color_actual = lerp_color(color_dia, color_atardecer, t_atardecer)
    else:
        # Interpolar colores para la noche
        t_noche = (current_time - duracion_amanecer - duracion_dia - duracion_atardecer) / duracion_noche
        color_actual = lerp_color(color_atardecer, color_noche, t_noche)

    # Establecer el color de fondo actual
    glClearColor(*color_actual, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glfw.swap_buffers(window)

    # Terminar la animación después de 30 segundos
    if current_time >= 30:
        break

glfw.terminate()
