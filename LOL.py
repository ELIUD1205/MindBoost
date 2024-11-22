import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de Pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Reflejos - Tap the Shape")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
FONDO_COLOR = (116, 86, 155)  # Color RGB equivalente a "#74569b"

# Cargar las imágenes
imagen1 = pygame.image.load("assets/Burbuja.png")  # Imagen original
imagen2 = pygame.image.load("assets/POP.png")  # Imagen de reemplazo temporal
imagen_actual = imagen1  # Imagen actual a mostrar
radio_inicial = imagen1.get_width() // 2  # Radio inicial basado en el ancho de la imagen
radio_minimo = 10  # Radio mínimo antes de desaparecer

# Configuración de tiempo de vida
tiempo_inicial = 10000  # Tiempo de vida inicial de la figura en ms
tiempo_vida = tiempo_inicial  # Tiempo de vida actual
puntaje = 0
radio_actual = radio_inicial

# Variables de estado
tiempo_inicio = pygame.time.get_ticks()
mostrar_reemplazo = False
tiempo_reemplazo = 250  # Tiempo en ms para mostrar la imagen de reemplazo
tiempo_cambio = None  # Guardar el tiempo en que se cambió la imagen

# Reloj de Pygame para controlar FPS
clock = pygame.time.Clock()

# Estado inicial
pos_circulo = (random.randint(radio_inicial, ANCHO - radio_inicial),
               random.randint(radio_inicial, ALTO - radio_inicial))

# Loop Principal
ejecutando = True
while ejecutando:
    pantalla.fill(FONDO_COLOR)

    # Manejar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            dist = ((x - pos_circulo[0]) ** 2 + (y - pos_circulo[1]) ** 2) ** 0.5
            if dist <= radio_actual:
                # Acierto, aumentar puntaje y reducir tiempo de vida
                puntaje += 1
                tiempo_vida = max(500, tiempo_vida - 100)
                
                # Cambiar temporalmente a la imagen de reemplazo
                mostrar_reemplazo = True
                tiempo_cambio = pygame.time.get_ticks()

    # Tiempo transcurrido
    tiempo_actual = pygame.time.get_ticks() - tiempo_inicio
    
    # Verificar si el jugador falló
    if tiempo_actual >= tiempo_vida:
        print("¡Perdiste!")
        puntaje = 0
        tiempo_vida = tiempo_inicial
        pos_circulo = (random.randint(radio_inicial, ANCHO - radio_inicial),
                       random.randint(radio_inicial, ALTO - radio_inicial))
        radio_actual = radio_inicial
        tiempo_inicio = pygame.time.get_ticks()

    # Si estamos mostrando la imagen de reemplazo, verificar el tiempo transcurrido
    if mostrar_reemplazo and tiempo_cambio:
        # Mostrar la imagen de reemplazo durante un tiempo limitado
        if pygame.time.get_ticks() - tiempo_cambio < tiempo_reemplazo:
            # Redimensionar la segunda imagen
            factor_tiempo = (pygame.time.get_ticks() - tiempo_inicio) / tiempo_vida
            radio_actual = max(radio_minimo, int(radio_inicial * (1 - factor_tiempo)))
            imagen_escalada = pygame.transform.scale(imagen2, (2 * radio_actual, 2 * radio_actual))
            pantalla.blit(imagen_escalada, imagen_escalada.get_rect(center=pos_circulo))
        else:
            # Volver a la imagen original y reiniciar la posición y tamaño
            mostrar_reemplazo = False
            pos_circulo = (random.randint(radio_inicial, ANCHO - radio_inicial),
                           random.randint(radio_inicial, ALTO - radio_inicial))
            radio_actual = radio_inicial
            tiempo_inicio = pygame.time.get_ticks()
    else:
        # Redimensionar y mostrar la imagen original si la imagen de reemplazo no está activa
        factor_tiempo = tiempo_actual / tiempo_vida
        radio_actual = max(radio_minimo, int(radio_inicial * (1 - factor_tiempo)))
        imagen_escalada = pygame.transform.scale(imagen1, (2 * radio_actual, 2 * radio_actual))
        pantalla.blit(imagen_escalada, imagen_escalada.get_rect(center=pos_circulo))

    # Mostrar puntaje
    fuente = pygame.font.Font(None, 36)
    texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, NEGRO)
    pantalla.blit(texto_puntaje, (10, 10))

    # Actualizar pantalla y mantener alta frecuencia de fotogramas
    pygame.display.flip()
    clock.tick(60)  # Mantener 60 FPS

# Salir de Pygame
pygame.quit()
