import pygame, sys, random, json, time, os
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

player_name = ""

#Main Menu
FondoAzul = pygame.image.load("assets/FondoAzul.png")
FondoMain = pygame.image.load("assets/FondoMainMenu.png")
BGMapache = pygame.image.load("assets/BGMapache.png")
BotonVolumen = pygame.image.load("assets/BotonVolumen.png")
BotonVolumenS = pygame.image.load("assets/BotonVolumenSpray.png")
Musica_Menu = pygame.mixer.Sound("assets/Digital-Serenity-ext-v2.1.wav")
Musica_Menu.set_volume(0.2)

#Volumen
SubirVolumen = pygame.image.load("assets/SubirVolumen.png")
SubirVolumenS = pygame.image.load("assets/SubirVolumenS.png")
BajarVolumen = pygame.image.load("assets/BajarVolumen.png")
BajarVolumenS = pygame.image.load("assets/BajarVolumenS.png")
VolumenSimbol = pygame.image.load("assets/VolumenSimbol.png")
VolumenMute = pygame.image.load("assets/VolumenMute.png")

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
BGMenuPuzzleNumerico = pygame.image.load("assets/BGMenuPuzzleNumerico.png")
BGPuzzleNumerico = pygame.image.load("assets/BGPuzzleNumerico.png")
ButtonSTM = pygame.image.load("assets/ButtonSTM.png")
BGLoadingSTM = pygame.image.load("assets/BGLoadingSTM.png")
BGWinSTM = pygame.image.load("assets/BGWinPuzzleNumerico.png")
BGTutorialSTM = pygame.image.load("assets/BGTutorialSTM.png")
BackSTM = pygame.image.load("assets/Flecha_Back.png")
BGScoresSTM = pygame.image.load("assets/BGScoresSTM.png")

#Colores Y Figuras
ColoresyfigurasSpray = pygame.image.load("assets/ColoresYFigurasSpray.png")
ColoresyfigurasSprayS = pygame.image.load("assets/ColoresYFigurasSprayS.png")
BGMenuCYF = pygame.image.load("assets/BGMenuFYC.png")
CakeSpray = pygame.image.load("assets/CakeSpray.png")
CakeSprayS = pygame.image.load("assets/CakeSprayS.png")
BGLoadingCYF = pygame.image.load("assets/BGLoadingCYF.png")
BotonExit = pygame.image.load("assets/BotonExit.png")
BotonExitSpray = pygame.image.load("assets/BotonExitSpray.png")
BGTutorialCYF = pygame.image.load("assets/BGTutorialCYF.png")
BGScoreCYF = pygame.image.load("assets/BGScoreCYF.png")

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

#Efectos de sonido
sounds_loadingbars = [
    pygame.mixer.Sound("assets/Loading.wav"),
    pygame.mixer.Sound("assets/BurbujasLoading.wav")
]

# Diccionario para almacenar volúmenes actuales
volumen_actual = {
    "loadingbars": 0.5,
}
mute_estado = {
    "loadingbars": False,  
}

# Ajustar volúmenes iniciales
for sonido in sounds_loadingbars:
    sonido.set_volume(volumen_actual["loadingbars"])

# Función para ajustar el volumen de una lista y actualizar su almacenamiento
def ajustar_volumen(lista_sonidos, clave, incremento):
    if not mute_estado[clave]:  # Solo ajustar volumen si no está muteado
        nuevo_volumen = min(1.0, max(0.0, volumen_actual[clave] + incremento))
        volumen_actual[clave] = nuevo_volumen
        for sonido in lista_sonidos:
            sonido.set_volume(nuevo_volumen)

# Función para alternar mute/unmute
def toggle_mute(lista_sonidos, clave):
    if mute_estado[clave]:  # Si está en mute, restaurar el volumen
        for sonido in lista_sonidos:
            sonido.set_volume(volumen_actual[clave])
        print(f"{clave.capitalize()} desmuteados. Volumen: {volumen_actual[clave]*100:.0f}%")
    else:  # Si no está en mute, silenciar
        for sonido in lista_sonidos:
            sonido.set_volume(0.0)
        print(f"{clave.capitalize()} muteados.")
    mute_estado[clave] = not mute_estado[clave]

# Configuración de la playlist
CARPETA_MUSICA = "musica"  # Carpeta donde se almacenan las canciones
VOLUMEN_INICIAL = 0.5      # Volumen inicial (0.0 a 1.0)
mute_music = False
# Cargar canciones automáticamente desde la carpeta
playlist = [
    os.path.join(CARPETA_MUSICA, archivo) 
    for archivo in os.listdir(CARPETA_MUSICA) 
    if archivo.endswith((".ogg", ".wav", ".mp3"))
]
if not playlist:
    print("No se encontraron canciones en la carpeta especificada.")
    pygame.quit()
    sys.exit()
# Mezclar la playlist aleatoriamente
random.shuffle(playlist)

# Función para reproducir la playlist
def reproducir_playlist(playlist, volumen=VOLUMEN_INICIAL):
    pygame.mixer.music.set_volume(volumen)
    if playlist:  # Si hay canciones en la playlist
        pygame.mixer.music.load(playlist[0])  # Cargar la primera canción
        pygame.mixer.music.play()
        print(f"Reproduciendo: {os.path.basename(playlist[0])}")
        # Configurar evento para cuando la canción termine
        pygame.mixer.music.set_endevent(pygame.USEREVENT)

# Función para avanzar en la playlist
def avanzar_playlist(playlist):
    if playlist:  # Si hay canciones en la lista
        playlist.append(playlist.pop(0))  # Mover la primera canción al final
        reproducir_playlist(playlist)

# Comenzar la playlist
reproducir_playlist(playlist)

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

    sounds_loadingbars[0].play(loops=0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:  # Si termina una canción
                avanzar_playlist(playlist)

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
            if event.type == pygame.USEREVENT:  # Si termina una canción
                avanzar_playlist(playlist)

        pygame.display.update()

def about():
    pygame.display.set_caption("About")
    loading_bar = LoadingBar(screen, FondoMain, start_color=(255, 212, 163), end_color=(208, 129, 89), text_color="#d08159", loading_time=1.5, segments=10)

    sounds_loadingbars[0].play(loops=0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:  # Si termina una canción
                avanzar_playlist(playlist)

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
            if event.type == pygame.USEREVENT:  # Si termina una canción
                avanzar_playlist(playlist)

        pygame.display.update()

def volumen():
    pygame.display.set_caption("Ajustar Volumen")
    loading_bar = LoadingBar(screen, FondoMain, start_color=(255, 212, 163), end_color=(208, 129, 89), text_color="#d08159", loading_time=1.5, segments=10)

    sounds_loadingbars[0].play(loops=0)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:  # Si termina una canción
                avanzar_playlist(playlist)

        # Dibujar la barra de carga
        if loading_bar.draw():  # Si la barra de carga está llena
            break  # Detener el bucle principal cuando la barra esté llena

        # Esperar un poco para que el evento de carga se vea
        pygame.time.wait(100)

    # Configurar un valor inicial del volumen
    current_volume = pygame.mixer.music.get_volume()

    while True:
        # Capturar posición del mouse
        Volumen_mouse_pos = pygame.mouse.get_pos()

        # Dibujar fondo y elementos en la pantalla
        screen.blit(FondoMain, [0, 0])

        contorno("VOLUME", get_font(100), "#d08159", "black", 640, 100)
        contorno1(f"MUSIC VOLUME: {current_volume * 100:.0f}%", get_font(60), "#ffecd6", "black", 450, 200)
        contorno1(f"LOADING VOLUME: {volumen_actual['loadingbars']*100:.0f}%", get_font(60), "#ffecd6", "black", 410, 280)

        #Botones para volumen musica
        Subir_Volumen_Musica = Button(SubirVolumen, pos=(860, 195), 
                            text_input="", font=get_font(75), base_color="#000000", hovering_color="White")
        Subir_Volumen_Musica.update(screen)

        Bajar_Volumen_Musica = Button(BajarVolumen, pos=(960, 195), 
                            text_input="", font=get_font(75), base_color="#000000", hovering_color="White")
        Bajar_Volumen_Musica.update(screen)

        Volumen_Mute_Musica = Button(VolumenMute, pos=(1060, 195), 
                            text_input="", font=get_font(75), base_color="#000000", hovering_color="White")
        Volumen_Mute_Musica.update(screen)

        #Botones para volumen loadingbars
        Subir_Volumen_loadingbars = Button(SubirVolumen, pos=(860, 275), 
                            text_input="", font=get_font(75), base_color="#000000", hovering_color="White")
        Subir_Volumen_loadingbars.update(screen)

        Bajar_Volumen_loadingbars = Button(BajarVolumen, pos=(960, 275), 
                            text_input="", font=get_font(75), base_color="#000000", hovering_color="White")
        Bajar_Volumen_loadingbars.update(screen)

        Volumen_Mute_loadingbars = Button(VolumenMute, pos=(1060, 275), 
                            text_input="", font=get_font(75), base_color="#000000", hovering_color="White")
        Volumen_Mute_loadingbars.update(screen)

        #Botón de regreso al menú principal
        About_back = Button(image=pygame.image.load("assets/MainButton.png"), pos=(640, 600), 
                            text_input="BACK", font=get_font(75), base_color="#000000", hovering_color="White")

        #Actualizar color y estado del botón
        About_back.changeColor(Volumen_mouse_pos)
        About_back.update(screen)

        if current_volume == 0:
            Volumen_Mute_Musica.update(screen)

        #Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #Salir del juego
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  #Volver al menú principal
                if About_back.checkForInput(Volumen_mouse_pos):
                    main_menu()
                #Musica
                if Subir_Volumen_Musica.checkForInput(Volumen_mouse_pos):
                    current_volume = min(current_volume + 0.05, 1.0)  # Limitar a 1.0 (100%)
                    pygame.mixer.music.set_volume(current_volume)
                    print(f"Volumen: {current_volume * 100:.0f}%")
                if Bajar_Volumen_Musica.checkForInput(Volumen_mouse_pos):
                    current_volume = max(current_volume - 0.05, 0.0)  #Limitar a 0.0 (0%)
                    pygame.mixer.music.set_volume(current_volume)
                    print(f"Volumen: {current_volume * 100:.0f}%")
                if Volumen_Mute_Musica.checkForInput(Volumen_mouse_pos):
                    global mute_music
                    if not mute_music:
                        pygame.mixer.music.set_volume(0.0)  # Mute música
                        print("Música muteada")
                    else:
                        pygame.mixer.music.set_volume(VOLUMEN_INICIAL)  # Restaurar volumen
                        print(f"Música desmuteada. Volumen: {VOLUMEN_INICIAL * 100:.0f}%")
                    mute_music = not mute_music  # Alternar estado de mute
                #Loadingbars
                if Subir_Volumen_loadingbars.checkForInput(Volumen_mouse_pos):
                    ajustar_volumen(sounds_loadingbars, "loadingbars", 0.05)
                    print(f"Volumen loadingbars: {volumen_actual['loadingbars']*100:.0f}%")
                if Bajar_Volumen_loadingbars.checkForInput(Volumen_mouse_pos):
                    ajustar_volumen(sounds_loadingbars, "loadingbars", -0.05)
                    print(f"Volumen loadingbars: {volumen_actual['loadingbars']*100:.0f}%")
                if Volumen_Mute_loadingbars.checkForInput(Volumen_mouse_pos):
                    toggle_mute(sounds_loadingbars, "loadingbars")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # Subir volumen
                    ajustar_volumen(sounds_loadingbars, "loadingbars", 0.05)
                    print(f"Volumen loadingbars: {volumen_actual['loadingbars']*100:.0f}%")
                elif event.key == pygame.K_DOWN:
                    # Bajar volumen
                    ajustar_volumen(sounds_loadingbars, "loadingbars", -0.05)
                    print(f"Volumen loadingbars: {volumen_actual['loadingbars']*100:.0f}%")
            if event.type == pygame.USEREVENT:  #Avanzar la playlist automáticamente
                avanzar_playlist(playlist)

        #Actualizar la pantalla
        pygame.display.update()

def menu_reaction_game():
    pygame.display.set_caption("Menú Reaction Game")
    loading_bar = LoadingBar(screen, BGLoadingReactionGame, start_color=(255, 255, 255), end_color=(250, 140, 180), text_color="#2e67a5", loading_time=1.5, segments=10)

    while True:
        sounds_loadingbars[1].play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:  # Si termina una canción
                avanzar_playlist(playlist)

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
            sounds_loadingbars[1].play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)

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
        burbuja_clickeada = False

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

                # Restablecer estado de la burbuja para permitir nuevos clics
                burbuja_clickeada = False

                # Mostrar puntaje
                texto_puntaje_ReactionGame = get_font(40).render(f"SCORE: {puntaje}", True, "black")
                texto_puntaje_ReactionGame_rect = texto_puntaje_ReactionGame.get_rect(center=(640,50))
                screen.blit(texto_puntaje_ReactionGame, texto_puntaje_ReactionGame_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not burbuja_clickeada:  # Solo procesar si la burbuja no fue clickeada
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

                            # Marcar la burbuja como clickeada
                            burbuja_clickeada = True

                    if ReactionGame_exit.checkForInput(reaction_games_mouse_pos):
                        save_score(puntaje, player_name)
                        menu_reaction_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        save_score(puntaje, player_name)
                        reaction_games()
                if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)

            pygame.display.flip()
            clock.tick(60)  # Mantener 60 FPS

    def tutorial_reaction_game():
        pygame.display.set_caption("Tutorial Reaction Game")
        loading_bar = LoadingBar(screen, BGLoadingReactionGame, start_color=(255, 255, 255), end_color=(250, 140, 180), text_color="#2e67a5", loading_time=1.5, segments=10)

        while True:
            sounds_loadingbars[1].play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)

            # Dibujar la barra de carga
            if loading_bar.draw():  # Si la barra de carga está llena
                break  # Detener el bucle principal cuando la barra esté llena

            # Esperar un poco para que el evento de carga se vea
            pygame.time.wait(100)
        
        def tutorialreactiongame():
            pygame.display.set_caption("Reaction Game")
            loading_bar = LoadingBar(screen, BGLoadingReactionGame, start_color=(255, 255, 255), end_color=(250, 140, 180), text_color="#2e67a5", loading_time=1.5, segments=10)

            while True:
                sounds_loadingbars[1].play()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.USEREVENT:  # Si termina una canción
                        avanzar_playlist(playlist)

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
            burbuja_clickeada = False

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

                    # Restablecer estado de la burbuja para permitir nuevos clics
                    burbuja_clickeada = False

                    # Mostrar puntaje
                    texto_puntaje_ReactionGame = get_font(40).render(f"SCORE: {puntaje}", True, "black")
                    texto_puntaje_ReactionGame_rect = texto_puntaje_ReactionGame.get_rect(center=(640,50))
                    screen.blit(texto_puntaje_ReactionGame, texto_puntaje_ReactionGame_rect)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if not burbuja_clickeada:  # Solo procesar si la burbuja no fue clickeada
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

                                # Marcar la burbuja como clickeada
                                burbuja_clickeada = True
                        if ReactionGame_exit.checkForInput(reaction_games_mouse_pos):
                            tutorial_reaction_game()
                    if event.type == pygame.USEREVENT:  # Si termina una canción
                        avanzar_playlist(playlist)

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
                if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)
            pygame.display.update()
    
    def score_reaction_game():
        pygame.display.set_caption("Score Reaction Game")
        loading_bar = LoadingBar(screen, BGLoadingReactionGame, start_color=(255, 255, 255), end_color=(250, 140, 180), text_color="#2e67a5", loading_time=1.5, segments=10)

        while True:
            sounds_loadingbars[1].play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)

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
                if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)

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
                    Musica_Menu.stop()
                    reaction_games()
                if Back_reaction_game_button.checkForInput(Menu_reaction_game_mouse_pos):
                    games()
                if Tutorial_reaction_game_button.checkForInput(Menu_reaction_game_mouse_pos):
                    tutorial_reaction_game()
                if Score_reaction_game_button.checkForInput(Menu_reaction_game_mouse_pos):
                    score_reaction_game()
            if event.type == pygame.USEREVENT:  # Si termina una canción
                avanzar_playlist(playlist)

        pygame.display.update()

def menu_simon_dice():
    pygame.display.set_caption("Simon Dice")
    loading_bar = LoadingBar(screen, BGSimonDiceLoading, start_color=(240, 246, 240), end_color=(0, 0, 0), text_color="#f0f6f0", loading_time=1.5, segments=10)
    Scores_file = "Top_scores_simon_dice.json"

    def simon_dice():
        loading_bar = LoadingBar(screen, BGSimonDiceLoading, start_color=(240, 246, 240), end_color=(0, 0, 0), text_color="#f0f6f0", loading_time=1.5, segments=10)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)

            # Dibujar la barra de carga
            if loading_bar.draw():  # Si la barra de carga está llena
                break  # Detener el bucle principal cuando la barra esté llena

            #Esperar un poco para que el evento de carga se vea
            pygame.time.wait(100)

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
        espacio = 80
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
        jugando = False  # Controla si el jugador puede interactuar

        # Cargar imágenes de corazones
        corazon = pygame.image.load("assets/Heart.png").convert_alpha()
        corazon_tamaño = (50, 50)  # Tamaño de los corazones
        corazon1 = pygame.transform.scale(corazon, corazon_tamaño)
        corazon_vacio = pygame.image.load("assets/Heart-1.png").convert_alpha()
        corazon_vacio1 = pygame.transform.scale(corazon_vacio, corazon_tamaño)

        # Configuración de vidas
        max_vidas = 3
        vidas = max_vidas

        # Botón de salida
        SimonDice_exit = Button(
            ExitButtonSimonDice, pos=(1104, 644),
            text_input="EXIT", font=get_font(40), base_color="#f0f6f0", hovering_color="#b8b5b9"
        )

        # Estados del juego
        ESTADO_GENERANDO = 'GENERANDO_SECUENCIA'
        ESTADO_JUGANDO = 'JUGANDO'
        ESTADO_GAME_OVER = 'GAME_OVER'
        estado = ESTADO_GENERANDO
        tiempo_evento = 0  # Tiempo para manejar eventos basados en tiempo

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
            screen.blit(BGSimonDice, (0, 0))

            # Mostrar puntaje
            contorno1(f"SCORE: {score}", get_font(50), "#f0f6f0", "black", 640, 40)

            if estado == ESTADO_JUGANDO:
                SimonDice_exit.update(screen)
                SimonDice_exit.changeColor(simon_dice_mouse_pos)

            dibujar_vidas(vidas)

            for color, rect in botones.items():
                if highlight == color:
                    screen.blit(imagenes_highlight[color], rect)
                else:
                    screen.blit(imagenes[color], rect)
            pygame.display.update([rect for rect in botones.values()])
            # No es necesario llamar a flip después de update
            # pygame.display.flip()

        def mostrar_mensaje(texto, color=(255, 255, 255), tamaño=50, x=size[0] // 2, y=size[1] // 2):
            contorno1(texto, get_font(tamaño), color, "black", x, y)
            pygame.display.flip()

        def play_secuencia(seq):
            nonlocal estado, tiempo_evento
            estado = ESTADO_GENERANDO
            jugando = False
            print(f"Estado de jugando: {jugando}")

            # Limpiar eventos previos
            pygame.event.clear()

            # Mostrar mensaje "GENERANDO SECUENCIA..."
            screen.blit(BGSimonDice, (0, 0))  # Redibuja el fondo
            contorno1(f"SCORE: {score}", get_font(50), "#f0f6f0", "black", 640, 40)
            mostrar_mensaje("GENERANDO SECUENCIA...", tamaño=60, color="#f0f6f0")
            tiempo_evento = pygame.time.get_ticks()
            estado = ESTADO_GENERANDO

        def añadir_color_random(seq):
            color = random.choice(list(botones.keys()))
            seq.append(color)

        def revisar_player_secuencia():
            for i in range(len(player_secuencia)):
                if player_secuencia[i] != secuencia[i]:
                    return False
            return True

        def manejar_estado():
            nonlocal estado, tiempo_evento, jugando
            current_time = pygame.time.get_ticks()

            if estado == ESTADO_GENERANDO:
                # Después de mostrar el mensaje, empezar a mostrar la secuencia
                if current_time - tiempo_evento >= 3000:
                    # Iniciar la secuencia
                    tiempo_evento = current_time
                    for color in secuencia:
                        # Mostrar cada color con tiempos
                        screen.blit(BGSimonDice, (0, 0))
                        contorno1(f"SCORE: {score}", get_font(50), "#f0f6f0", "black", 640, 40)
                        #dibujar_vidas(vidas)
                        for c, rect in botones.items():
                            if c == color:
                                screen.blit(imagenes_highlight[c], rect)
                            else:
                                screen.blit(imagenes[c], rect)
                        pygame.display.flip()
                        pygame.time.wait(700)  # Mostrar color
                        # Restaurar botones
                        screen.blit(BGSimonDice, (0, 0))
                        contorno1(f"SCORE: {score}", get_font(50), "#f0f6f0", "black", 640, 40)
                        dibujar_vidas(vidas)
                        dibujar_botones()
                        pygame.display.flip()
                        pygame.time.wait(400)  # Pausa entre colores
                    # Mostrar mensaje "¡TU TURNO!"
                    mostrar_mensaje("¡TU TURNO!", tamaño=60, color="#f0f6f0")
                    tiempo_evento = current_time
                    estado = ESTADO_JUGANDO
                    jugando = True

            elif estado == ESTADO_JUGANDO:
                pass  # El jugador puede interactuar

        # Inicializar el primer color
        añadir_color_random(secuencia)

        while True:
            simon_dice_mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)

                if estado == ESTADO_JUGANDO and event.type == pygame.MOUSEBUTTONDOWN:
                    if SimonDice_exit.checkForInput(simon_dice_mouse_pos):
                        save_score(score, player_name)
                        menu_simon_dice()
                    for color, rect in botones.items():
                        if rect.collidepoint(simon_dice_mouse_pos):
                            player_secuencia.append(color)
                            dibujar_botones(color)
                            pygame.display.flip()
                            # Añadir un pequeño retardo sin bloquear
                            tiempo_evento = pygame.time.get_ticks()
                            while pygame.time.get_ticks() - tiempo_evento < 300:
                                for sub_event in pygame.event.get():
                                    if sub_event.type == pygame.QUIT:
                                        pygame.quit()
                                        return
                                clock.tick(60)
                            dibujar_botones()
                            pygame.display.flip()
                            tiempo_evento = pygame.time.get_ticks()
                            while pygame.time.get_ticks() - tiempo_evento < 100:
                                for sub_event in pygame.event.get():
                                    if sub_event.type == pygame.QUIT:
                                        pygame.quit()
                                        return
                                clock.tick(60)

                            if not revisar_player_secuencia():
                                vidas -= 1
                                mostrar_mensaje("¡SECUENCIA INCORRECTA!", tamaño=60, color="#b45252")
                                # Esperar sin bloquear
                                tiempo_evento = pygame.time.get_ticks()
                                while pygame.time.get_ticks() - tiempo_evento < 3000:
                                    for sub_event in pygame.event.get():
                                        if sub_event.type == pygame.QUIT:
                                            pygame.quit()
                                            return
                                    clock.tick(60)
                                screen.blit(BGSimonDice, (0,0))
                                dibujar_vidas_grande(vidas)
                                pygame.display.flip()
                                tiempo_evento = pygame.time.get_ticks()
                                while pygame.time.get_ticks() - tiempo_evento < 3000:
                                    for sub_event in pygame.event.get():
                                        if sub_event.type == pygame.QUIT:
                                            pygame.quit()
                                            return
                                    clock.tick(60)
                                player_secuencia = []

                                if vidas <= 0:
                                    mostrar_mensaje("GAME OVER", tamaño=80, color="#FF0000")
                                    tiempo_evento = pygame.time.get_ticks()
                                    while pygame.time.get_ticks() - tiempo_evento < 3000:
                                        for sub_event in pygame.event.get():
                                            if sub_event.type == pygame.QUIT:
                                                pygame.quit()
                                                return
                                        clock.tick(60)
                                    save_score(score, player_name)
                                    menu_simon_dice()
                                    return
                            
                                play_secuencia(secuencia)
                            if len(player_secuencia) == len(secuencia):
                                score += 1
                                mostrar_mensaje("¡SECUENCIA CORRECTA!", tamaño=60, color="#8ab060")
                                # Esperar sin bloquear
                                tiempo_evento = pygame.time.get_ticks()
                                while pygame.time.get_ticks() - tiempo_evento < 3000:
                                    for sub_event in pygame.event.get():
                                        if sub_event.type == pygame.QUIT:
                                            pygame.quit()
                                            return
                                    clock.tick(60)
                                player_secuencia = []
                                añadir_color_random(secuencia)
                                play_secuencia(secuencia)

            # Manejar el estado del juego basado en tiempo
            manejar_estado()

            # Actualizar la pantalla
            dibujar_botones()
            clock.tick(30)
    
    def tutorial_simon_dice():
        pygame.display.set_caption("Tutorial Simón Dice")
        loading_bar = LoadingBar(screen, BGSimonDiceLoading, start_color=(240, 246, 240), end_color=(0, 0, 0), text_color="#f0f6f0", loading_time=1.5, segments=10)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)

            # Dibujar la barra de carga
            if loading_bar.draw():  # Si la barra de carga está llena
                break  # Detener el bucle principal cuando la barra esté llena

            # Esperar un poco para que el evento de carga se vea
            pygame.time.wait(100)

        while True:
            Tutorial_reaction_game_mouse_pos = pygame.mouse.get_pos()
            screen.blit(BGSimonDice, (0,0))
            contorno("TUTORIAL", get_font(60), "#f0f6f0", "black", 640, 45)

            contorno1("En Simón Dice, se genera una secuencia de", get_font(40), "#f0f6f0", "black", 640, 140)
            contorno1("colores que debes memorizar y repetir en el", get_font(40), "#f0f6f0", "black", 640, 190)
            contorno1("mismo orden. Cuando la secuencia termine,", get_font(40), "#f0f6f0", "black", 640, 240)
            contorno1("aparecerá el mensaje '¡ES TU TURNO!'. Si aciertas, la", get_font(40), "#f0f6f0", "black", 640, 290)
            contorno1("secuencia se hara más larga; si te equivocas, verás", get_font(40), "#f0f6f0", "black", 640, 340)
            contorno1("'SECUENCIA INCORRECTA' y perderás una vida. Tienes", get_font(40), "#f0f6f0", "black", 640, 390)
            contorno1("3 vidas, y si las pierdes todas, el juego terminará", get_font(40), "#f0f6f0", "black", 640, 440)
            contorno1("con 'GAME OVER'. El objetivo es llegar lo más lejos", get_font(40), "#f0f6f0", "black", 640, 490)
            contorno1("posible repitiendo las secuencias correctamente", get_font(40), "#f0f6f0", "black", 640, 540)

            Tutorial_reaction_game_b = Button(SimonDiceButtonGreen, pos=(320, 620), 
                            text_input="TUTORIAL", font=get_font(65), base_color="#000000", hovering_color="White")
            Back_tutorial_reaction_game_button = Button(SimonDiceButtonRed, pos=(960, 620), 
                            text_input="BACK", font=get_font(65), base_color="#000000", hovering_color="White")
            
            for button in [Back_tutorial_reaction_game_button]:
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
                        menu_simon_dice()
                if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)
            pygame.display.update()

    def scores_simon_dice():
        pygame.display.set_caption("Scores Simón Dice")
        loading_bar = LoadingBar(screen, BGSimonDiceLoading, start_color=(240, 246, 240), end_color=(0, 0, 0), text_color="#f0f6f0", loading_time=1.5, segments=10)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)

            # Dibujar la barra de carga
            if loading_bar.draw():  # Si la barra de carga está llena
                break  # Detener el bucle principal cuando la barra esté llena

            # Esperar un poco para que el evento de carga se vea
            pygame.time.wait(100)
        
        # Función para cargar los puntajes
        def load_scores():
            try:
                with open("Top_scores_simon_dice.json", "r") as file:
                    return json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                # Si no hay archivo o está corrupto, usar una lista predeterminada
                return [{"name": "---", "score": 0} for _ in range(5)]

        # Cargar los puntajes
        top_scores = load_scores()

        while True:
            Score_reaction_game_mouse_pos = pygame.mouse.get_pos()
            screen.blit(BGSimonDice, (0,0))
            #screen.fill("#222323")

            # Título de la pantalla de puntajes
            contorno("TOP SCORES", get_font(100), "#f0f6f0", "black", 640, 100)
            contorno("RANK", get_font(80), "#b45252", "black", 380, 220)
            contorno("NAME", get_font(80), "#4b80ca", "black", 640, 220)
            contorno("SCORE", get_font(80), "#8ab060", "black", 900, 220)

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
            Back_to_menu_button = Button(SimonDiceButtonYellow, pos=(640, 630), 
                                         text_input="BACK", font=get_font(65), base_color="black", hovering_color="White")

            Back_to_menu_button.changeColor(Score_reaction_game_mouse_pos)
            Back_to_menu_button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Back_to_menu_button.checkForInput(Score_reaction_game_mouse_pos):
                        menu_simon_dice()
                if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)

            pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:  # Si termina una canción
                avanzar_playlist(playlist)

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
                    tutorial_simon_dice()
                if Score_simon_dice_button.checkForInput(simon_dice_mouse_pos):
                    scores_simon_dice()
            if event.type == pygame.USEREVENT:  # Si termina una canción
                avanzar_playlist(playlist)

        pygame.display.update()

def menu_puzzle_numerico():
    pygame.display.set_caption("Menú Steal The Money")
    loading_bar = LoadingBar(screen, BGLoadingSTM, start_color=(225, 203, 134), end_color=(224, 153, 48), text_color="#e1cb86", loading_time=1.5, segments=10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:  # Si termina una canción
                avanzar_playlist(playlist)

        # Dibujar la barra de carga
        if loading_bar.draw():  # Si la barra de carga está llena
            break  # Detener el bucle principal cuando la barra esté llena

        # Esperar un poco para que el evento de carga se vea
        pygame.time.wait(100)
    
    def Steal_the_money():
        # Dimensiones de la pantalla
        SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
        BOARD_SIZE = 400
        TILE_SIZE = BOARD_SIZE // 3
        BUTTON_HEIGHT = 50

        SCORES_FILE = "top_scores_STM.json"

        # Inicializar pantalla
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Steal The Money")
        loading_bar = LoadingBar(screen, BGLoadingSTM, start_color=(225, 203, 134), end_color=(224, 153, 48), text_color="#e1cb86", loading_time=1.5, segments=10)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)

            # Dibujar la barra de carga
            if loading_bar.draw():  # Si la barra de carga está llena
                break  # Detener el bucle principal cuando la barra esté llena

        # Esperar un poco para que el evento de carga se vea
        pygame.time.wait(100)

        # Variables del cronómetro
        start_time = time.time()
        def format_time(elapsed):
            mins, secs = divmod(elapsed, 60)
            return f"{int(mins):02}:{int(secs):02}"

        # Crear tablero inicial
        def create_board():
            numbers = list(range(1, 9)) + [None]
            random.shuffle(numbers)
            return [numbers[i:i+3] for i in range(0, 9, 3)]

        def reset_game():
            global board, start_time
            board = create_board()
            start_time = time.time()
            #pygame.mixer.Sound.play(reset_sound)

        # Función para cargar los puntajes
        def load_top_scores():
            try:
                with open(SCORES_FILE, "r") as file:
                    return json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                return []

        # Función para guardar los puntajes
        def save_top_scores(top_scores):
            with open(SCORES_FILE, "w") as file:
                json.dump(top_scores, file)

        def STM_win():
            pygame.display.set_caption("Steal The Money")

            while True:
                screen.blit(BGWinSTM, (0,0))
                STM_win_mouse_pos = pygame.mouse.get_pos()

                STM_grabthemoney = Button(image=None, pos=(400, 190), 
                        text_input="GRAB THE MONEY", font=get_font(50), base_color="black", hovering_color="red")
            
                STM_reset = Button(image=None, pos=(900, 190), 
                                text_input="RESET", font=get_font(50), base_color="black", hovering_color="red")
                    
                for button in [STM_grabthemoney, STM_reset]:
                    button.changeColor(STM_win_mouse_pos)
                    button.update(screen)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if STM_grabthemoney.checkForInput(STM_win_mouse_pos):
                            menu_puzzle_numerico()
                        if STM_reset.checkForInput(STM_win_mouse_pos):
                            Steal_the_money()
                    if event.type == pygame.USEREVENT:  # Si termina una canción
                        avanzar_playlist(playlist)

                pygame.display.update()

        board = create_board()

        # Dibujar el tablero
        def draw_board():
            top_left_x = (SCREEN_WIDTH - BOARD_SIZE) // 2
            top_left_y = (SCREEN_HEIGHT - BOARD_SIZE) // 2

            # Dibujar fondo del tablero
            background_rect = pygame.Rect(top_left_x, top_left_y, BOARD_SIZE, BOARD_SIZE)
            pygame.draw.rect(screen, "gray", background_rect)  # Cambia el color según prefieras

            for row in range(3):
                for col in range(3):
                    value = board[row][col]
                    x = top_left_x + col * TILE_SIZE
                    y = top_left_y + row * TILE_SIZE
                    rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                    pygame.draw.rect(screen, "black", rect, 8)  # Grosor de las líneas modificado
                    if value is not None:
                        font = pygame.font.Font("assets/font.ttf", 80)  # Fuente modificada
                        text = font.render(str(value), True, "black")  # Color modificado
                        text_rect = text.get_rect(center=(x + TILE_SIZE // 2, y + TILE_SIZE // 2))
                        screen.blit(text, text_rect)

        # Dibujar interfaz adicional (botón y cronómetro)
        def draw_ui():
            font = pygame.font.Font("assets/font.ttf", 50)

            # Botón de salida
            button_rect = pygame.Rect((SCREEN_WIDTH - 200) // 2, SCREEN_HEIGHT - 140, 200, 50)
            pygame.draw.rect(screen, "#b8b5b9", button_rect)
            text = font.render("EXIT", True, "red")
            text_rect = text.get_rect(center=button_rect.center)
            screen.blit(text, text_rect)

            # Cronómetro
            elapsed = time.time() - start_time
            timer_text = font.render(format_time(elapsed), True, "RED")
            timer_rect = timer_text.get_rect(center=(SCREEN_WIDTH // 2, 120))
            screen.blit(timer_text, timer_rect)

        # Buscar posición de la casilla vacía
        def find_empty():
            for row in range(3):
                for col in range(3):
                    if board[row][col] is None:
                        return row, col

        # Mover casilla
        def move_tile(row, col):
            empty_row, empty_col = find_empty()
            if abs(empty_row - row) + abs(empty_col - col) == 1:  # Movimiento válido
                board[empty_row][empty_col], board[row][col] = board[row][col], board[empty_row][empty_col]
                #pygame.mixer.Sound.play(move_sound)

        # Comprobar si se ha ganado
        def check_win():
            target = list(range(1, 9)) + [None]
            current = [cell for row in board for cell in row]
            return current == target
        
        # Registrar el puntaje del jugador
        def register_score(player_name, elapsed_time):
            top_scores = load_top_scores()
            top_scores.append({"name": player_name, "time": format_time(elapsed_time)})
            top_scores = sorted(top_scores, key=lambda x: x["time"])[:5]
            save_top_scores(top_scores)

        # Bucle principal
        while True:
            screen.blit(BGPuzzleNumerico, (0, 0))
            draw_board()
            draw_ui()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    empty_row, empty_col = find_empty()
                    if event.key == pygame.K_UP and empty_row < 2:  # Mover hacia abajo
                        move_tile(empty_row + 1, empty_col)
                    elif event.key == pygame.K_DOWN and empty_row > 0:  # Mover hacia arriba
                        move_tile(empty_row - 1, empty_col)
                    elif event.key == pygame.K_LEFT and empty_col < 2:  # Mover hacia la derecha
                        move_tile(empty_row, empty_col + 1)
                    elif event.key == pygame.K_RIGHT and empty_col > 0:  # Mover hacia la izquierda
                        move_tile(empty_row, empty_col - 1)
                    if event.key == pygame.K_w and empty_row < 2:  # Mover hacia abajo
                        move_tile(empty_row + 1, empty_col)
                    elif event.key == pygame.K_s and empty_row > 0:  # Mover hacia arriba
                        move_tile(empty_row - 1, empty_col)
                    elif event.key == pygame.K_a and empty_col < 2:  # Mover hacia la derecha
                        move_tile(empty_row, empty_col + 1)
                    elif event.key == pygame.K_d and empty_col > 0:  # Mover hacia la izquierda
                        move_tile(empty_row, empty_col - 1)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    button_rect = pygame.Rect((SCREEN_WIDTH - 200) // 2, SCREEN_HEIGHT - 140, 200, 50)
                    if button_rect.collidepoint(x, y):
                        menu_puzzle_numerico()
                if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)
            
            if check_win():
                register_score(player_name, time.time() - start_time)
                STM_win()
    
    def tutorial_STM():
        pygame.display.set_caption("Tutorial Steal The Money")
        loading_bar = LoadingBar(screen, BGLoadingSTM, start_color=(225, 203, 134), end_color=(224, 153, 48), text_color="#e1cb86", loading_time=1.5, segments=10)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)

            # Dibujar la barra de carga
            if loading_bar.draw():  # Si la barra de carga está llena
                break  # Detener el bucle principal cuando la barra esté llena

            # Esperar un poco para que el evento de carga se vea
            pygame.time.wait(100)
        
        def tutorial_STM_game():
            # Dimensiones de la pantalla
            SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
            BOARD_SIZE = 400
            TILE_SIZE = BOARD_SIZE // 3
            BUTTON_HEIGHT = 50

            # Inicializar pantalla
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.set_caption("Steal The Money")
            loading_bar = LoadingBar(screen, BGLoadingSTM, start_color=(225, 203, 134), end_color=(224, 153, 48), text_color="#e1cb86", loading_time=1.5, segments=10)

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.USEREVENT:  # Si termina una canción
                        avanzar_playlist(playlist)

                # Dibujar la barra de carga
                if loading_bar.draw():  # Si la barra de carga está llena
                    break  # Detener el bucle principal cuando la barra esté llena

            # Esperar un poco para que el evento de carga se vea
            pygame.time.wait(100)

            # Variables del cronómetro
            start_time = time.time()
            def format_time(elapsed):
                mins, secs = divmod(elapsed, 60)
                return f"{int(mins):02}:{int(secs):02}"

            # Crear tablero inicial
            def create_board():
                numbers = list(range(1, 9)) + [None]
                random.shuffle(numbers)
                return [numbers[i:i+3] for i in range(0, 9, 3)]

            def reset_game():
                global board, start_time
                board = create_board()
                start_time = time.time()
                #pygame.mixer.Sound.play(reset_sound)

            def STM_win_tuto():
                pygame.display.set_caption("Steal The Money")

                while True:
                    screen.blit(BGWinSTM, (0,0))
                    STM_win_mouse_pos = pygame.mouse.get_pos()

                    STM_grabthemoney = Button(image=None, pos=(400, 190), 
                            text_input="GRAB THE MONEY", font=get_font(50), base_color="black", hovering_color="red")
            
                    STM_reset = Button(image=None, pos=(900, 190), 
                                    text_input="RESET", font=get_font(50), base_color="black", hovering_color="red")
                    
                    for button in [STM_grabthemoney, STM_reset]:
                        button.changeColor(STM_win_mouse_pos)
                        button.update(screen)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if STM_grabthemoney.checkForInput(STM_win_mouse_pos):
                                tutorial_STM()
                            if STM_reset.checkForInput(STM_win_mouse_pos):
                                tutorial_STM_game()
                        if event.type == pygame.USEREVENT:  # Si termina una canción
                            avanzar_playlist(playlist)

                    pygame.display.update()

            board = create_board()

            # Dibujar el tablero
            def draw_board():
                top_left_x = (SCREEN_WIDTH - BOARD_SIZE) // 2
                top_left_y = (SCREEN_HEIGHT - BOARD_SIZE) // 2

                # Dibujar fondo del tablero
                background_rect = pygame.Rect(top_left_x, top_left_y, BOARD_SIZE, BOARD_SIZE)
                pygame.draw.rect(screen, "gray", background_rect)  # Cambia el color según prefieras

                for row in range(3):
                    for col in range(3):
                        value = board[row][col]
                        x = top_left_x + col * TILE_SIZE
                        y = top_left_y + row * TILE_SIZE
                        rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                        pygame.draw.rect(screen, "black", rect, 8)  # Grosor de las líneas modificado
                        if value is not None:
                            font = pygame.font.Font("assets/font.ttf", 80)  # Fuente modificada
                            text = font.render(str(value), True, "black")  # Color modificado
                            text_rect = text.get_rect(center=(x + TILE_SIZE // 2, y + TILE_SIZE // 2))
                            screen.blit(text, text_rect)

            # Dibujar interfaz adicional (botón y cronómetro)
            def draw_ui():
                font = pygame.font.Font("assets/font.ttf", 50)

                # Botón de salida
                button_rect = pygame.Rect((SCREEN_WIDTH - 200) // 2, SCREEN_HEIGHT - 140, 200, 50)
                pygame.draw.rect(screen, "#b8b5b9", button_rect)
                text = font.render("EXIT", True, "red")
                text_rect = text.get_rect(center=button_rect.center)
                screen.blit(text, text_rect)

                # Cronómetro
                elapsed = time.time() - start_time
                timer_text = font.render(format_time(elapsed), True, "RED")
                timer_rect = timer_text.get_rect(center=(SCREEN_WIDTH // 2, 120))
                screen.blit(timer_text, timer_rect)

            # Buscar posición de la casilla vacía
            def find_empty():
                for row in range(3):
                    for col in range(3):
                        if board[row][col] is None:
                            return row, col

            # Mover casilla
            def move_tile(row, col):
                empty_row, empty_col = find_empty()
                if abs(empty_row - row) + abs(empty_col - col) == 1:  # Movimiento válido
                    board[empty_row][empty_col], board[row][col] = board[row][col], board[empty_row][empty_col]
                    #pygame.mixer.Sound.play(move_sound)

            # Comprobar si se ha ganado
            def check_win():
                target = list(range(1, 9)) + [None]
                current = [cell for row in board for cell in row]
                return current == target

            # Bucle principal
            while True:
                screen.blit(BGPuzzleNumerico, (0, 0))
                draw_board()
                draw_ui()
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        empty_row, empty_col = find_empty()
                        if event.key == pygame.K_UP and empty_row < 2:  # Mover hacia abajo
                            move_tile(empty_row + 1, empty_col)
                        elif event.key == pygame.K_DOWN and empty_row > 0:  # Mover hacia arriba
                            move_tile(empty_row - 1, empty_col)
                        elif event.key == pygame.K_LEFT and empty_col < 2:  # Mover hacia la derecha
                            move_tile(empty_row, empty_col + 1)
                        elif event.key == pygame.K_RIGHT and empty_col > 0:  # Mover hacia la izquierda
                            move_tile(empty_row, empty_col - 1)
                        if event.key == pygame.K_w and empty_row < 2:  # Mover hacia abajo
                            move_tile(empty_row + 1, empty_col)
                        elif event.key == pygame.K_s and empty_row > 0:  # Mover hacia arriba
                            move_tile(empty_row - 1, empty_col)
                        elif event.key == pygame.K_a and empty_col < 2:  # Mover hacia la derecha
                            move_tile(empty_row, empty_col + 1)
                        elif event.key == pygame.K_d and empty_col > 0:  # Mover hacia la izquierda
                            move_tile(empty_row, empty_col - 1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        button_rect = pygame.Rect((SCREEN_WIDTH - 200) // 2, SCREEN_HEIGHT - 140, 200, 50)
                        if button_rect.collidepoint(x, y):
                            tutorial_STM()
                    if event.type == pygame.USEREVENT:  # Si termina una canción
                        avanzar_playlist(playlist)
                
                elapsed = time.time() - start_time
                if elapsed >= 30:
                    STM_win_tuto()

                if check_win():
                    STM_win_tuto()
        
        while True:
            screen.blit(BGTutorialSTM, (0,0))
            tutorial_STM_mouse_pos = pygame.mouse.get_pos()

            contorno("TUTORIAL", get_font(80), "red", "black", 640, 120)
            contorno1("¡Bienvenido al juego de puzzle numérico! Tu", get_font(30), "#e1cb86", "black", 640, 200)
            contorno1("objetivo es ordenar los números del 1 al 8 en un", get_font(30), "#e1cb86", "black", 640, 250)
            contorno1("tablero de 3x3, dejando la casilla vacía en la esquina", get_font(30), "#e1cb86", "black", 640, 300)
            contorno1("inferior derecha. Desliza las piezas moviéndolas", get_font(30), "#e1cb86", "black", 640, 350)
            contorno1("hacia el espacio vacío para reorganizarlas. Usa las", get_font(30), "#e1cb86", "black", 640, 400)
            contorno1("flechas del teclado para jugar. ¡Piensa estratégicamente,", get_font(30), "#e1cb86", "black", 640, 450)
            contorno1("resuelve el puzzle y demuestra tu habilidad!", get_font(30), "#e1cb86", "black", 640, 500)

            STM_tutorial_back = Button(BackSTM, pos=(60, 390), 
                            text_input="", font=get_font(60), base_color="#222323", hovering_color="#e1cb86")
            
            STM_tutorial = Button(image=None, pos=(1070, 580), 
                            text_input="TUTORIAL", font=get_font(30), base_color="black", hovering_color="red")
            
            for button in [STM_tutorial_back, STM_tutorial]:
                button.changeColor(tutorial_STM_mouse_pos)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if STM_tutorial_back.checkForInput(tutorial_STM_mouse_pos):
                        menu_puzzle_numerico()
                    if STM_tutorial.checkForInput(tutorial_STM_mouse_pos):
                        tutorial_STM_game()
                if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)

            pygame.display.update()
    
    def score_STM():
        pygame.display.set_caption("Score Steal The Money")
        loading_bar = LoadingBar(screen, BGLoadingSTM, start_color=(225, 203, 134), end_color=(224, 153, 48), text_color="#e1cb86", loading_time=1.5, segments=10)
        SCORES_FILE = "top_scores_STM.json"

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)

            # Dibujar la barra de carga
            if loading_bar.draw():  # Si la barra de carga está llena
                break  # Detener el bucle principal cuando la barra esté llena

            # Esperar un poco para que el evento de carga se vea
            pygame.time.wait(100)
        
        def load_top_scores():
            try:
                with open(SCORES_FILE, "r") as file:
                    return json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                return []
        
        # Cargar puntajes
        top_scores = load_top_scores()
        
        while True:
            screen.blit(BGScoresSTM, (0, 0))

            STM_score_mouse_pos = pygame.mouse.get_pos()

            ##e2c56e

            contorno("TOP SCORES", get_font(90), "red", "black", 640, 120)
            contorno("RANK", get_font(80), "#e2c56e", "black", 380, 220)
            contorno("NAME", get_font(80), "#e2c56e", "black", 640, 220)
            contorno("SCORE", get_font(80), "#e2c56e", "black", 900, 220)

            STM_score_back = Button(BackSTM, pos=(60, 390), 
                            text_input="", font=get_font(60), base_color="#222323", hovering_color="#e1cb86")
            
            for button in [STM_score_back]:
                button.changeColor(STM_score_mouse_pos)
                button.update(screen)

            # Dibujar puntajes
            for i, entry in enumerate(top_scores[:5]):
                rank_text = f"{i + 1}st" if i == 0 else f"{i + 1}nd" if i == 1 else f"{i + 1}rd" if i == 2 else f"{i + 1}th"
                rank_text = get_font(50).render(rank_text, True, "black")
                rank_text_rect = rank_text.get_rect(center=(380, 300 + i *60))
                screen.blit(rank_text, rank_text_rect)
                name_text = get_font(50).render(entry["name"], True, "black")
                name_text_rect = name_text.get_rect(center=(640, 300 + i * 60))
                screen.blit(name_text, name_text_rect)
                score_text = get_font(50).render(str(entry["time"]), True, "black")
                score_text_rect = score_text.get_rect(center=(900, 300 + i * 60))
                screen.blit(score_text, score_text_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if STM_score_back.checkForInput(STM_score_mouse_pos):
                        menu_puzzle_numerico()

            pygame.display.update()


    while True:
        screen.blit(BGMenuPuzzleNumerico, (0, 0))

        STM_mouse_pos = pygame.mouse.get_pos()

        contorno("STEAL THE MONEY", get_font(100), "#e1cb86", "black", 640, 80)

        STM_play = Button(ButtonSTM, pos=(160, 280), 
                            text_input="PLAY", font=get_font(60), base_color="#222323", hovering_color="#e1cb86")
        
        STM_back = Button(ButtonSTM, pos=(480, 320), 
                            text_input="BACK", font=get_font(60), base_color="#222323", hovering_color="#e1cb86")
        
        STM_tutorial = Button(ButtonSTM, pos=(800, 260), 
                            text_input="TUTORIAL", font=get_font(40), base_color="#222323", hovering_color="#e1cb86")
        
        STM_score = Button(ButtonSTM, pos=(1120, 290), 
                            text_input="SCORE", font=get_font(55), base_color="#222323", hovering_color="#e1cb86")
        
        for button in [STM_play, STM_back, STM_tutorial, STM_score]:
            button.changeColor(STM_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if STM_back.checkForInput(STM_mouse_pos):
                    games()
                if STM_play.checkForInput(STM_mouse_pos):
                    Steal_the_money()
                if STM_tutorial.checkForInput(STM_mouse_pos):
                    tutorial_STM()
                if STM_score.checkForInput(STM_mouse_pos):
                    score_STM()
            if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)

        pygame.display.update()

def menu_colores_y_figuras():
    pygame.display.set_caption("Colores Y Figuras")
    loading_bar = LoadingBar(screen, BGLoadingCYF, start_color=(232, 193, 112), end_color=(165, 48, 48), text_color="#4f8fba", loading_time=1.5, segments=10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:  # Si termina una canción
                avanzar_playlist(playlist)

        # Dibujar la barra de carga
        if loading_bar.draw():  # Si la barra de carga está llena
            break  # Detener el bucle principal cuando la barra esté llena

        # Esperar un poco para que el evento de carga se vea
        pygame.time.wait(100)

    Scores_file = "Top_scores_CYF.json"
    
    def CYF_game():
        #screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Colores Y Figuras")
        loading_bar = LoadingBar(screen, BGLoadingCYF, start_color=(232, 193, 112), end_color=(165, 48, 48), text_color="#4f8fba", loading_time=1.5, segments=10)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)

            # Dibujar la barra de carga
            if loading_bar.draw():  # Si la barra de carga está llena
                break  # Detener el bucle principal cuando la barra esté llena

            # Esperar un poco para que el evento de carga se vea
            pygame.time.wait(100)

        # Configuración de la pantalla
        WIDTH, HEIGHT = 1280, 720

        BGFigurasYColores = pygame.image.load("assets/BGgameFYC.png")

        # Colores
        COLORS = {
            "ROJO": (165, 48, 48),
            "VERDE": (117, 167, 67),
            "AZUL": (79, 143, 186),
            "AMARILLO": (232, 193, 112),
            "MORADO": (64, 39, 81)
        }

        # Configuración del reloj
        clock = pygame.time.Clock()
        FPS = 60

        # Clase Figura
        class Figura:
            def __init__(self, x, y, color, tipo):
                self.x = x
                self.y = y
                self.color = color
                self.tipo = tipo
                self.rect = pygame.Rect(x, y, 50, 50)

            def dibujar(self, pantalla):
                if self.tipo == "CIRCULO":
                    pygame.draw.circle(pantalla, self.color, (self.x + 25, self.y + 25), 25)
                    pygame.draw.circle(pantalla, (0, 0, 0), (self.x + 25, self.y + 25), 25, 2)  # Contorno negro
                elif self.tipo == "CUADRADO":
                    pygame.draw.rect(pantalla, self.color, self.rect)
                    pygame.draw.rect(pantalla, (0, 0, 0), self.rect, 2)  # Contorno negro
                elif self.tipo == "TRIANGULO":
                    puntos = [(self.x + 25, self.y), (self.x, self.y + 50), (self.x + 50, self.y + 50)]
                    pygame.draw.polygon(pantalla, self.color, puntos)
                    pygame.draw.polygon(pantalla, (0, 0, 0), puntos, 2)  # Contorno negro
                elif self.tipo == "RECTANGULO":
                    pygame.draw.rect(pantalla, self.color, (self.x, self.y, 60, 40))
                    pygame.draw.rect(pantalla, (0, 0, 0), (self.x, self.y, 60, 40), 2)  # Contorno negro
                elif self.tipo == "ROMBO":
                    puntos = [(self.x + 25, self.y), (self.x, self.y + 25), (self.x + 25, self.y + 50), (self.x + 50, self.y + 25)]
                    pygame.draw.polygon(pantalla, self.color, puntos)
                    pygame.draw.polygon(pantalla, (0, 0, 0), puntos, 2)  # Contorno negro
                elif self.tipo == "ESTRELLA":
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
                elif self.tipo == "OVALO":
                    pygame.draw.ellipse(pantalla, self.color, (self.x, self.y, 60, 40))
                    pygame.draw.ellipse(pantalla, (0, 0, 0), (self.x, self.y, 60, 40), 2)  # Contorno negro
                elif self.tipo == "PENTAGONO":
                    puntos = [
                        (self.x + 25, self.y),
                        (self.x + 50, self.y + 20),
                        (self.x + 40, self.y + 50),
                        (self.x + 10, self.y + 50),
                        (self.x, self.y + 20)
                    ]
                    pygame.draw.polygon(pantalla, self.color, puntos)
                    pygame.draw.polygon(pantalla, (0, 0, 0), puntos, 2)  # Contorno negro
                elif self.tipo == "HEXAGONO":
                    puntos = [
                        (self.x + 25, self.y),
                        (self.x + 45, self.y + 15),
                        (self.x + 45, self.y + 35),
                        (self.x + 25, self.y + 50),
                        (self.x + 5, self.y + 35),
                        (self.x + 5, self.y + 15)
                    ]
                    pygame.draw.polygon(pantalla, self.color, puntos)
                    pygame.draw.polygon(pantalla, (0, 0, 0), puntos, 2)  # Contorno negro


            def clicado(self, pos):
                if self.tipo == "CIRCULO":
                    distancia = ((self.x + 25 - pos[0]) ** 2 + (self.y + 25 - pos[1]) ** 2) ** 0.5
                    return distancia <= 25
                elif self.tipo == "CUADRADO":
                    return self.rect.collidepoint(pos)
                elif self.tipo == "TRIANGULO":
                    puntos = [(self.x + 25, self.y), (self.x, self.y + 50), (self.x + 50, self.y + 50)]
                    return pygame.draw.polygon(screen, (0, 0, 0), puntos, 2).collidepoint(pos)
                elif self.tipo == "RECTANGULO":
                    return pygame.Rect(self.x, self.y, 60, 40).collidepoint(pos)
                elif self.tipo == "ROMBO":
                    puntos = [(self.x + 25, self.y), (self.x, self.y + 25), (self.x + 25, self.y + 50), (self.x + 50, self.y + 25)]
                    return pygame.draw.polygon(screen, (0, 0, 0), puntos, 2).collidepoint(pos)
                elif self.tipo == "ESTRELLA":
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
                elif self.tipo == "OVALO":
                    return pygame.Rect(self.x, self.y, 60, 40).collidepoint(pos)
                elif self.tipo == "PENTAGONO":
                    puntos = [
                        (self.x + 25, self.y),
                        (self.x + 50, self.y + 20),
                        (self.x + 40, self.y + 50),
                        (self.x + 10, self.y + 50),
                        (self.x, self.y + 20)
                    ]
                    return pygame.draw.polygon(screen, (0, 0, 0), puntos, 2).collidepoint(pos)
                elif self.tipo == "HEXAGONO":
                    puntos = [
                        (self.x + 25, self.y),
                        (self.x + 45, self.y + 15),
                        (self.x + 45, self.y + 35),
                        (self.x + 25, self.y + 50),
                        (self.x + 5, self.y + 35),
                        (self.x + 5, self.y + 15)
                    ]
                    return pygame.draw.polygon(screen, (0, 0, 0), puntos, 2).collidepoint(pos)
        
        def game_over(puntaje):
            while True:
                screen.blit(BGFigurasYColores, (0,0))
                pos = pygame.mouse.get_pos()

                contorno("GAME OVER", get_font(100), "red", "black", 640, 280)
                contorno1(f"PUNTAJE: {puntaje}", get_font(60), "#75a743", "black", 640, 360)
                contorno1("PRESS R TO RESET", get_font(40), "#e8c170", "black", 640, 420)
                # Dibujar texto
                contorno1(objetivo_texto, get_font(30), "#e8c170", "black", 380, 40)

                # Dibujar temporizador
                contorno1(f"TIEMPO RESTANTE: {int(tiempo_restante)} s", get_font(30), "#a53030","black", 380, 80)

                CYF_exit = Spray(base_image=BotonExit, hover_image=BotonExitSpray, pos=(1220, 660))
                CYF_exit.changeImage(pos)
                CYF_exit.update(screen)  # Dibujar el botón

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.USEREVENT:  # Si termina una canción
                        avanzar_playlist(playlist)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            CYF_game()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if CYF_exit.checkForInput(pos):
                            menu_colores_y_figuras()
                    if event.type == pygame.USEREVENT:  # Si termina una canción
                        avanzar_playlist(playlist)
                
                pygame.display.update()

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
        
        # Función principal del juego  
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
                tipo = random.choice(["CIRCULO", "CUADRADO", "TRIANGULO", "RECTANGULO", "ROMBO", "ESTRELLA", "OVALO", "PENTAGONO", "HEXAGONO"])
                figuras.append(Figura(x, y, color, tipo))

            # Elegir figura objetivo
            objetivo = random.choice(figuras)
            nombre_color = [k for k, v in COLORS.items() if v == objetivo.color][0]

            # Identificar todas las figuras que coincidan con el objetivo
            figuras_objetivo = [figura for figura in figuras if figura.color == objetivo.color and figura.tipo == objetivo.tipo]

            objetivo_texto = f"HAZ CLIC EN UN {objetivo.tipo} DE COLOR {nombre_color}"

            # Temporizador
            tiempo_restante = tiempo_limite
            inicio_nivel = pygame.time.get_ticks()

            # Ciclo del nivel
            while True:
                screen.blit(BGFigurasYColores, (0,0))
                pos = pygame.mouse.get_pos()

                # Calcular tiempo restante
                tiempo_actual = pygame.time.get_ticks()
                tiempo_restante = tiempo_limite - (tiempo_actual - inicio_nivel) / 1000

                if tiempo_restante <= 0:
                    save_score(puntaje, player_name)
                    game_over(puntaje)

                # Dibujar texto
                contorno1(objetivo_texto, get_font(30), "#e8c170", "black", 380, 40)

                # Dibujar temporizador
                contorno1(f"TIEMPO RESTANTE: {int(tiempo_restante)} s", get_font(30), "#a53030","black", 380, 80)

                CYF_exit = Spray(base_image=BotonExit, hover_image=BotonExitSpray, pos=(1220, 660))
                CYF_exit.changeImage(pos)
                CYF_exit.update(screen)  # Dibujar el botón

                # Dibujar figuras
                for figura in figuras:
                    figura.dibujar(screen)

                # Manejo de eventos
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if any(figura.clicado(pos) for figura in figuras_objetivo):
                            puntaje += 1
                            nivel += 1
                            tiempo_limite += 0.5  # Incrementar tiempo límite con cada acierto
                            break
                        else:
                            save_score(puntaje, player_name)
                            game_over(puntaje)
                        if CYF_exit.checkForInput(pos):
                            menu_colores_y_figuras()

                    if event.type == pygame.USEREVENT:  # Si termina una canción
                        avanzar_playlist(playlist)

                else:
                    # Actualizar pantalla
                    pygame.display.flip()
                    clock.tick(FPS)
                    continue
                break

    def CYF_tutorial():
        pygame.display.set_caption("Tutorial Colores Y Figuras")
        loading_bar = LoadingBar(screen, BGLoadingCYF, start_color=(232, 193, 112), end_color=(165, 48, 48), text_color="#4f8fba", loading_time=1.5, segments=10)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)

            # Dibujar la barra de carga
            if loading_bar.draw():  # Si la barra de carga está llena
                break  # Detener el bucle principal cuando la barra esté llena

            # Esperar un poco para que el evento de carga se vea
            pygame.time.wait(100)

        def CYF_tutorial_game():
            #screen = pygame.display.set_mode((1280, 720))
            pygame.display.set_caption("Colores Y Figuras")
            loading_bar = LoadingBar(screen, BGLoadingCYF, start_color=(232, 193, 112), end_color=(165, 48, 48), text_color="#4f8fba", loading_time=1.5, segments=10)

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.USEREVENT:  # Si termina una canción
                        avanzar_playlist(playlist)

                # Dibujar la barra de carga
                if loading_bar.draw():  # Si la barra de carga está llena
                    break  # Detener el bucle principal cuando la barra esté llena

                # Esperar un poco para que el evento de carga se vea
                pygame.time.wait(100)

            # Configuración de la pantalla
            WIDTH, HEIGHT = 1280, 720

            BGFigurasYColores = pygame.image.load("assets/BGgameFYC.png")

            # Colores
            COLORS = {
                "ROJO": (165, 48, 48),
                "VERDE": (117, 167, 67),
                "AZUL": (79, 143, 186),
                "AMARILLO": (232, 193, 112),
                "MORADO": (64, 39, 81)
            }

            # Configuración del reloj
            clock = pygame.time.Clock()
            FPS = 60

            # Clase Figura
            class Figura:
                def __init__(self, x, y, color, tipo):
                    self.x = x
                    self.y = y
                    self.color = color
                    self.tipo = tipo
                    self.rect = pygame.Rect(x, y, 50, 50)

                def dibujar(self, pantalla):
                    if self.tipo == "CIRCULO":
                        pygame.draw.circle(pantalla, self.color, (self.x + 25, self.y + 25), 25)
                        pygame.draw.circle(pantalla, (0, 0, 0), (self.x + 25, self.y + 25), 25, 2)  # Contorno negro
                    elif self.tipo == "CUADRADO":
                        pygame.draw.rect(pantalla, self.color, self.rect)
                        pygame.draw.rect(pantalla, (0, 0, 0), self.rect, 2)  # Contorno negro
                    elif self.tipo == "TRIANGULO":
                        puntos = [(self.x + 25, self.y), (self.x, self.y + 50), (self.x + 50, self.y + 50)]
                        pygame.draw.polygon(pantalla, self.color, puntos)
                        pygame.draw.polygon(pantalla, (0, 0, 0), puntos, 2)  # Contorno negro
                    elif self.tipo == "RECTANGULO":
                        pygame.draw.rect(pantalla, self.color, (self.x, self.y, 60, 40))
                        pygame.draw.rect(pantalla, (0, 0, 0), (self.x, self.y, 60, 40), 2)  # Contorno negro
                    elif self.tipo == "ROMBO":
                        puntos = [(self.x + 25, self.y), (self.x, self.y + 25), (self.x + 25, self.y + 50), (self.x + 50, self.y + 25)]
                        pygame.draw.polygon(pantalla, self.color, puntos)
                        pygame.draw.polygon(pantalla, (0, 0, 0), puntos, 2)  # Contorno negro
                    elif self.tipo == "ESTRELLA":
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
                    elif self.tipo == "OVALO":
                        pygame.draw.ellipse(pantalla, self.color, (self.x, self.y, 60, 40))
                        pygame.draw.ellipse(pantalla, (0, 0, 0), (self.x, self.y, 60, 40), 2)  # Contorno negro
                    elif self.tipo == "PENTAGONO":
                        puntos = [
                            (self.x + 25, self.y),
                            (self.x + 50, self.y + 20),
                            (self.x + 40, self.y + 50),
                            (self.x + 10, self.y + 50),
                            (self.x, self.y + 20)
                        ]
                        pygame.draw.polygon(pantalla, self.color, puntos)
                        pygame.draw.polygon(pantalla, (0, 0, 0), puntos, 2)  # Contorno negro
                    elif self.tipo == "HEXAGONO":
                        puntos = [
                            (self.x + 25, self.y),
                            (self.x + 45, self.y + 15),
                            (self.x + 45, self.y + 35),
                            (self.x + 25, self.y + 50),
                            (self.x + 5, self.y + 35),
                            (self.x + 5, self.y + 15)
                        ]
                        pygame.draw.polygon(pantalla, self.color, puntos)
                        pygame.draw.polygon(pantalla, (0, 0, 0), puntos, 2)  # Contorno negro


                def clicado(self, pos):
                    if self.tipo == "CIRCULO":
                        distancia = ((self.x + 25 - pos[0]) ** 2 + (self.y + 25 - pos[1]) ** 2) ** 0.5
                        return distancia <= 25
                    elif self.tipo == "CUADRADO":
                        return self.rect.collidepoint(pos)
                    elif self.tipo == "TRIANGULO":
                        puntos = [(self.x + 25, self.y), (self.x, self.y + 50), (self.x + 50, self.y + 50)]
                        return pygame.draw.polygon(screen, (0, 0, 0), puntos, 2).collidepoint(pos)
                    elif self.tipo == "RECTANGULO":
                        return pygame.Rect(self.x, self.y, 60, 40).collidepoint(pos)
                    elif self.tipo == "ROMBO":
                        puntos = [(self.x + 25, self.y), (self.x, self.y + 25), (self.x + 25, self.y + 50), (self.x + 50, self.y + 25)]
                        return pygame.draw.polygon(screen, (0, 0, 0), puntos, 2).collidepoint(pos)
                    elif self.tipo == "ESTRELLA":
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
                    elif self.tipo == "OVALO":
                        return pygame.Rect(self.x, self.y, 60, 40).collidepoint(pos)
                    elif self.tipo == "PENTAGONO":
                        puntos = [
                            (self.x + 25, self.y),
                            (self.x + 50, self.y + 20),
                            (self.x + 40, self.y + 50),
                            (self.x + 10, self.y + 50),
                            (self.x, self.y + 20)
                        ]
                        return pygame.draw.polygon(screen, (0, 0, 0), puntos, 2).collidepoint(pos)
                    elif self.tipo == "HEXAGONO":
                        puntos = [
                            (self.x + 25, self.y),
                            (self.x + 45, self.y + 15),
                            (self.x + 45, self.y + 35),
                            (self.x + 25, self.y + 50),
                            (self.x + 5, self.y + 35),
                            (self.x + 5, self.y + 15)
                        ]
                        return pygame.draw.polygon(screen, (0, 0, 0), puntos, 2).collidepoint(pos)
            
            def game_over(puntaje):
                while True:
                    screen.blit(BGFigurasYColores, (0,0))
                    pos = pygame.mouse.get_pos()

                    contorno("GAME OVER", get_font(100), "red", "black", 640, 280)
                    contorno1(f"PUNTAJE: {puntaje}", get_font(60), "#75a743", "black", 640, 360)
                    contorno1("PRESS R TO RESET", get_font(40), "#e8c170", "black", 640, 420)
                    # Dibujar texto
                    contorno1(objetivo_texto, get_font(30), "#e8c170", "black", 380, 40)

                    # Dibujar temporizador
                    contorno1(f"TIEMPO RESTANTE: {int(tiempo_restante)} s", get_font(30), "#a53030","black", 380, 80)

                    CYF_exit = Spray(base_image=BotonExit, hover_image=BotonExitSpray, pos=(1220, 660))
                    CYF_exit.changeImage(pos)
                    CYF_exit.update(screen)  # Dibujar el botón

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.USEREVENT:  # Si termina una canción
                            avanzar_playlist(playlist)
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                CYF_tutorial_game()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if CYF_exit.checkForInput(pos):
                                CYF_tutorial()
                    
                    pygame.display.update()

            # Función principal del juego
            
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
                    tipo = random.choice(["CIRCULO", "CUADRADO", "TRIANGULO", "RECTANGULO", "ROMBO", "ESTRELLA", "OVALO", "PENTAGONO", "HEXAGONO"])
                    figuras.append(Figura(x, y, color, tipo))

                # Elegir figura objetivo
                objetivo = random.choice(figuras)
                nombre_color = [k for k, v in COLORS.items() if v == objetivo.color][0]

                # Identificar todas las figuras que coincidan con el objetivo
                figuras_objetivo = [figura for figura in figuras if figura.color == objetivo.color and figura.tipo == objetivo.tipo]

                objetivo_texto = f"HAZ CLIC EN UN {objetivo.tipo} DE COLOR {nombre_color}"

                # Temporizador
                tiempo_restante = tiempo_limite
                inicio_nivel = pygame.time.get_ticks()

                if puntaje == 10:
                    CYF_tutorial()

                # Ciclo del nivel
                while True:
                    screen.blit(BGFigurasYColores, (0,0))
                    pos = pygame.mouse.get_pos()

                    # Calcular tiempo restante
                    tiempo_actual = pygame.time.get_ticks()
                    tiempo_restante = tiempo_limite - (tiempo_actual - inicio_nivel) / 1000

                    if tiempo_restante <= 0:
                        game_over(puntaje)

                    # Dibujar texto
                    contorno1(objetivo_texto, get_font(30), "#e8c170", "black", 380, 40)

                    # Dibujar temporizador
                    contorno1(f"TIEMPO RESTANTE: {int(tiempo_restante)} s", get_font(30), "#a53030","black", 380, 80)

                    CYF_exit = Spray(base_image=BotonExit, hover_image=BotonExitSpray, pos=(1220, 660))
                    CYF_exit.changeImage(pos)
                    CYF_exit.update(screen)  # Dibujar el botón

                    # Dibujar figuras
                    for figura in figuras:
                        figura.dibujar(screen)

                    # Manejo de eventos
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if any(figura.clicado(pos) for figura in figuras_objetivo):
                                puntaje += 1
                                nivel += 1
                                tiempo_limite += 0.5  # Incrementar tiempo límite con cada acierto
                                break
                            else:
                                game_over(puntaje)
                            if CYF_exit.checkForInput(pos):
                                CYF_tutorial()

                        if event.type == pygame.USEREVENT:  # Si termina una canción
                            avanzar_playlist(playlist)

                    else:
                        # Actualizar pantalla
                        pygame.display.flip()
                        clock.tick(FPS)
                        continue
                    break

        while True:
            Tutorial_CYF_mouse_pos = pygame.mouse.get_pos()
            screen.blit(BGTutorialCYF, (0,0))
            contorno("TUTORIAL", get_font(100), "#75a743", "black", 640, 80)

            contorno1("¡Bienvenido al juego de colores y figuras! Tu ", get_font(40), "#e8c170", "black", 640, 150)
            contorno1("objetivo es seguir las indicaciones que aparecerán", get_font(40), "#e8c170", "black", 640, 200)
            contorno1("en pantalla, como: 'Selecciona el cuadrado rojo'.", get_font(40), "#e8c170", "black", 640, 250)
            contorno1("Observa las figuras y colores que se muestran, y ", get_font(40), "#e8c170", "black", 640, 300)
            contorno1("toca la opción correcta antes de que se acabe el", get_font(40), "#e8c170", "black", 640, 350)
            contorno1("tiempo. ¡Pon a prueba tu rapidez y atención!", get_font(40), "#e8c170", "black", 640, 400)

            contorno1("TUTORIAL", get_font(30), "#4f8fba", "black", 1005, 450)
            contorno1("BACK", get_font(30), "#a53030", "black", 270, 450)

            CYF_tuto_back = Spray(base_image=CakeSpray, hover_image=CakeSprayS, pos=(270, 525))
            CYF_tuto_back.changeImage(Tutorial_CYF_mouse_pos)
            CYF_tuto_back.update(screen)  # Dibujar el botón

            CYF_tuto_game = Spray(base_image=CakeSpray, hover_image=CakeSprayS, pos=(1005, 525))
            CYF_tuto_game.changeImage(Tutorial_CYF_mouse_pos)
            CYF_tuto_game.update(screen)  # Dibujar el botón

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if CYF_tuto_back.checkForInput(Tutorial_CYF_mouse_pos):
                        menu_colores_y_figuras()
                    if CYF_tuto_game.checkForInput(Tutorial_CYF_mouse_pos):
                        CYF_tutorial_game()
                if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)

            pygame.display.update()
    
    def CYF_scoreV():
        pygame.display.set_caption("Score Colores Y Figuras")
        loading_bar = LoadingBar(screen, BGLoadingCYF, start_color=(232, 193, 112), end_color=(165, 48, 48), text_color="#4f8fba", loading_time=1.5, segments=10)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)

            # Dibujar la barra de carga
            if loading_bar.draw():  # Si la barra de carga está llena
                break  # Detener el bucle principal cuando la barra esté llena

            # Esperar un poco para que el evento de carga se vea
            pygame.time.wait(100)
        
        def load_scores():
            try:
                with open("Top_scores_CYF.json", "r") as file:
                    return json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                # Si no hay archivo o está corrupto, usar una lista predeterminada
                return [{"name": "---", "score": 0} for _ in range(5)]

        # Cargar los puntajes
        top_scores = load_scores()

        while True:
            Score_CYF_mouse_pos = pygame.mouse.get_pos()
            screen.blit(BGScoreCYF, (0, 0))

            # Título de la pantalla de puntajes
            contorno("TOP SCORES", get_font(100), "#4f8fba", "black", 640, 100)
            contorno("RANK", get_font(80), "#e8c170", "black", 380, 220)
            contorno("NAME", get_font(80), "#75a743", "black", 640, 220)
            contorno("SCORE", get_font(80), "#a53030", "black", 900, 220)

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

            contorno1("BACK", get_font(40), "#a53030", "black", 170, 450)
            
            CYF_back = Spray(base_image=CakeSpray, hover_image=CakeSprayS, pos=(170, 535))
            CYF_back.changeImage(Score_CYF_mouse_pos)
            CYF_back.update(screen)  # Dibujar el botón

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if CYF_back.checkForInput(Score_CYF_mouse_pos):
                        menu_colores_y_figuras()
                if event.type == pygame.USEREVENT:  # Si termina una canción
                    avanzar_playlist(playlist)

            pygame.display.update()

    while True:
        screen.blit(BGMenuCYF, [0, 0])

        CYF_mouse_pos = pygame.mouse.get_pos()

        contorno("COLORES Y FIGURAS", get_font(100), "#444774", "black", 640, 110)
        contorno1("BACK", get_font(40), "#a53030", "black", 270, 440)
        contorno1("PLAY", get_font(40), "#e8c170", "black", 270, 205)
        contorno1("TUTORIAL", get_font(40), "#75a743", "black", 1005, 205)
        contorno1("SCORE", get_font(40), "#4f8fba", "black", 1005, 440)

        CYF_back = Spray(base_image=CakeSpray, hover_image=CakeSprayS, pos=(270, 525))
        CYF_back.changeImage(CYF_mouse_pos)
        CYF_back.update(screen)  # Dibujar el botón

        CYF_play = Spray(base_image=CakeSpray, hover_image=CakeSprayS, pos=(270, 290))
        CYF_play.changeImage(CYF_mouse_pos)
        CYF_play.update(screen)  # Dibujar el botón

        CYF_tutorialB = Spray(base_image=CakeSpray, hover_image=CakeSprayS, pos=(1005, 290))
        CYF_tutorialB.changeImage(CYF_mouse_pos)
        CYF_tutorialB.update(screen)  # Dibujar el botón

        CYF_score = Spray(base_image=CakeSpray, hover_image=CakeSprayS, pos=(1005, 525))
        CYF_score.changeImage(CYF_mouse_pos)
        CYF_score.update(screen)  # Dibujar el botón

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CYF_back.checkForInput(CYF_mouse_pos):
                    games()
                if CYF_play.checkForInput(CYF_mouse_pos):
                    CYF_game()
                if CYF_tutorialB.checkForInput(CYF_mouse_pos):
                    CYF_tutorial()
                if CYF_score.checkForInput(CYF_mouse_pos):
                    CYF_scoreV()
            if event.type == pygame.USEREVENT:  # Si termina una canción
                avanzar_playlist(playlist)

        pygame.display.update()

def main_menu():
    pygame.display.set_caption("Menú")
    loading_bar = LoadingBar(screen, FondoMain, start_color=(255, 212, 163), end_color=(208, 129, 89), text_color="#d08159", loading_time=1.5, segments=10)

    sounds_loadingbars[0].play(loops=0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:  # Si termina una canción
                avanzar_playlist(playlist)

        # Dibujar la barra de carga
        if loading_bar.draw():  # Si la barra de carga está llena
            break  # Detener el bucle principal cuando la barra esté llena

        pygame.time.wait(100)

    while True:
        screen.blit(FondoMain, [0, 0])
        screen.blit(Biomind, (1200, 640))
        Brain_rect = Brain.get_rect(center=(640, 70))
        screen.blit(Brain, Brain_rect)

        Menu_mouse_pos = pygame.mouse.get_pos()

        contorno("MINDBOOST", get_font(100), "#d08159", "black", 640, 170)

        Games_button = Button(image=pygame.image.load("assets/MainButton.png"), pos=(640, 300), 
                            text_input="GAMES", font=get_font(75), base_color="#000000", hovering_color="White")
        About_button = Button(image=pygame.image.load("assets/MainButton.png"), pos=(640, 450), 
                            text_input="ABOUT", font=get_font(75), base_color="#000000", hovering_color="White")
        Back_button = Button(image=pygame.image.load("assets/MainButton.png"), pos=(640, 600), 
                            text_input="BACK", font=get_font(75), base_color="#000000", hovering_color="White")

        for button in [Games_button, Back_button, About_button]:
            button.changeColor(Menu_mouse_pos)
            button.update(screen)

        Volumen_boton = Spray(base_image=BotonVolumen, hover_image=BotonVolumenS, pos=(80, 640))
        Volumen_boton.changeImage(Menu_mouse_pos)
        Volumen_boton.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Games_button.checkForInput(Menu_mouse_pos):
                        games()
                if About_button.checkForInput(Menu_mouse_pos):
                    about()
                if Back_button.checkForInput(Menu_mouse_pos):
                    get_player_name()
                if Volumen_boton.checkForInput(Menu_mouse_pos):
                    volumen()
            if event.type == pygame.USEREVENT:  # Si termina una canción
                avanzar_playlist(playlist)

        pygame.display.update()

def get_player_name():
    global player_name  # Declarar que se va a modificar la variable global
    pygame.display.set_caption("Menú")
    name = player_name  # Usar el valor actual como base para modificar
    loading_bar = LoadingBar(screen, FondoMain, start_color=(255, 212, 163), end_color=(208, 129, 89), text_color="#d08159", loading_time=1.5, segments=10)

    sounds_loadingbars[0].play(loops=0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:  # Si termina una canción
                avanzar_playlist(playlist)

        # Dibujar la barra de carga
        if loading_bar.draw():  # Si la barra de carga está llena
            break  # Detener el bucle principal cuando la barra esté llena

        pygame.time.wait(100)

    while True:
        screen.blit(FondoMain, (0, 0))
        screen.blit(Biomind, (1200, 640))
        Brain_rect = Brain.get_rect(center=(640, 70))
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
                    player_name = name  # Actualizar la variable global
                    print(f"Player name: {player_name}")
                    main_menu()
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]  # Eliminar el último carácter
                if len(name) < 3 and event.unicode.isalnum():
                    name += event.unicode.upper()  # Agregar la letra en mayúsculas
            if event.type == pygame.USEREVENT:  # Si termina una canción
                avanzar_playlist(playlist)

# Comenzar con el flujo
get_player_name()