import pygame
import sys
import json

# Inicialización de Pygame
pygame.init()

# Configuración de pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Top 5 Scores with Names")

# Fuente para texto
font = pygame.font.Font(None, 50)

# Archivo para guardar los puntajes
SCORES_FILE = "top_scores_with_names.json"

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Función para cargar los puntajes
def load_top_scores():
    try:
        with open(SCORES_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Si no hay archivo o está corrupto, devolver una lista inicial vacía
        return [{"name": "Empty", "score": 0} for _ in range(5)]

# Función para guardar los puntajes
def save_top_scores(top_scores):
    with open(SCORES_FILE, "w") as file:
        json.dump(top_scores, file)

# Cargar los puntajes iniciales
top_scores = load_top_scores()
current_score = 0

# Reloj para controlar FPS
clock = pygame.time.Clock()

# Función para obtener el sufijo adecuado
def get_position_suffix(position):
    if position == 1:
        return "st"
    elif position == 2:
        return "nd"
    elif position == 3:
        return "rd"
    else:
        return "th"

# Función para pedir el nombre del jugador
def get_player_name():
    name = ""
    running = True
    while running:
        screen.fill(WHITE)
        prompt_text = font.render("Enter your name (3 letters):", True, BLACK)
        screen.blit(prompt_text, (50, 200))

        # Dibujar el rectángulo para la entrada de texto
        input_rect = pygame.Rect(50, 300, 200, 50)
        pygame.draw.rect(screen, GRAY, input_rect, border_radius=10)  # Fondo del rectángulo
        pygame.draw.rect(screen, BLACK, input_rect, 3, border_radius=10)  # Contorno del rectángulo

        # Mostrar el nombre ingresado hasta ahora
        name_text = font.render(name, True, BLACK)
        screen.blit(name_text, (input_rect.x + 60, input_rect.y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(name) == 3:
                    running = False  # Terminar si ya se ingresaron 3 letras
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]  # Eliminar el último carácter
                elif len(name) < 3 and event.unicode.isalnum():
                    name += event.unicode.upper()  # Agregar la letra en mayúsculas
    return name

# Pedir el nombre del jugador
player_name = get_player_name()

# Bucle principal
running = True
while running:
    # Dibujar fondo
    screen.fill(WHITE)

    # Mostrar los puntajes
    title_text = font.render("Top 5 Scores:", True, BLACK)
    screen.blit(title_text, (50, 20))

    for i, entry in enumerate(top_scores):
        # Obtener el sufijo adecuado para la posición
        position_suffix = get_position_suffix(i + 1)
        score_text = font.render(f"{i + 1}{position_suffix} {entry['name']} - {entry['score']}", True, BLACK)
        screen.blit(score_text, (50, 80 + i * 50))

    current_score_text = font.render(f"Current Score: {current_score}", True, BLACK)
    screen.blit(current_score_text, (50, 400))

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Incrementar el puntaje actual
                current_score += 10

                # Verificar si entra en el Top 5
                if current_score > min(entry["score"] for entry in top_scores):
                    # Actualizar el Top 5
                    top_scores.append({"name": player_name, "score": current_score})
                    top_scores = sorted(top_scores, key=lambda x: x["score"], reverse=True)[:5]  # Ordenar y mantener solo los 5 mejores
                    save_top_scores(top_scores)

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(30)

# Salir del juego
pygame.quit()
sys.exit()



