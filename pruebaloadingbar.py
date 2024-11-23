# main.py
import pygame
from utils.loadingbar import LoadingBar  # Importar la clase LoadingBar

# Configuración de Pygame
pygame.init()

# Crear la ventana
screen = pygame.display.set_mode((1280, 600))
pygame.display.set_caption("Barra de Carga con Degradado")

# Cargar una imagen de fondo (opcional)
bg_image = pygame.image.load("assets/FondoMainMenu.png")  # Si tienes una imagen de fondo

# Crear una instancia de la clase LoadingBar
loading_bar = LoadingBar(screen, bg_image, start_color=(255, 212, 163), end_color=(208, 129, 89), text_color=(255, 255, 255), loading_time=5, segments=10)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Salir si se cierra la ventana
            running = False

    # Dibujar la barra de carga
    if loading_bar.draw():
        running = False  # Detener el bucle principal cuando la barra esté llena

    # Esperar un poco para que el evento de carga se vea
    pygame.time.wait(100)

# Finalizar Pygame
pygame.quit()
