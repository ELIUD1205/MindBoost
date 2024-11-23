import pygame
import random
import time

pygame.init()

# Configuración de pantalla
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Simón Dice")



# Cargar imágenes
imagenes = {
    "ROJO": pygame.image.load("assets/RED.png"),
    "VERDE": pygame.image.load("assets/GREEN.png"),
    "AZUL": pygame.image.load("assets/BLUE.png"),
    "AMARILLO": pygame.image.load("assets/YELLOW.png"),
}
imagenes_highlight = {
    "ROJO": pygame.image.load("assets/RED_SEC.png"),
    "VERDE": pygame.image.load("assets/GREEN_SEC.png"),
    "AZUL": pygame.image.load("assets/BLUE_SEC.png"),
    "AMARILLO": pygame.image.load("assets/YELLOW_SEC.png"),
}

# Botones y posiciones
botones = {
    "ROJO": pygame.Rect(50, 50, 200, 200),
    "VERDE": pygame.Rect(350, 50, 200, 200),
    "AZUL": pygame.Rect(50, 350, 200, 200),
    "AMARILLO": pygame.Rect(350, 350, 200, 200),
}
secuencia = []
player_secuencia = []

# Función para dibujar los botones con imágenes
def dibujar_botones(highlight=None):
    screen.fill("grey")
    for color, rect in botones.items():
        if highlight == color:
            # Dibujar la imagen resaltada si está seleccionada
            screen.blit(imagenes_highlight[color], rect)
        else:
            # Dibujar la imagen normal
            screen.blit(imagenes[color], rect)
    pygame.display.flip()

# Reproducir la secuencia mostrando los colores con imágenes resaltadas
def play_secuencia(seq):
    for color in seq:
        dibujar_botones(color)
        pygame.time.delay(500)
        dibujar_botones()
        pygame.time.delay(200)

# Añadir un color aleatorio a la secuencia
def añadir_color_random(seq):
    color = random.choice(list(botones.keys()))
    seq.append(color)

# Revisar si la secuencia del jugador es correcta
def revisar_player_secuencia():
    for i in range(len(player_secuencia)):
        if player_secuencia[i] != secuencia[i]:
            return False
    return True

# Función principal del juego
def main():
    running = True
    global player_secuencia
    añadir_color_random(secuencia)
    play_secuencia(secuencia)
    
    while running:
        dibujar_botones()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for color, rect in botones.items():
                    if rect.collidepoint(pos):
                        player_secuencia.append(color)
                        dibujar_botones(color)
                        pygame.time.delay(300)
                        dibujar_botones()
                        
                        # Verificar si la secuencia es correcta hasta ahora
                        if not revisar_player_secuencia():
                            print("Secuencia incorrecta! Intenta de nuevo.")
                            player_secuencia = []
                            pygame.time.delay(2000)
                            play_secuencia(secuencia)
                            pygame.time.delay(1000)
                        elif len(player_secuencia) == len(secuencia):
                            print("¡Secuencia correcta!")
                            player_secuencia = []
                            pygame.time.delay(2000)
                            añadir_color_random(secuencia)
                            play_secuencia(secuencia)
                            pygame.time.delay(1000)
                            
        pygame.display.flip()
    pygame.quit()

# Ejecutar el juego
if __name__ == "__main__":
    main()

                            
    

