import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Encuentra la Figura Correcta")

BGFigurasYColores = pygame.image.load("assets/BGgameFYC.png")

# Colores
COLORS = {
    "Rojo": (165, 48, 48),
    "Verde": (117, 167, 67),
    "Azul": (79, 143, 186),
    "Amarillo": (232, 193, 112),
    "Morado": (64, 39, 81)
}

# Configuración del reloj
clock = pygame.time.Clock()
FPS = 60

# Fuente para el texto
font = pygame.font.Font(None, 36)

# Clase Figura
class Figura:
    def __init__(self, x, y, color, tipo):
        self.x = x
        self.y = y
        self.color = color
        self.tipo = tipo
        self.rect = pygame.Rect(x, y, 50, 50)

    def dibujar(self, pantalla):
        if self.tipo == "Circulo":
            pygame.draw.circle(pantalla, self.color, (self.x + 25, self.y + 25), 25)
            pygame.draw.circle(pantalla, (0, 0, 0), (self.x + 25, self.y + 25), 25, 2)  # Contorno negro
        elif self.tipo == "Cuadrado":
            pygame.draw.rect(pantalla, self.color, self.rect)
            pygame.draw.rect(pantalla, (0, 0, 0), self.rect, 2)  # Contorno negro
        elif self.tipo == "Triangulo":
            puntos = [(self.x + 25, self.y), (self.x, self.y + 50), (self.x + 50, self.y + 50)]
            pygame.draw.polygon(pantalla, self.color, puntos)
            pygame.draw.polygon(pantalla, (0, 0, 0), puntos, 2)  # Contorno negro
        elif self.tipo == "Rectangulo":
            pygame.draw.rect(pantalla, self.color, (self.x, self.y, 60, 40))
            pygame.draw.rect(pantalla, (0, 0, 0), (self.x, self.y, 60, 40), 2)  # Contorno negro
        elif self.tipo == "Rombo":
            puntos = [(self.x + 25, self.y), (self.x, self.y + 25), (self.x + 25, self.y + 50), (self.x + 50, self.y + 25)]
            pygame.draw.polygon(pantalla, self.color, puntos)
            pygame.draw.polygon(pantalla, (0, 0, 0), puntos, 2)  # Contorno negro
        elif self.tipo == "Estrella":
            puntos = [
                (self.x + 25, self.y),
                (self.x + 30, self.y + 20),
                (self.x + 50, self.y + 20),
                (self.x + 35, self.y + 30),
                (self.x + 40, self.y + 50),
                (self.x + 25, self.y + 40),
                (self.x + 10, self.y + 50),
                (self.x + 15, self.y + 30),
                (self.x, self.y + 20),
                (self.x + 20, self.y + 20)
            ]
            pygame.draw.polygon(pantalla, self.color, puntos)
            pygame.draw.polygon(pantalla, (0, 0, 0), puntos, 2)  # Contorno negro
        elif self.tipo == "Ovalo":
            pygame.draw.ellipse(pantalla, self.color, (self.x, self.y, 60, 40))
            pygame.draw.ellipse(pantalla, (0, 0, 0), (self.x, self.y, 60, 40), 2)  # Contorno negro

    def clicado(self, pos):
        if self.tipo == "Circulo":
            distancia = ((self.x + 25 - pos[0]) ** 2 + (self.y + 25 - pos[1]) ** 2) ** 0.5
            return distancia <= 25
        elif self.tipo == "Cuadrado":
            return self.rect.collidepoint(pos)
        elif self.tipo == "Triangulo":
            puntos = [(self.x + 25, self.y), (self.x, self.y + 50), (self.x + 50, self.y + 50)]
            return pygame.draw.polygon(screen, (0, 0, 0), puntos, 2).collidepoint(pos)
        elif self.tipo == "Rectangulo":
            return pygame.Rect(self.x, self.y, 60, 40).collidepoint(pos)
        elif self.tipo == "Rombo":
            puntos = [(self.x + 25, self.y), (self.x, self.y + 25), (self.x + 25, self.y + 50), (self.x + 50, self.y + 25)]
            return pygame.draw.polygon(screen, (0, 0, 0), puntos, 2).collidepoint(pos)
        elif self.tipo == "Estrella":
            puntos = [
                (self.x + 25, self.y),
                (self.x + 30, self.y + 20),
                (self.x + 50, self.y + 20),
                (self.x + 35, self.y + 30),
                (self.x + 40, self.y + 50),
                (self.x + 25, self.y + 40),
                (self.x + 10, self.y + 50),
                (self.x + 15, self.y + 30),
                (self.x, self.y + 20),
                (self.x + 20, self.y + 20)
            ]
            return pygame.draw.polygon(screen, (0, 0, 0), puntos, 2).collidepoint(pos)
        elif self.tipo == "Ovalo":
            return pygame.Rect(self.x, self.y, 60, 40).collidepoint(pos)

# Función principal del juego
def main():
    running = True
    nivel = 1
    puntaje = 0
    tiempo_limite = 5  # Tiempo inicial en segundos

    while running:
        # Generar figuras
        figuras = []
        for _ in range(nivel + 2):
            x = random.randint(50, WIDTH - 100)
            y = random.randint(50, HEIGHT - 100)
            color = random.choice(list(COLORS.values()))
            tipo = random.choice(["Circulo", "Cuadrado", "Triangulo", "Rectangulo", "Rombo", "Estrella", "Ovalo"])
            figuras.append(Figura(x, y, color, tipo))

        # Elegir figura objetivo
        objetivo = random.choice(figuras)
        nombre_color = [k for k, v in COLORS.items() if v == objetivo.color][0]

        # Identificar todas las figuras que coincidan con el objetivo
        figuras_objetivo = [figura for figura in figuras if figura.color == objetivo.color and figura.tipo == objetivo.tipo]

        objetivo_texto = f"Haz clic en un {objetivo.tipo} de color {nombre_color}"

        # Temporizador
        tiempo_restante = tiempo_limite
        inicio_nivel = pygame.time.get_ticks()

        # Ciclo del nivel
        while True:
            screen.blit(BGFigurasYColores, (0,0))

            # Calcular tiempo restante
            tiempo_actual = pygame.time.get_ticks()
            tiempo_restante = tiempo_limite - (tiempo_actual - inicio_nivel) / 1000

            if tiempo_restante <= 0:
                print("¡Tiempo agotado!")
                print(f"Puntaje final: {puntaje}")
                pygame.quit()
                sys.exit()

            # Dibujar texto
            texto = font.render(objetivo_texto, True, (0, 0, 0))
            screen.blit(texto, (20, 20))

            # Dibujar temporizador
            texto_tiempo = font.render(f"Tiempo restante: {int(tiempo_restante)} s", True, (255, 0, 0))
            screen.blit(texto_tiempo, (20, 60))

            # Dibujar figuras
            for figura in figuras:
                figura.dibujar(screen)

            # Manejo de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if any(figura.clicado(pos) for figura in figuras_objetivo):
                        puntaje += 1
                        nivel += 1
                        tiempo_limite += 1  # Incrementar tiempo límite con cada acierto
                        break
                    else:
                        print("¡Fallaste!")
                        print(f"Puntaje final: {puntaje}")
                        pygame.quit()
                        sys.exit()

            else:
                # Actualizar pantalla
                pygame.display.flip()
                clock.tick(FPS)
                continue
            break

if __name__ == "__main__":
    main()

