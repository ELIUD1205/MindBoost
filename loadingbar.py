import pygame
import time

class LoadingBar:
    def __init__(self, screen, bg_image, start_color, end_color, text_color, loading_time=5, segments=10):
        # Inicialización de variables
        self.screen = screen
        self.bg_image = bg_image
        self.start_color = start_color
        self.end_color = end_color
        self.text_color = text_color
        self.loading_time = loading_time
        self.segments = segments

        # Fuente para el texto de carga
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render("Loading...", True, self.text_color)
        self.text_rect = self.text.get_rect(center=(screen.get_width() // 2, 200))

        # Configuración de la barra
        self.bar_width = 60
        self.bar_height = 40
        self.gap = 10

        # Coordenadas de la barra
        self.bar_x_start = (screen.get_width() - (self.segments * self.bar_width + (self.segments - 1) * self.gap)) // 2
        self.bar_y = (screen.get_height() - self.bar_height) // 2

        # Tiempo por segmento
        self.time_per_segment = self.loading_time / self.segments
        self.start_time = time.time()

    def interpolate_color(self, start_color, end_color, t):
        """Interpela entre start_color y end_color usando el valor t (0 a 1)."""
        r = start_color[0] + (end_color[0] - start_color[0]) * t
        g = start_color[1] + (end_color[1] - start_color[1]) * t
        b = start_color[2] + (end_color[2] - start_color[2]) * t
        return (int(r), int(g), int(b))

    def draw(self):
        """Dibuja la barra de carga y el texto."""
        elapsed_time = time.time() - self.start_time
        filled_segments = min(int(elapsed_time / self.time_per_segment), self.segments)

        # Dibujar fondo
        if self.bg_image:
            self.screen.blit(self.bg_image, (0, 0))
        else:
            self.screen.fill((255, 255, 255))  # Fondo blanco si no hay imagen

        # Mostrar texto "Cargando..."
        self.screen.blit(self.text, self.text_rect)

        # Dibujar los segmentos de la barra
        for i in range(self.segments):
            # Coordenada X del segmento actual
            x = self.bar_x_start + i * (self.bar_width + self.gap)

            # Calcular el progreso del segmento actual (0 a 1)
            progress = i / (self.segments - 1) if self.segments > 1 else 1

            # Cambiar color gradualmente dependiendo del progreso del segmento
            color = self.interpolate_color(self.start_color, self.end_color, progress)

            # Dibujar segmentos llenos con el color interpolado
            if i < filled_segments:
                pygame.draw.rect(self.screen, color, (x, self.bar_y, self.bar_width, self.bar_height))
            else:
                # Los segmentos vacíos se muestran grises
                pygame.draw.rect(self.screen, (100, 100, 100), (x, self.bar_y, self.bar_width, self.bar_height))

        # Actualizar la pantalla
        pygame.display.flip()

        # Detener cuando todos los segmentos estén llenos
        return filled_segments >= self.segments

# --- Ejemplo de cómo llamar a la clase y usarla en otro código ---

# Inicialización de Pygame
pygame.init()

# Configurar la ventana
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Barra de Carga con Degradado")

# Definir los colores y la imagen de fondo (puedes cambiar el color o añadir una imagen de fondo)
START_COLOR = (255, 212, 163)  # Color inicial (Rojo claro)
END_COLOR = (208, 129, 89)    # Color final (Naranja)
TEXT_COLOR = (255, 255, 255)   # Color del texto (Blanco)

# Cargar una imagen de fondo (opcional)
try:
    bg_image = pygame.image.load("assets/FondoMainMenu.png")  # Si tienes una imagen de fondo
except pygame.error:
    bg_image = None  # Si no tienes una imagen, se usará un fondo blanco

# Crear una instancia de la clase LoadingBar
loading_bar = LoadingBar(screen, bg_image, start_color=(255, 212, 163), end_color=(208, 129, 89), text_color=(255, 255, 255) , loading_time=5, segments=10)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Salir si se cierra la ventana
            running = False

    # Dibujar la barra de carga
    if loading_bar.draw():
        running = False  # Salir cuando la barra esté llena

    # Esperar un poco para que el evento de carga se vea
    pygame.time.wait(100)

# Finalizar Pygame
pygame.quit()


