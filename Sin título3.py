import pygame
import random

class SimonDiceGame:
    def __init__(self):
        # Inicialización de Pygame
        pygame.init()
        self.size = (1280, 800)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Simón Dice")
        self.clock = pygame.time.Clock()
        
        # Configuración de juego
        self.score = 0
        self.vidas = 3
        self.max_vidas = 3
        self.secuencia = []
        self.player_secuencia = []
        self.inicio_juego = True
        self.inicio_tiempo = pygame.time.get_ticks()
        
        # Tamaño de botones
        self.boton_tamaño = 200
        self.espacio = 50
        self.inicio_x = (self.size[0] - (2 * self.boton_tamaño + self.espacio)) // 2
        self.inicio_y = (self.size[1] - (2 * self.boton_tamaño + self.espacio)) // 2

        # Recursos
        self.cargar_imagenes()
        self.crear_botones()
        
    def cargar_imagenes(self):
        # Cargar imágenes de colores
        self.imagenes = {
            "ROJO": pygame.image.load("assets/RED.png").convert(),
            "VERDE": pygame.image.load("assets/GREEN.png").convert(),
            "AZUL": pygame.image.load("assets/BLUE.png").convert(),
            "AMARILLO": pygame.image.load("assets/YELLOW.png").convert(),
        }
        self.imagenes_highlight = {
            "ROJO": pygame.image.load("assets/RED_SEC.png").convert(),
            "VERDE": pygame.image.load("assets/GREEN_SEC.png").convert(),
            "AZUL": pygame.image.load("assets/BLUE_SEC.png").convert(),
            "AMARILLO": pygame.image.load("assets/YELLOW_SEC.png").convert(),
        }
        # Cargar imágenes de vidas
        corazon = pygame.image.load("assets/Heart.png").convert_alpha()
        corazon_vacio = pygame.image.load("assets/Heart-1.png").convert_alpha()
        self.corazon = pygame.transform.scale(corazon, (50, 50))
        self.corazon_vacio = pygame.transform.scale(corazon_vacio, (50, 50))

    def crear_botones(self):
        # Definir rectángulos para los botones
        self.botones = {
            "ROJO": pygame.Rect(self.inicio_x, self.inicio_y, self.boton_tamaño, self.boton_tamaño),
            "VERDE": pygame.Rect(self.inicio_x + self.boton_tamaño + self.espacio, self.inicio_y, self.boton_tamaño, self.boton_tamaño),
            "AZUL": pygame.Rect(self.inicio_x, self.inicio_y + self.boton_tamaño + self.espacio, self.boton_tamaño, self.boton_tamaño),
            "AMARILLO": pygame.Rect(self.inicio_x + self.boton_tamaño + self.espacio, self.inicio_y + self.boton_tamaño + self.espacio, self.boton_tamaño, self.boton_tamaño),
        }

    def dibujar_vidas(self):
        # Dibujar las vidas restantes en la esquina superior
        for i in range(self.max_vidas):
            x = 50 + i * (self.corazon.get_width() + 10)
            y = 20
            if i < self.vidas:
                self.screen.blit(self.corazon, (x, y))
            else:
                self.screen.blit(self.corazon_vacio, (x, y))
    
    def dibujar_botones(self, highlight=None):
        # Dibujar botones de colores
        for color, rect in self.botones.items():
            if highlight == color:
                self.screen.blit(self.imagenes_highlight[color], rect)
            else:
                self.screen.blit(self.imagenes[color], rect)
    
    def dibujar_pantalla(self, highlight=None):
        # Redibujar la pantalla completa
        self.screen.fill((0, 0, 0))  # Fondo negro
        self.dibujar_vidas()
        self.dibujar_botones(highlight)
        self.mostrar_texto(f"SCORE: {self.score}", (640, 40), tamaño=50)
        pygame.display.flip()

    def mostrar_texto(self, texto, pos, tamaño=50, color=(255, 255, 255)):
        # Mostrar texto en pantalla
        font = pygame.font.Font(None, tamaño)
        texto_render = font.render(texto, True, color)
        rect = texto_render.get_rect(center=pos)
        self.screen.blit(texto_render, rect)
    
    def generar_secuencia(self):
        self.mostrar_texto("GENERANDO SECUENCIA...", (640, 400), tamaño=80)
        pygame.display.flip()
        pygame.time.delay(2000)
        for color in self.secuencia:
            self.dibujar_pantalla(color)
            pygame.time.delay(700)
            self.dibujar_pantalla()
            pygame.time.delay(300)
    
    def comprobar_secuencia(self):
        # Comparar secuencia del jugador con la generada
        for i in range(len(self.player_secuencia)):
            if self.player_secuencia[i] != self.secuencia[i]:
                return False
        return True

    def añadir_color_random(self):
        # Añadir un color aleatorio a la secuencia
        color = random.choice(list(self.botones.keys()))
        self.secuencia.append(color)
    
    def manejar_eventos(self):
        # Manejar eventos de entrada
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for color, rect in self.botones.items():
                    if rect.collidepoint(mouse_pos):
                        self.player_secuencia.append(color)
                        self.dibujar_pantalla(color)
                        pygame.time.delay(300)
                        self.dibujar_pantalla()
                        if not self.comprobar_secuencia():
                            self.vidas -= 1
                            if self.vidas <= 0:
                                self.mostrar_texto("GAME OVER", (640, 400), tamaño=80, color=(255, 0, 0))
                                pygame.display.flip()
                                pygame.time.delay(3000)
                                return False
                            else:
                                self.mostrar_texto("SECUENCIA INCORRECTA", (640, 400), tamaño=80, color=(255, 100, 100))
                                pygame.display.flip()
                                pygame.time.delay(2000)
                                self.player_secuencia = []
                                self.generar_secuencia()
                        elif len(self.player_secuencia) == len(self.secuencia):
                            self.score += 1
                            self.mostrar_texto("¡CORRECTO!", (640, 400), tamaño=80, color=(100, 255, 100))
                            pygame.display.flip()
                            pygame.time.delay(2000)
                            self.player_secuencia = []
                            self.añadir_color_random()
                            self.generar_secuencia()
        return True

    def iniciar_juego(self):
        # Lógica principal del juego
        self.añadir_color_random()
        while True:
            if not self.manejar_eventos():
                break
            if self.inicio_juego:
                tiempo_actual = pygame.time.get_ticks()
                if tiempo_actual - self.inicio_tiempo > 2000:
                    self.inicio_juego = False
                    self.generar_secuencia()
            self.dibujar_pantalla()
            self.clock.tick(60)

if __name__ == "__main__":
    juego = SimonDiceGame()
    juego.iniciar_juego()




                            
    

