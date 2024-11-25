import pygame, sys, random, json, time
#Importar la clase Button del codigo button
from utils.button import Button
#Importar la clase Spray del codigo spray
from utils.spray import Spray
from utils.loadingbar import LoadingBar

#Iniciar pygame
pygame.init()

#Iniciar mezclador de sonido
pygame.mixer.init()

#Configurar la pantalla
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menú")

#Main Menu
FondoAzul = pygame.image.load("assets/FondoAzul.png")
FondoMain = pygame.image.load("assets/FondoMainMenu.png")
BGPuzzleNumerico = pygame.image.load("assets/BGPuzzleNumerico.png")
BGMapache = pygame.image.load("assets/BGMapache.png")

#Logo
Biomind = pygame.image.load("assets/BIOMIND.png")
Brain = pygame.image.load("assets/Brain.png")

#Simon Dice
SimondiceSpray = pygame.image.load("assets/SimonDiceSpray.png")
SimondiceSprayS = pygame.image.load("assets/SimonDiceSprayS.png")
BGSimonDice = pygame.image.load("assets/BGSimonDicePlay.png").convert()
SimonDiceButtonRed = pygame.image.load("assets/SimonDiceButtonRed.png")
SimonDiceButtonGreen = pygame.image.load("assets/SimonDiceButtonGreen.png")
SimonDiceButtonBlue = pygame.image.load("assets/SimonDiceButtonBlue.png")
SimonDiceButtonYellow = pygame.image.load("assets/SimonDiceButtonYellow.png")
BGSimonDiceMenu = pygame.image.load("assets/BGSimonDiceMainMenu.png")
BGSimonDiceLoading = pygame.image.load("assets/BGSimonDiceLoading.png")
ExitButtonSimonDice = pygame.image.load("assets/ExitButtonSimonDice.png")
jugando = False

#Puzzle Numerico
PuzzlenumericoSpray = pygame.image.load("assets/PuzzleNumericoSpray.png")
PuzzlenumericoSprayS = pygame.image.load("assets/PuzzleNumericoSprayS.png")

#Colores Y Figuras
ColoresyfigurasSpray = pygame.image.load("assets/ColoresYFigurasSpray.png")
ColoresyfigurasSprayS = pygame.image.load("assets/ColoresYFigurasSprayS.png")

#Reaction Game
JuegodereaccionSpray = pygame.image.load("assets/JuegoDeReaccionSpray.png")
JuegodereaccionSprayS = pygame.image.load("assets/JuegoDeReaccionSprayS.png")
BGMenuReactionGame = pygame.image.load("assets/BGMenuReactionGame.png")
BGReactionGame = pygame.image.load("assets/BGReactionGame.png")
BGTopScoresReactionGame = pygame.image.load("assets/BGTopScoresReactionGame.png")
BGLoadingReactionGame = pygame.image.load("assets/BGLoadingReactionGame.png")
Burbuja = pygame.image.load("assets/Burbuja.png")
POP = pygame.image.load("assets/POP.png")
Sonido_POP = pygame.mixer.Sound("assets/POP.mp3")
Sonido_Burbujas = pygame.mixer.Sound("assets/BurbujasLoading.mp3")

#Define la función para dar tipografia a los textos
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

#Define la función para poner contorno a los textos
def contorno(text, font, text_color, outline_color, x, y):
    # Renderiza el texto en el color del borde
    text_surface = font.render(text, True, outline_color)
    text_rect = text_surface.get_rect(center=(x, y))

    # Dibuja el contorno en todas las direcciones alrededor del texto
    screen.blit(text_surface, text_rect.move(-8, 0))  # Izquierda
    screen.blit(text_surface, text_rect.move(8, 0))   # Derecha
    screen.blit(text_surface, text_rect.move(0, -8))  # Arriba
    screen.blit(text_surface, text_rect.move(0, 8))   # Abajo

    # Dibuja las esquinas del contorno
    screen.blit(text_surface, text_rect.move(-8, -8))  # Arriba izquierda
    screen.blit(text_surface, text_rect.move(8, -8))   # Arriba derecha
    screen.blit(text_surface, text_rect.move(-8, 8))   # Abajo izquierda
    screen.blit(text_surface, text_rect.move(8, 8))    # Abajo derecha

    # Renderiza el texto principal en el color deseado
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, text_rect)

def contorno1(text, font, text_color, outline_color, x, y):
    # Renderiza el texto en el color del borde
    text_surface = font.render(text, True, outline_color)
    text_rect = text_surface.get_rect(center=(x, y))

    # Dibuja el contorno en todas las direcciones alrededor del texto
    screen.blit(text_surface, text_rect.move(-3, 0))  # Izquierda
    screen.blit(text_surface, text_rect.move(3, 0))   # Derecha
    screen.blit(text_surface, text_rect.move(0, -3))  # Arriba
    screen.blit(text_surface, text_rect.move(0, 3))   # Abajo

    # Dibuja las esquinas del contorno
    screen.blit(text_surface, text_rect.move(-3, -3))  # Arriba izquierda
    screen.blit(text_surface, text_rect.move(3, -3))   # Arriba derecha
    screen.blit(text_surface, text_rect.move(-3, 3))   # Abajo izquierda
    screen.blit(text_surface, text_rect.move(3, 3))    # Abajo derecha

    # Renderiza el texto principal en el color deseado
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, text_rect)

def games():
    pygame.display.set_caption("Games")
    loading_bar = LoadingBar(screen, FondoMain, start_color=(255, 212, 163), end_color=(208, 129, 89), text_color="#d08159", loading_time=1.5, segments=10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                pygame.quit()
                sys.exit()

        # Dibujar la barra de carga
        if loading_bar.draw():  # Si la barra de carga está llena
            break  # Detener el bucle principal cuando la barra esté llena

        # Esperar un poco para que el evento de carga se vea
        pygame.time.wait(100)

    while True:
        screen.blit(FondoMain, [0, 0])
        screen.blit(Biomind, (1200, 640))

        Games_mouse_pos = pygame.mouse.get_pos()

        contorno("GAMES", get_font(60), "#d08159", "black", 640, 360)

        Simon_Dice_B = Spray(base_image=SimondiceSpray, hover_image=SimondiceSprayS, pos=(320, 180))
        Simon_Dice_B.changeImage(Games_mouse_pos)
        Simon_Dice_B.update(screen)  # Dibujar el botón

        Puzzle_Numerico_B = Spray(base_image=PuzzlenumericoSpray, hover_image=PuzzlenumericoSprayS, pos=(960, 180))
        Puzzle_Numerico_B.changeImage(Games_mouse_pos)
        Puzzle_Numerico_B.update(screen)

        Juego_De_Reaccion_B = Spray(base_image=JuegodereaccionSpray, hover_image=JuegodereaccionSprayS, pos=(320, 540))
        Juego_De_Reaccion_B.changeImage(Games_mouse_pos)
        Juego_De_Reaccion_B.update(screen)

        Colores_Y_Figuras_B = Spray(base_image=ColoresyfigurasSpray, hover_image=ColoresyfigurasSprayS, pos=(960, 540))
        Colores_Y_Figuras_B.changeImage(Games_mouse_pos)
        Colores_Y_Figuras_B.update(screen)

        Games_back = Button(image=None, pos=(640, 420), 
                            text_input="BACK", font=get_font(50), base_color="black", hovering_color="#ffecd6")

        Games_back.changeColor(Games_mouse_pos)
        Games_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Games_back.checkForInput(Games_mouse_pos):
                    main_menu()
                if Juego_De_Reaccion_B.checkForInput(Games_mouse_pos):
                    menu_reaction_game()
                if Simon_Dice_B.checkForInput(Games_mouse_pos):
                    menu_simon_dice()
                if Puzzle_Numerico_B.checkForInput(Games_mouse_pos):
                    menu_puzzle_numerico()
                if Colores_Y_Figuras_B.checkForInput(Games_mouse_pos):
                    menu_colores_y_figuras()

        pygame.display.update()

def about():
    pygame.display.set_caption("About")
    loading_bar = LoadingBar(screen, FondoMain, start_color=(255, 212, 163), end_color=(208, 129, 89), text_color="#d08159", loading_time=1.5, segments=10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                pygame.quit()
                sys.exit()

        # Dibujar la barra de carga
        if loading_bar.draw():  # Si la barra de carga está llena
            break  # Detener el bucle principal cuando la barra esté llena

        # Esperar un poco para que el evento de carga se vea
        pygame.time.wait(100)

    while True:
        Play_mouse_pos = pygame.mouse.get_pos()

        screen.blit(FondoMain, [0, 0])
        screen.blit(Biomind, (1200, 640))

        contorno1("GAME BY BIOMIND STUDIO", get_font(60), "#d08159", "black", 640, 100)

        contorno1("MindBoost es un videojuego serio diseñado para la estimulación cognitiva.", get_font(30), "#ffecd6", "black", 640, 180)
        contorno1("El objetivo es fortalecer habilidades mentales, como la memoria,", get_font(30), "#ffecd6", "black", 640, 230)
        contorno1("la concentración y agilidad mental, a través de juegos interactivos.", get_font(30), "#ffecd6", "black", 640, 280)

        contorno1("MEMBERS", get_font(40), "#d08159", "black", 640, 360)

        contorno1("JORGE ELIUD JIMENEZ NAJAR", get_font(20), "#ffecd6", "black", 640, 420)
        contorno1("IRAIS GUADALUPE SOLANO ROSAS", get_font(20), "#ffecd6", "black", 640, 450)
        contorno1("AMMI PAHOLA RODRIGUEZ SALGADO", get_font(20), "#ffecd6", "black", 640, 480)
        contorno1("PABLO AZGAD CAMARENA MENDOZA", get_font(20), "#ffecd6", "black", 640, 510)
        contorno1("LUIS ALBERTO MARTEL ORDOÑEZ", get_font(20), "#ffecd6", "black", 640, 540)

        About_back = Button(image=pygame.image.load("assets/MainButton.png"), pos=(640, 640), 
                            text_input="BACK", font=get_font(75), base_color="#000000", hovering_color="White")

        About_back.changeColor(Play_mouse_pos)
        About_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if About_back.checkForInput(Play_mouse_pos):
                    main_menu()

        pygame.display.update()

def menu_reaction_game():
    pygame.display.set_caption("Menú Reaction Game")
    loading_bar = LoadingBar(screen, BGLoadingReactionGame, start_color=(255, 255, 255), end_color=(250, 140, 180), text_color="#2e67a5", loading_time=1.5, segments=10)

    while True:
        Sonido_Burbujas.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                pygame.quit()
                sys.exit()

        # Dibujar la barra de carga
        if loading_bar.draw():  # Si la barra de carga está llena
            break  # Detener el bucle principal cuando la barra esté llena

        # Esperar un poco para que el evento de carga se vea
        pygame.time.wait(100)

    Scores_file = "Top_scores_reaction_game.json"

    def reaction_games():
        pygame.display.set_caption("Reaction Game")
        loading_bar = LoadingBar(screen, BGLoadingReactionGame, start_color=(255, 255, 255), end_color=(250, 140, 180), text_color="#2e67a5", loading_time=1.5, segments=10)

        while True:
            Sonido_Burbujas.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                    pygame.quit()
                    sys.exit()

            # Dibujar la barra de carga
            if loading_bar.draw():  # Si la barra de carga está llena
                break  # Detener el bucle principal cuando la barra esté llena

            # Esperar un poco para que el evento de carga se vea
            pygame.time.wait(100)

        ancho, alto = 1280, 720

        # Imagen
        imagen_actual = Burbuja
        Burbuja_rect = Burbuja.get_rect()
        radio_inicial_burbuja = Burbuja.get_width() // 2  # Radio inicial basado en el ancho de la imagen
        radio_minimo = 15  # Radio mínimo antes de desaparecer

        # Configuración de tiempo de vida
        tiempo_inicial = 8000  # Tiempo de vida inicial de la figura en ms
        tiempo_vida = tiempo_inicial  # Tiempo de vida actual
        puntaje = 0
        radio_actual_burbuja = radio_inicial_burbuja

        # Variables de estado
        tiempo_inicio = pygame.time.get_ticks()
        mostrar_reemplazo = False
        tiempo_reemplazo = 250  # Tiempo en ms para mostrar la imagen de reemplazo
        tiempo_cambio = None  # Guardar el tiempo en que se cambió la imagen

        # Reloj de Pygame para controlar FPS
        clock = pygame.time.Clock()

        #Area en la que apareceran los circulos
        ancho_area_central = int(ancho * 0.92)  # 60% del ancho total de la pantalla
        alto_area_central = int(alto * 0.76)    # 60% del alto total de la pantalla
        inicio_x = (ancho - ancho_area_central) // 2
        inicio_y = (alto - alto_area_central) // 2

        # Estado inicial
        pos_circulo = (random.randint(int(inicio_x + radio_inicial_burbuja), int(inicio_x + ancho_area_central - radio_inicial_burbuja)), 
                    random.randint(int(inicio_y + radio_inicial_burbuja), int(inicio_y + alto_area_central - radio_inicial_burbuja)))
        tiempo_inicio = pygame.time.get_ticks()

        def save_score(new_score, player_name):
            try:
                with open(Scores_file, "r") as file:
                    scores = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                scores = [{"name": "---", "score": 0} for _ in range(5)]
            
            # Añadir el nuevo puntaje
            scores.append({"name": player_name, "score": new_score})
            # Ordenar por puntaje descendente y mantener solo los 5 mejores
            scores = sorted(scores, key=lambda x: x["score"], reverse=True)[:5]

            # Guardar los puntajes actualizados
            with open(Scores_file, "w") as file:
                json.dump(scores, file)

        while True:
            screen.blit(BGReactionGame, (0, 0))

            reaction_games_mouse_pos = pygame.mouse.get_pos()

            #Dibujar el área central para visualización
            #pygame.draw.rect(screen, (100, 100, 100), (inicio_x, inicio_y, ancho_area_central, alto_area_central), 2)
            # Manejar eventos

            ReactionGame_exit = Button(image=None, pos=(640, 670), 
                                text_input="EXIT", font=get_font(50), base_color="White", hovering_color="#b8b5b9")

            ReactionGame_exit.changeColor(reaction_games_mouse_pos)
            ReactionGame_exit.update(screen)

            # Tiempo transcurrido
            tiempo_actual = pygame.time.get_ticks() - tiempo_inicio
    
            # Game Over
            if tiempo_actual >= tiempo_vida:
                contorno("GAME OVER", get_font(100), "black", "red", 640, 300)
                Press_r = get_font(40).render("PRESS R TO RESTART", True, "black")
                Press_r_rect = Press_r.get_rect(center=(640,360))
                screen.blit(Press_r, Press_r_rect)
                texto_puntaje_ReactionGame = get_font(40).render(f"SCORE: {puntaje}", True, "black")
                texto_puntaje_ReactionGame_rect = texto_puntaje_ReactionGame.get_rect(center=(640,50))
                screen.blit(texto_puntaje_ReactionGame, texto_puntaje_ReactionGame_rect)

            # Si estamos mostrando la imagen de reemplazo, verificar el tiempo transcurrido
            if mostrar_reemplazo and tiempo_cambio:
                # Mostrar la imagen de reemplazo durante un tiempo limitado
                if pygame.time.get_ticks() - tiempo_cambio < tiempo_reemplazo:
                    # Redimensionar la segunda imagen
                    factor_tiempo = (pygame.time.get_ticks() - tiempo_inicio) / tiempo_vida
                    radio_actual = max(radio_minimo, int(radio_inicial_burbuja * (1 - factor_tiempo)))
                    imagen_escalada = pygame.transform.scale(POP, (2 * radio_actual, 2 * radio_actual))
                    screen.blit(imagen_escalada, imagen_escalada.get_rect(center=pos_circulo))
                else:
                    # Volver a la imagen original y reiniciar la posición y tamaño
                    mostrar_reemplazo = False
                    pos_circulo = (random.randint(int(inicio_x + radio_inicial_burbuja), int(inicio_x + ancho_area_central - radio_inicial_burbuja)),
                            random.randint(int(inicio_y + radio_inicial_burbuja), int(inicio_y + alto_area_central - radio_inicial_burbuja)))
                    radio_actual = radio_inicial_burbuja
                    tiempo_inicio = pygame.time.get_ticks()
            if not mostrar_reemplazo and tiempo_actual < tiempo_vida:
                # Redimensionar y mostrar la imagen original si la imagen de reemplazo no está activa y no es game over
                factor_tiempo = tiempo_actual / tiempo_vida
                radio_actual = max(radio_minimo, int(radio_inicial_burbuja * (1 - factor_tiempo)))
                imagen_escalada = pygame.transform.scale(Burbuja, (2 * radio_actual, 2 * radio_actual))
                screen.blit(imagen_escalada, imagen_escalada.get_rect(center=pos_circulo))

                # Mostrar puntaje
                texto_puntaje_ReactionGame = get_font(40).render(f"SCORE: {puntaje}", True, "black")
                texto_puntaje_ReactionGame_rect = texto_puntaje_ReactionGame.get_rect(center=(640,50))
                screen.blit(texto_puntaje_ReactionGame, texto_puntaje_ReactionGame_rect)

            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    dist = ((x - pos_circulo[0]) ** 2 + (y - pos_circulo[1]) ** 2) ** 0.5
                    if dist <= radio_actual_burbuja:
                        # Acierto, aumentar puntaje y reducir tiempo de vida
                        puntaje += 1
                        tiempo_vida = max(500, tiempo_vida - 50)
                
                        # Cambiar temporalmente a la imagen de reemplazo
                        mostrar_reemplazo = True
                        Sonido_POP.play()
                        tiempo_cambio = pygame.time.get_ticks()
                    if ReactionGame_exit.checkForInput(reaction_games_mouse_pos):
                        save_score(puntaje, player_name)
                        menu_reaction_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        save_score(puntaje, player_name)
                        reaction_games()

            pygame.display.flip()
            clock.tick(60)  # Mantener 60 FPS

    def tutorial_reaction_game():
        pygame.display.set_caption("Tutorial Reaction Game")
        loading_bar = LoadingBar(screen, BGLoadingReactionGame, start_color=(255, 255, 255), end_color=(250, 140, 180), text_color="#2e67a5", loading_time=1.5, segments=10)

        while True:
            Sonido_Burbujas.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                    pygame.quit()
                    sys.exit()

            # Dibujar la barra de carga
            if loading_bar.draw():  # Si la barra de carga está llena
                break  # Detener el bucle principal cuando la barra esté llena

            # Esperar un poco para que el evento de carga se vea
            pygame.time.wait(100)
        
        def tutorialreactiongame():
            pygame.display.set_caption("Reaction Game")
            loading_bar = LoadingBar(screen, BGLoadingReactionGame, start_color=(255, 255, 255), end_color=(250, 140, 180), text_color="#2e67a5", loading_time=1.5, segments=10)

            while True:
                Sonido_Burbujas.play()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                        pygame.quit()
                        sys.exit()

                # Dibujar la barra de carga
                if loading_bar.draw():  # Si la barra de carga está llena
                    break  # Detener el bucle principal cuando la barra esté llena

                # Esperar un poco para que el evento de carga se vea
                pygame.time.wait(100)

            ancho, alto = 1280, 720

            # Imagen
            imagen_actual = Burbuja
            Burbuja_rect = Burbuja.get_rect()
            radio_inicial_burbuja = Burbuja.get_width() // 2  # Radio inicial basado en el ancho de la imagen
            radio_minimo = 15  # Radio mínimo antes de desaparecer

            # Configuración de tiempo de vida
            tiempo_inicial = 8000  # Tiempo de vida inicial de la figura en ms
            tiempo_vida = tiempo_inicial  # Tiempo de vida actual
            puntaje = 0
            radio_actual_burbuja = radio_inicial_burbuja

            # Variables de estado
            tiempo_inicio = pygame.time.get_ticks()
            mostrar_reemplazo = False
            tiempo_reemplazo = 250  # Tiempo en ms para mostrar la imagen de reemplazo
            tiempo_cambio = None  # Guardar el tiempo en que se cambió la imagen

            # Reloj de Pygame para controlar FPS
            clock = pygame.time.Clock()

            #Area en la que apareceran los circulos
            ancho_area_central = int(ancho * 0.92)  # 60% del ancho total de la pantalla
            alto_area_central = int(alto * 0.76)    # 60% del alto total de la pantalla
            inicio_x = (ancho - ancho_area_central) // 2
            inicio_y = (alto - alto_area_central) // 2

            # Estado inicial
            pos_circulo = (random.randint(int(inicio_x + radio_inicial_burbuja), int(inicio_x + ancho_area_central - radio_inicial_burbuja)), 
                        random.randint(int(inicio_y + radio_inicial_burbuja), int(inicio_y + alto_area_central - radio_inicial_burbuja)))
            tiempo_inicio = pygame.time.get_ticks()

            while True:
                screen.blit(BGReactionGame, (0, 0))

                reaction_games_mouse_pos = pygame.mouse.get_pos()

                #Dibujar el área central para visualización
                #pygame.draw.rect(screen, (100, 100, 100), (inicio_x, inicio_y, ancho_area_central, alto_area_central), 2)
                # Manejar eventos

                ReactionGame_exit = Button(image=None, pos=(640, 670), 
                                    text_input="EXIT", font=get_font(50), base_color="White", hovering_color="#b8b5b9")

                ReactionGame_exit.changeColor(reaction_games_mouse_pos)
                ReactionGame_exit.update(screen)

                # Tiempo transcurrido
                tiempo_actual = pygame.time.get_ticks() - tiempo_inicio
    
                # Game Over
                if tiempo_vida == 7800:
                    tutorial_reaction_game()

                # Si estamos mostrando la imagen de reemplazo, verificar el tiempo transcurrido
                if mostrar_reemplazo and tiempo_cambio:
                    # Mostrar la imagen de reemplazo durante un tiempo limitado
                    if pygame.time.get_ticks() - tiempo_cambio < tiempo_reemplazo:
                        # Redimensionar la segunda imagen
                        factor_tiempo = (pygame.time.get_ticks() - tiempo_inicio) / tiempo_vida
                        radio_actual = max(radio_minimo, int(radio_inicial_burbuja * (1 - factor_tiempo)))
                        imagen_escalada = pygame.transform.scale(POP, (2 * radio_actual, 2 * radio_actual))
                        screen.blit(imagen_escalada, imagen_escalada.get_rect(center=pos_circulo))
                    else:
                        # Volver a la imagen original y reiniciar la posición y tamaño
                        mostrar_reemplazo = False
                        pos_circulo = (random.randint(int(inicio_x + radio_inicial_burbuja), int(inicio_x + ancho_area_central - radio_inicial_burbuja)),
                                random.randint(int(inicio_y + radio_inicial_burbuja), int(inicio_y + alto_area_central - radio_inicial_burbuja)))
                        radio_actual = radio_inicial_burbuja
                        tiempo_inicio = pygame.time.get_ticks()
                if not mostrar_reemplazo and tiempo_actual < tiempo_vida:
                    # Redimensionar y mostrar la imagen original si la imagen de reemplazo no está activa y no es game over
                    factor_tiempo = tiempo_actual / tiempo_vida
                    radio_actual = max(radio_minimo, int(radio_inicial_burbuja * (1 - factor_tiempo)))
                    imagen_escalada = pygame.transform.scale(Burbuja, (2 * radio_actual, 2 * radio_actual))
                    screen.blit(imagen_escalada, imagen_escalada.get_rect(center=pos_circulo))

                    # Mostrar puntaje
                    texto_puntaje_ReactionGame = get_font(40).render(f"SCORE: {puntaje}", True, "black")
                    texto_puntaje_ReactionGame_rect = texto_puntaje_ReactionGame.get_rect(center=(640,50))
                    screen.blit(texto_puntaje_ReactionGame, texto_puntaje_ReactionGame_rect)

                for event in pygame.event.get():
            
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = pygame.mouse.get_pos()
                        dist = ((x - pos_circulo[0]) ** 2 + (y - pos_circulo[1]) ** 2) ** 0.5
                        if dist <= radio_actual_burbuja:
                            # Acierto, aumentar puntaje y reducir tiempo de vida
                            puntaje += 1
                            tiempo_vida = max(500, tiempo_vida - 20)
                
                            # Cambiar temporalmente a la imagen de reemplazo
                            mostrar_reemplazo = True
                            Sonido_POP.play()
                            tiempo_cambio = pygame.time.get_ticks()
                        if ReactionGame_exit.checkForInput(reaction_games_mouse_pos):
                            tutorial_reaction_game()

                pygame.display.flip()
                clock.tick(60)  # Mantener 60 FPS

        while True:
            Tutorial_reaction_game_mouse_pos = pygame.mouse.get_pos()
            screen.blit(BGTopScoresReactionGame, (0,0))
            contorno("TUTORIAL", get_font(100), "#2e67a5", "black", 640, 100)

            contorno1("Bienvenido a Reaction Game", get_font(40), "#fa8cb4", "black", 640, 200)
            contorno1("¡Pon a prueba tu velocidad!", get_font(40), "#fa8cb4", "black", 640, 250)
            contorno1("En el juego, aparecerán burbujas en la pantalla", get_font(40), "#fa8cb4", "black", 640, 300)
            contorno1("deberás tocar antes de que desaparezcan. Si logras", get_font(40), "#fa8cb4", "black", 640, 350)
            contorno1("tocarlas, continuarás jugando; si no lo haces, el", get_font(40), "#fa8cb4", "black", 640, 400)
            contorno1("juego se acaba. Entre más burbujas toques, más", get_font(40), "#fa8cb4", "black", 640, 450)
            contorno1("rápido se volverá el juego.", get_font(40), "#fa8cb4", "black", 640, 500)

            Tutorial_reaction_game_b = Button(image=pygame.image.load("assets/ReactionGameButton.png"), pos=(320, 620), 
                            text_input="TUTORIAL", font=get_font(65), base_color="#000000", hovering_color="White")
            Back_tutorial_reaction_game_button = Button(image=pygame.image.load("assets/ReactionGameButton.png"), pos=(960, 620), 
                            text_input="BACK", font=get_font(65), base_color="#000000", hovering_color="White")
            
            for button in [Tutorial_reaction_game_b, Back_tutorial_reaction_game_button]:
                button.changeColor(Tutorial_reaction_game_mouse_pos)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Tutorial_reaction_game_b.checkForInput(Tutorial_reaction_game_mouse_pos):
                        tutorialreactiongame()
                    if Back_tutorial_reaction_game_button.checkForInput(Tutorial_reaction_game_mouse_pos):
                        menu_reaction_game()
            pygame.display.update()
    
    def score_reaction_game():
        pygame.display.set_caption("Score Reaction Game")
        loading_bar = LoadingBar(screen, BGLoadingReactionGame, start_color=(255, 255, 255), end_color=(250, 140, 180), text_color="#2e67a5", loading_time=1.5, segments=10)

        while True:
            Sonido_Burbujas.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                    pygame.quit()
                    sys.exit()

            # Dibujar la barra de carga
            if loading_bar.draw():  # Si la barra de carga está llena
                break  # Detener el bucle principal cuando la barra esté llena

            # Esperar un poco para que el evento de carga se vea
            pygame.time.wait(100)

        # Función para cargar los puntajes
        def load_scores():
            try:
                with open("Top_scores_reaction_game.json", "r") as file:
                    return json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                # Si no hay archivo o está corrupto, usar una lista predeterminada
                return [{"name": "---", "score": 0} for _ in range(5)]

        # Cargar los puntajes
        top_scores = load_scores()

        while True:
            Score_reaction_game_mouse_pos = pygame.mouse.get_pos()
            screen.blit(BGTopScoresReactionGame, (0, 0))

            # Título de la pantalla de puntajes
            contorno("TOP SCORES", get_font(100), "#2e67a5", "black", 640, 100)
            contorno("RANK", get_font(80), "#fa8cb4", "black", 380, 220)
            contorno("NAME", get_font(80), "#fa8cb4", "black", 640, 220)
            contorno("SCORE", get_font(80), "#fa8cb4", "black", 900, 220)

            # Dibujar la lista de puntajes
            for i, entry in enumerate(top_scores):
                rank_text = f"{i + 1}st" if i == 0 else f"{i + 1}nd" if i == 1 else f"{i + 1}rd" if i == 2 else f"{i + 1}th"
                rank_text = get_font(50).render(rank_text, True, "black")
                rank_text_rect = rank_text.get_rect(center=(380, 300 + i * 60))
                screen.blit(rank_text, rank_text_rect)
                name_text = get_font(50).render(entry["name"], True, "black")
                name_text_rect = name_text.get_rect(center=(640, 300 + i * 60))
                screen.blit(name_text, name_text_rect)
                score_text = get_font(50).render(str(entry["score"]), True, "black")
                score_text_rect = score_text.get_rect(center=(900, 300 + i * 60))
                screen.blit(score_text, score_text_rect)

            # Botón para volver
            Back_to_menu_button = Button(image=pygame.image.load("assets/ReactionGameButton.png"), pos=(640, 630), 
                                         text_input="BACK", font=get_font(65), base_color="black", hovering_color="White")

            Back_to_menu_button.changeColor(Score_reaction_game_mouse_pos)
            Back_to_menu_button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Back_to_menu_button.checkForInput(Score_reaction_game_mouse_pos):
                        menu_reaction_game()

            pygame.display.update()

    while True:
        Menu_reaction_game_mouse_pos = pygame.mouse.get_pos()
        screen.blit(BGMenuReactionGame, (0,0))

        contorno("REACTION", get_font(100), "#2e67a5", "black", 640, 150)
        contorno("GAME", get_font(100), "#2e67a5", "black", 640, 250)

        Play_reaction_game_button = Button(image=pygame.image.load("assets/ReactionGameButton.png"), pos=(240, 450), 
                            text_input="PLAY", font=get_font(65), base_color="#000000", hovering_color="White")
        Tutorial_reaction_game_button = Button(image=pygame.image.load("assets/ReactionGameButton.png"), pos=(1050, 450), 
                            text_input="TUTORIAL", font=get_font(65), base_color="#000000", hovering_color="White")
        Back_reaction_game_button = Button(image=pygame.image.load("assets/ReactionGameButton.png"), pos=(240, 600), 
                            text_input="BACK", font=get_font(65), base_color="#000000", hovering_color="White")
        Score_reaction_game_button = Button(image=pygame.image.load("assets/ReactionGameButton.png"), pos=(1050, 600), 
                            text_input="SCORE", font=get_font(65), base_color="#000000", hovering_color="White")
        
        for button in [Play_reaction_game_button, Tutorial_reaction_game_button, Back_reaction_game_button, Score_reaction_game_button]:
            button.changeColor(Menu_reaction_game_mouse_pos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Play_reaction_game_button.checkForInput(Menu_reaction_game_mouse_pos):
                    reaction_games()
                if Back_reaction_game_button.checkForInput(Menu_reaction_game_mouse_pos):
                    games()
                if Tutorial_reaction_game_button.checkForInput(Menu_reaction_game_mouse_pos):
                    tutorial_reaction_game()
                if Score_reaction_game_button.checkForInput(Menu_reaction_game_mouse_pos):
                    score_reaction_game()

        pygame.display.update()

def menu_simon_dice():
    pygame.display.set_caption("Simon Dice")
    loading_bar = LoadingBar(screen, BGSimonDiceLoading, start_color=(240, 246, 240), end_color=(0, 0, 0), text_color="#f0f6f0", loading_time=1.5, segments=10)

    def simon_dice():
        size = (1280, 800)
        pygame.display.set_caption("Simón Dice")
        clock = pygame.time.Clock()  # Para limitar los FPS
        score = 0

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

        # Cargar imágenes de corazones
        corazon = pygame.image.load("assets/Heart.png").convert_alpha()
        corazon_tamaño = (50, 50)  # Tamaño de los corazones
        corazon1 = pygame.transform.scale(corazon, corazon_tamaño)
        corazon_vacio = pygame.image.load("assets/Heart-1.png").convert_alpha()
        corazon_vacio1 = pygame.transform.scale(corazon_vacio, corazon_tamaño)

        # Configuración de vidas
        max_vidas = 3
        vidas = max_vidas

        SimonDice_exit = Button(ExitButtonSimonDice, pos=(1104, 644), 
                                text_input="EXIT", font=get_font(40), base_color="#f0f6f0", hovering_color="#b8b5b9")

        # Función para dibujar corazones
        def dibujar_vidas(vidas):
            for i in range(max_vidas):
                x = 50 + i * (corazon_tamaño[0] + 10)
                y = 120
                if i < vidas:
                    screen.blit(corazon1, (x, y))  # Corazón lleno
                else:
                    screen.blit(corazon_vacio1, (x, y))  # Corazón vacío
        
        def dibujar_vidas_grande(vidas):
            for i in range(max_vidas):
                x = 330 + i * (200 + 10)
                y = 300
                if i < vidas:
                    screen.blit(corazon, (x, y))  # Corazón lleno
                else:
                    screen.blit(corazon_vacio, (x, y))  # Corazón vacío

        def dibujar_botones(highlight=None):
            screen.blit(BGSimonDice, (0,0))

            # Mostrar puntaje
            contorno1(f"SCORE: {score}", get_font(50), "#f0f6f0", "black", 640, 40)

            if jugando == True:
                SimonDice_exit.update(screen)
                SimonDice_exit.changeColor(simon_dice_mouse_pos)

            dibujar_vidas(vidas)

            for color, rect in botones.items():
                if highlight == color:
                    screen.blit(imagenes_highlight[color], rect)
                else:
                    screen.blit(imagenes[color], rect)
            pygame.display.update([rect for rect in botones.values()])
            pygame.display.flip()

        def mostrar_mensaje(texto, color=(255, 255, 255), tamaño=50, x=size[0] // 2, y=size[1] // 2):
            contorno1(texto, get_font(tamaño), color, "black", x, size[1] // 2)
            pygame.display.flip()

        def play_secuencia(seq):
            global jugando
            jugando = False
            print(f"Estado de jugando: {jugando}")

            screen.blit(BGSimonDice, (0, 0))  # Redibuja el fondo
            contorno1(f"SCORE: {score}", get_font(50), "#f0f6f0", "black", 640, 40)
            mostrar_mensaje("GENERANDO SECUENCIA...", tamaño=80, color="#f0f6f0")
            pygame.time.delay(3000)  # Pausa para leer el mensaje

            for color in seq:
                dibujar_botones(color)
                pygame.time.delay(1000)
                dibujar_botones()
                pygame.time.delay(1000)

            # Mostrar mensaje "Tu turno"
            screen.blit(BGSimonDice, (0, 0))  # Redibuja el fondo
            contorno1(f"SCORE: {score}", get_font(50), "#f0f6f0", "black", 640, 40)
            mostrar_mensaje("¡TU TURNO!", tamaño=80, color="#f0f6f0")
            pygame.time.delay(3000)  # Pausa para leer el mensaje

            jugando = True
            print(f"Estado de jugando: {jugando}")


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
            simon_dice_mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if jugando == True and event.type == pygame.MOUSEBUTTONDOWN:
                    if SimonDice_exit.checkForInput(simon_dice_mouse_pos):
                        menu_simon_dice()
                    for color, rect in botones.items():
                        if rect.collidepoint(simon_dice_mouse_pos):
                            player_secuencia.append(color)
                            dibujar_botones(color)
                            pygame.time.delay(300)
                            dibujar_botones()

                            if not revisar_player_secuencia():
                                vidas -= 1
                                screen.blit(BGSimonDice, (0,0))
                                contorno1(f"SCORE: {score}", get_font(50), "#f0f6f0", "black", 640, 40)
                                mostrar_mensaje("¡SECUENCIA INCORRECTA!", tamaño=80, color="#b45252")
                                pygame.time.delay(3000)
                                screen.blit(BGSimonDice, (0,0))
                                contorno1(f"SCORE: {score}", get_font(50), "#f0f6f0", "black", 640, 40)
                                dibujar_vidas_grande(vidas)
                                pygame.display.flip()
                                pygame.time.delay(3000)
                                player_secuencia = []

                                if vidas <= 0:
                                    mostrar_mensaje("GAME OVER", tamaño=80, color="#FF0000")
                                    pygame.time.delay(3000)
                                    pygame.quit()
                                    return
                                
                                play_secuencia(secuencia)
                            if len(player_secuencia) == len(secuencia):
                                score += 1
                                screen.blit(BGSimonDice, (0,0))
                                contorno1(f"SCORE: {score}", get_font(50), "#f0f6f0", "black", 640, 40)
                                mostrar_mensaje("¡SECUENCIA CORRECTA!", tamaño=80, color="#8ab060")
                                pygame.time.delay(3000)
                                player_secuencia = []
                                añadir_color_random(secuencia)
                                play_secuencia(secuencia)

            if inicio_juego:
                tiempo_actual = pygame.time.get_ticks()
                if tiempo_actual - inicio_tiempo > 2000:
                    inicio_juego = False
                    play_secuencia(secuencia)

            dibujar_botones()
            clock.tick(30)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                pygame.quit()
                sys.exit()

        # Dibujar la barra de carga
        if loading_bar.draw():  # Si la barra de carga está llena
            break  # Detener el bucle principal cuando la barra esté llena

        # Esperar un poco para que el evento de carga se vea
        pygame.time.wait(100)

    while True:
        screen.blit(BGSimonDiceMenu, (0,0))
        simon_dice_mouse_pos = pygame.mouse.get_pos()

        contorno1("SIMON DICE", get_font(60), "#f0f6f0", "black", 640, 45)

        SimondiceSpray_rect = SimondiceSpray.get_rect(center=(635,400))
        screen.blit(SimondiceSpray, SimondiceSpray_rect)

        Play_simon_dice_button = Button(image=pygame.image.load("assets/SimonDiceButtonRed.png"), pos=(320, 200), 
                            text_input="PLAY", font=get_font(65), base_color="#000000", hovering_color="White")
        Tutorial_simon_dice_button = Button(image=pygame.image.load("assets/SimonDiceButtonGreen.png"), pos=(950, 200), 
                            text_input="TUTORIAL", font=get_font(65), base_color="#000000", hovering_color="White")
        Back_simon_dice_button = Button(image=pygame.image.load("assets/SimonDiceButtonBlue.png"), pos=(320, 600), 
                            text_input="BACK", font=get_font(65), base_color="#000000", hovering_color="White")
        Score_simon_dice_button = Button(image=pygame.image.load("assets/SimonDiceButtonYellow.png"), pos=(950, 600), 
                            text_input="SCORE", font=get_font(65), base_color="#000000", hovering_color="White")
        
        for button in [Play_simon_dice_button, Tutorial_simon_dice_button, Back_simon_dice_button, Score_simon_dice_button]:
            button.changeColor(simon_dice_mouse_pos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Play_simon_dice_button.checkForInput(simon_dice_mouse_pos):
                    simon_dice()
                if Back_simon_dice_button.checkForInput(simon_dice_mouse_pos):
                    games()
                if Tutorial_simon_dice_button.checkForInput(simon_dice_mouse_pos):
                    tutorial_reaction_game()
                if Score_simon_dice_button.checkForInput(simon_dice_mouse_pos):
                    score_reaction_game()

        pygame.display.update()

def menu_puzzle_numerico():
    pygame.display.set_caption("Puzzle Numerico")

    while True:
        screen.blit(BGPuzzleNumerico, (0, 0))

        simon_dice_mouse_pos = pygame.mouse.get_pos()

        Biomind_titeld = get_font(30).render("Aqui iria el juego...", True, "Red")
        Biomind_titeld_rect = Biomind_titeld.get_rect(center=(640,200))
        screen.blit(Biomind_titeld, Biomind_titeld_rect)
        About_P1 = get_font(30).render("Si tuviera uno", True, "black")
        About_P1_rect = About_P1.get_rect(center=(640,280))
        screen.blit(About_P1, About_P1_rect)

        simon_dice_exit = Button(image=None, pos=(640, 620), 
                            text_input="EXIT", font=get_font(60), base_color="Red", hovering_color="White")

        simon_dice_exit.changeColor(simon_dice_mouse_pos)
        simon_dice_exit.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if simon_dice_exit.checkForInput(simon_dice_mouse_pos):
                    games()

        pygame.display.update()

def menu_colores_y_figuras():
    pygame.display.set_caption("Colores Y Figuras")

    while True:
        screen.blit(BGMapache, [0, 0])

        simon_dice_mouse_pos = pygame.mouse.get_pos()

        Biomind_titeld = get_font(30).render("MAPACHE DUERMIENDO", True, "black")
        Biomind_titeld_rect = Biomind_titeld.get_rect(center=(450,340))
        screen.blit(Biomind_titeld, Biomind_titeld_rect)
        About_P1 = get_font(30).render("PORFAVOR SALGA", True, "black")
        About_P1_rect = About_P1.get_rect(center=(450,380))
        screen.blit(About_P1, About_P1_rect)

        simon_dice_exit = Button(image=None, pos=(430, 570), 
                            text_input="EXIT", font=get_font(60), base_color="#d08159", hovering_color="#ffecd6")

        simon_dice_exit.changeColor(simon_dice_mouse_pos)
        simon_dice_exit.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if simon_dice_exit.checkForInput(simon_dice_mouse_pos):
                    games()

        pygame.display.update()

def main_menu():
    pygame.display.set_caption("Menú")
    loading_bar = LoadingBar(screen, FondoMain, start_color=(255, 212, 163), end_color=(208, 129, 89), text_color="#d08159", loading_time=1.5, segments=10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                pygame.quit()
                sys.exit()

        # Dibujar la barra de carga
        if loading_bar.draw():  # Si la barra de carga está llena
            break  # Detener el bucle principal cuando la barra esté llena

        # Esperar un poco para que el evento de carga se vea
        pygame.time.wait(100)
    
    while True:
        screen.blit(FondoMain, [0, 0])
        screen.blit(Biomind, (1200, 640))
        Brain_rect = Brain.get_rect(center=(640,70))
        screen.blit(Brain, Brain_rect)
        
        Menu_mouse_pos = pygame.mouse.get_pos()
        
        contorno("MINDBOOST", get_font(100), "#d08159", "black", 640, 170)

        Games_button = Button(image=pygame.image.load("assets/MainButton.png"), pos=(640, 300), 
                            text_input="GAMES", font=get_font(75), base_color="#000000", hovering_color="White")
        About_button = Button(image=pygame.image.load("assets/MainButton.png"), pos=(640, 450), 
                            text_input="ABOUT", font=get_font(75), base_color="#000000", hovering_color="White")
        Quit_button = Button(image=pygame.image.load("assets/MainButton.png"), pos=(640, 600), 
                            text_input="QUIT", font=get_font(75), base_color="#000000", hovering_color="White")

        for button in [Games_button, Quit_button, About_button]:
            button.changeColor(Menu_mouse_pos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Games_button.checkForInput(Menu_mouse_pos):
                        games()
                if About_button.checkForInput(Menu_mouse_pos):
                    about()
                if Quit_button.checkForInput(Menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def get_player_name():
    pygame.display.set_caption("Menú")

    name = ""

    while True:
        screen.blit(FondoMain, (0,0))
        screen.blit(Biomind, (1200, 640))
        Brain_rect = Brain.get_rect(center=(640,70))
        screen.blit(Brain, Brain_rect)
        get_player_name_mouse_pos = pygame.mouse.get_pos()
        
        contorno("MINDBOOST", get_font(100), "#d08159", "black", 640, 170)
        Enter_your_name = get_font(60).render("ENTER YOUR NICKNAME:", True, "#ffecd6")
        Enter_your_name_rect = Enter_your_name.get_rect(center=(640, 300))
        screen.blit(Enter_your_name, Enter_your_name_rect)

        # Dibujar el rectángulo para la entrada de texto
        input_rect = pygame.Rect(440, 380, 400, 60)
        pygame.draw.rect(screen, "#d08159", input_rect, border_radius=10)  # Fondo del rectángulo
        pygame.draw.rect(screen, "#9c6244", input_rect, 10, border_radius=10)  # Contorno del rectángulo
        pygame.draw.rect(screen, "black", input_rect, 6, border_radius=10)  # Contorno del rectángulo

        Quit_button = Button(image=pygame.image.load("assets/MainButton.png"), pos=(640, 600), 
                            text_input="QUIT", font=get_font(75), base_color="#000000", hovering_color="White")
        
        for button in [Quit_button]:
            button.changeColor(get_player_name_mouse_pos)
            button.update(screen)

        # Mostrar el nombre ingresado hasta ahora
        name_text = get_font(50).render(name, True, "#ffecd6")
        name_text_rect = name_text.get_rect(center=(640, 415))
        screen.blit(name_text, name_text_rect)

        if len(name) == 3:
            Press_enter = get_font(30).render("PRESS THE ENTER KEY TO CONTINUE", True, "#ffecd6")
            Press_enter_rect = Press_enter.get_rect(center=(640, 480))
            screen.blit(Press_enter, Press_enter_rect)

        if len(name) > 0 and len(name) < 2:
            warning_text = get_font(30).render("ENTER 2 LETTERS TO CONTINUE", True, "#ffecd6")
            warning_rect = warning_text.get_rect(center=(640, 480))
            screen.blit(warning_text, warning_rect)

        if len(name) > 1 and len(name) < 3:
            warning_text = get_font(30).render("ENTER 1 LETTER TO CONTINUE", True, "#ffecd6")
            warning_rect = warning_text.get_rect(center=(640, 480))
            screen.blit(warning_text, warning_rect)

        if len(name) == 0:
            Press_enter = get_font(30).render("ENTER ONLY 3 LETTERS", True, "#ffecd6")
            Press_enter_rect = Press_enter.get_rect(center=(640, 480))
            screen.blit(Press_enter, Press_enter_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Quit_button.checkForInput(get_player_name_mouse_pos):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(name) == 3:
                    return name
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]  # Eliminar el último carácter
                if len(name) < 3 and event.unicode.isalnum():
                    name += event.unicode.upper()  # Agregar la letra en mayúsculas

player_name = get_player_name()
print(f"Player name: {player_name}")
main_menu()