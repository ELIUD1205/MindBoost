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
        self.font = pygame.font.Font("assets/font.ttf", 80)  # Ajusta la ruta si es necesario
        self.text = "LOADING..."
        self.text_rect = None  # Será inicializado al renderizar el texto

        # Configuración de la barra
        self.bar_width = 80
        self.bar_height = 60
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

    def render_text_with_outline(self, text, font, text_color, outline_color, x, y):
        """Renderiza un texto con un contorno alrededor."""
        # Renderizar texto con el color del borde
        outline_surface = font.render(text, True, outline_color)
        outline_rect = outline_surface.get_rect(center=(x, y))

        # Dibujar el contorno en todas las direcciones
        offsets = [(-8, 0), (8, 0), (0, -8), (0, 8), (-8, -8), (8, -8), (-8, 8), (8, 8)]
        for dx, dy in offsets:
            self.screen.blit(outline_surface, outline_rect.move(dx, dy))

        # Dibujar el texto principal en el centro
        text_surface = font.render(text, True, text_color)
        self.screen.blit(text_surface, outline_rect)

    def draw(self):
        """Dibuja la barra de carga y el texto."""
        elapsed_time = time.time() - self.start_time
        filled_segments = min(int(elapsed_time / self.time_per_segment), self.segments)

        # Dibujar fondo
        if self.bg_image:
            self.screen.blit(self.bg_image, (0, 0))
        else:
            self.screen.fill((255, 255, 255))  # Fondo blanco si no hay imagen

        # Mostrar texto "Loading..." con contorno
        if not self.text_rect:  # Solo calcular el rectángulo una vez
            self.text_rect = self.font.render(self.text, True, self.text_color).get_rect(
                center=(self.screen.get_width() // 2, 275)
            )
        self.render_text_with_outline(self.text, self.font, self.text_color, (0, 0, 0), self.text_rect.centerx, self.text_rect.centery)

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



