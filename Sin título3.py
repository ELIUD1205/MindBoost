# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 16:40:20 2024

@author: HP
"""

import pygame
import random
import time

pygame.init()

# Configuración de pantalla
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Simón Dice")

# Colores
Blanco = (255, 255, 255)
Negro = (0, 0, 0)
Rojo = (255, 0, 0)
Verde = (0, 255, 0)
Azul = (0, 0, 255)
Amarillo = (255, 255, 0)

# Botones
botones = {
    "ROJO": pygame.Rect(50, 50, 200, 200),
    "VERDE": pygame.Rect(350, 50, 200, 200),
    "AZUL": pygame.Rect(50, 350, 200, 200),
    "AMARILLO": pygame.Rect(350, 350, 200, 200)
}
colores = {"ROJO": Rojo, "VERDE": Verde, "AZUL": Azul, "AMARILLO": Amarillo}
secuencia = []
player_secuencia = []

# Función para dibujar los botones
def dibujar_botones(highlight=None):
    screen.fill(Negro)
    for color, rect in botones.items():
        pygame.draw.rect(screen, colores[color] if highlight != color else Blanco, rect)
    pygame.display.flip()

# Reproducir la secuencia mostrando los colores
def play_secuencia(seq):
    for color in seq:
        dibujar_botones(color)
        pygame.time.delay(500)
        dibujar_botones()
        pygame.time.delay(200)

# Añadir un color aleatorio a la secuencia
def añadir_color_random(seq):
    color = random.choice(list(colores.keys()))
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
                            play_secuencia(secuencia)
                            pygame.time.delay(500)
                        elif len(player_secuencia) == len(secuencia):
                            print("¡Secuencia correcta!")
                            player_secuencia = []
                            añadir_color_random(secuencia)
                            play_secuencia(secuencia)
                            pygame.time.delay(500)
                            
        pygame.display.flip()
    pygame.quit()

# Ejecutar el juego
if __name__ == "__main__":
    main()

                            
    

