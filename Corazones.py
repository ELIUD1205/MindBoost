import pygame

def main():
    pygame.init()

    # Configuración de pantalla
    size = (1280, 720)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Vidas con Corazones")
    clock = pygame.time.Clock()

    # Cargar imágenes de corazones
    corazon = pygame.image.load("assets/Heart.png").convert_alpha()
    corazon_tamaño = (50, 50)  # Tamaño de los corazones
    corazon = pygame.transform.scale(corazon, corazon_tamaño)
    corazon_vacio = pygame.image.load("assets/Heart-1.png").convert_alpha()
    corazon_vacio = pygame.transform.scale(corazon_vacio, corazon_tamaño)

    # Configuración de vidas
    max_vidas = 3
    vidas = max_vidas

    # Función para dibujar corazones
    def dibujar_vidas(vidas):
        for i in range(max_vidas):
            x = 50 + i * (corazon_tamaño[0] + 10)
            y = 50
            if i < vidas:
                screen.blit(corazon, (x, y))  # Corazón lleno
            else:
                screen.blit(corazon_vacio, (x, y))  # Corazón vacío

    # Bucle principal
    running = True
    while running:
        screen.fill((0, 0, 0))  # Fondo negro

        # Dibujar vidas
        dibujar_vidas(vidas)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and vidas > 0:  # Si se presiona "R"
                    vidas -= 1  # Reducir una vida

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
