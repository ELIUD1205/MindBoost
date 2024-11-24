import pygame
import random

def main():
    pygame.init()

    # Configuración de pantalla
    size = (1280, 720)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Simón Dice")
    clock = pygame.time.Clock()  # Para limitar los FPS

    # Configuración de colores
    fondo_color = pygame.image.load("assets/BGSimonDicePlay.png").convert()  # Cambia aquí el color del fondo

    # Cargar imágenes
    imagenes = {
        "ROJO": pygame.image.load("assets/RED.png").convert(),
        "VERDE": pygame.image.load("assets/GREEN.png").convert(),
        "AZUL": pygame.image.load("assets/BLUE.png").convert(),
        "AMARILLO": pygame.image.load("assets/YELLOW.png").convert(),
    }
    imagenes_highlight = {
        "ROJO": pygame.image.load("assets/RED_SEC.png").convert(),
        "VERDE": pygame.image.load("assets/GREEN_SEC.png").convert(),
        "AZUL": pygame.image.load("assets/BLUE_SEC.png").convert(),
        "AMARILLO": pygame.image.load("assets/YELLOW_SEC.png").convert(),
    }


    # Tamaño de los botones y posiciones
    boton_tamaño = 200
    espacio = 50
    inicio_x = (size[0] - (2 * boton_tamaño + espacio)) // 2
    inicio_y = (size[1] - (2 * boton_tamaño + espacio)) // 2

    botones = {
        "ROJO": pygame.Rect(inicio_x, inicio_y, boton_tamaño, boton_tamaño),
        "VERDE": pygame.Rect(inicio_x + boton_tamaño + espacio, inicio_y, boton_tamaño, boton_tamaño),
        "AZUL": pygame.Rect(inicio_x, inicio_y + boton_tamaño + espacio, boton_tamaño, boton_tamaño),
        "AMARILLO": pygame.Rect(inicio_x + boton_tamaño + espacio, inicio_y + boton_tamaño + espacio, boton_tamaño, boton_tamaño),
    }

    secuencia = []
    player_secuencia = []
    inicio_juego = True  # Para manejar la pausa inicial
    inicio_tiempo = pygame.time.get_ticks()  # Capturar tiempo inicial

    def dibujar_botones(highlight=None):
        screen.blit(fondo_color, (0,0))  # Cambiar el color del fondo aquí
        for color, rect in botones.items():
            if highlight == color:
                screen.blit(imagenes_highlight[color], rect)
            else:
                screen.blit(imagenes[color], rect)
        pygame.display.update([rect for rect in botones.values()])
        pygame.display.flip()

    def play_secuencia(seq):
        for color in seq:
            dibujar_botones(color)
            pygame.time.delay(500)
            dibujar_botones()
            pygame.time.delay(200)

    def añadir_color_random(seq):
        color = random.choice(list(botones.keys()))
        seq.append(color)

    def revisar_player_secuencia():
        for i in range(len(player_secuencia)):
            if player_secuencia[i] != secuencia[i]:
                return False
        return True

    añadir_color_random(secuencia)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif not inicio_juego and event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for color, rect in botones.items():
                    if rect.collidepoint(pos):
                        player_secuencia.append(color)
                        dibujar_botones(color)
                        pygame.time.delay(300)
                        dibujar_botones()

                        if not revisar_player_secuencia():
                            print("Secuencia incorrecta! Intenta de nuevo.")
                            player_secuencia = []
                            pygame.time.delay(2000)
                            play_secuencia(secuencia)
                        elif len(player_secuencia) == len(secuencia):
                            print("¡Secuencia correcta!")
                            player_secuencia = []
                            pygame.time.delay(2000)
                            añadir_color_random(secuencia)
                            play_secuencia(secuencia)

        if inicio_juego:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - inicio_tiempo > 2000:
                inicio_juego = False
                play_secuencia(secuencia)
        
        dibujar_botones()
        clock.tick(60)  # Limitar FPS a 60

main()



                            
    

