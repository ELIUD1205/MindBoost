import pygame
import random
import os

# Inicializar Pygame y el mezclador
pygame.init()
pygame.mixer.init()

# Configuración general
CARPETA_MUSICA = "musica"  # Carpeta donde se almacenan las canciones
VOLUMEN_INICIAL = 0.5      # Volumen inicial (0.0 a 1.0)

# Cargar canciones automáticamente desde la carpeta
playlist = [
    os.path.join(CARPETA_MUSICA, archivo) 
    for archivo in os.listdir(CARPETA_MUSICA) 
    if archivo.endswith((".ogg", ".wav", ".mp3"))
]

if not playlist:
    print("No se encontraron canciones en la carpeta especificada.")
    pygame.quit()
    exit()

# Mezclar la playlist aleatoriamente
random.shuffle(playlist)

# Configurar volumen
pygame.mixer.music.set_volume(VOLUMEN_INICIAL)
print(f"Volumen inicial: {VOLUMEN_INICIAL * 100}%")

# Configurar evento para detectar fin de la canción
pygame.mixer.music.set_endevent(pygame.USEREVENT)

# Función para reproducir la playlist
def reproducir_playlist(playlist):
    if len(playlist) > 0:
        cancion_actual = playlist.pop(0)  # Obtener la primera canción
        pygame.mixer.music.load(cancion_actual)
        pygame.mixer.music.play()
        print(f"Reproduciendo: {cancion_actual}")
    else:
        # Reiniciar playlist y mezclar nuevamente
        print("Fin de la playlist. Reiniciando...")
        playlist.extend(original_playlist)  # Restaurar la playlist original
        random.shuffle(playlist)           # Mezclar nuevamente
        reproducir_playlist(playlist)

# Guardar una copia de la playlist original para reiniciar
original_playlist = playlist[:]

# Comenzar con la primera canción
reproducir_playlist(playlist)

# Loop principal del programa
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Saliendo del programa...")
            running = False
            pygame.mixer.music.stop()  # Detener música al salir

        elif event.type == pygame.USEREVENT:  # Canción terminada
            reproducir_playlist(playlist)

    # Opcional: manejar comandos de usuario para ajustes de volumen
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:  # Subir volumen
        current_volume = pygame.mixer.music.get_volume()
        new_volume = min(current_volume + 0.1, 1.0)  # Máximo 1.0
        pygame.mixer.music.set_volume(new_volume)
        print(f"Volumen: {new_volume * 100:.0f}%")

    if keys[pygame.K_DOWN]:  # Bajar volumen
        current_volume = pygame.mixer.music.get_volume()
        new_volume = max(current_volume - 0.1, 0.0)  # Mínimo 0.0
        pygame.mixer.music.set_volume(new_volume)
        print(f"Volumen: {new_volume * 100:.0f}%")

pygame.quit()


