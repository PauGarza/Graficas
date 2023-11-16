import glfw
from OpenGL.GL import *

def main():
    # Inicialización de GLFW
    if not glfw.init():
        return

    # Creación de la ventana con las dimensiones deseadas
    window = glfw.create_window(1366, 1004, "Ventana OpenGL", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    # Configuración del viewport y la proyección ortográfica
    glViewport(0, 0, 1366, 1004)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 1366, 0, 1004, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Color de fondo convertido de HEX #54B6EB a valores de 0 a 1
    glClearColor(84/255, 182/255, 235/255, 1)

    # Loop principal
    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)

        # Dibujo de un rectángulo que cubra toda la pantalla como fondo
        glColor3f(84/255, 182/255, 235/255)  # Color del rectángulo
        glBegin(GL_QUADS)
        glVertex2f(0, 0)
        glVertex2f(1366, 0)
        glVertex2f(1366, 1004)
        glVertex2f(0, 1004)
        glEnd()

        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
