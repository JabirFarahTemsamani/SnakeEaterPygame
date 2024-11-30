
import pygame, sys, time, random
from menu import show_menu

pygame.init()

"""Mostrar el menú inicial"""
difficulty, (frame_size_x, frame_size_y) = show_menu()

"""Audios que ens interesen"""
game_over_sound = pygame.mixer.Sound("game_over.wav")
eat_sound = pygame.mixer.Sound("eat.wav")

"""Inicialitzam finestra"""
pygame.display.set_caption('Snake Eater') # Nom de la finestra
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

"""Declaració de variables inicials"""
# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# FPS (frames per second) controller
fps_controller = pygame.time.Clock() # el joc s'actualizara  "fps_controller" cops per segon el programa s'executara

# Game variables
snake_pos = [100, 50] #pos inicial de la serp
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]] # 10 pixels per cada part del cos en horitzontal

food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10] # pos food
food_spawn = True # si hi ha menjar

direction = 'RIGHT' # direcció inicial
change_to = direction # direcció nova

score = 0 # puntuació inicial


"""Game over"""
def game_over():
    pygame.mixer.music.set_volume(0.5)
    game_over_sound.play()

    my_font = pygame.font.SysFont('comic sans', 90) 
    game_over_surface = my_font.render('GAME OVER', True, red) 
    game_over_rect = game_over_surface.get_rect() 
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4) 
    
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)  
    
    show_score(0, red, 'times', 20) 

    pygame.display.flip() 
    time.sleep(3) 
    pygame.quit()
    sys.exit(0)


"""Puntuació"""
# Score
def show_score(choice, color, font, size): 
    
    score_font = pygame.font.SysFont(font, size) 
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()

    if choice == 1:
        score_rect.midtop = (frame_size_x/10, 15) # a dalt a la esquerra
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25) # a baix al mig

    game_window.blit(score_surface, score_rect)


"""Joc"""
# Main logic
while True:

    for event in pygame.event.get(): # ens donda el últim event (presiona ratolí o tecla o x per sortir finestra)
        
        if event.type == pygame.QUIT: # si x (finestra) 
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN: #  cas en el que event es presionar una tecla

            if event.key == pygame.K_UP or event.key == ord('w'): # fletxa o w --> UP
                change_to = 'UP' # seguent posició                                  
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'

            if event.key == pygame.K_ESCAPE: # ESC 
                pygame.event.post(pygame.event.Event(pygame.QUIT)) # envia a la cadena de events un quit es un altre forma de fer-ho

    # Evitar direccions prohibides
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'                            
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moure la serp
    if direction == 'UP':
        snake_pos[1] -= 10 # nova pos del cap de la serp (canviem las coordenades) # coord Y #
    if direction == 'DOWN':
        snake_pos[1] += 10 
    if direction == 'LEFT':
        snake_pos[0] -= 10 # coord X #
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Actualitzan el body de la serp
    snake_body.insert(0, list(snake_pos)) # nova posició del cap
    
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]: # si coord cap == coord menjar
        eat_sound.play() 
        score += 1
        food_spawn = False
    else:
        snake_body.pop() # eliimina l'ultim elemet 

    # Ceem el nou menjar
    if not food_spawn:
        food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10] 
    food_spawn = True

    """Implementació gràfica"""
    game_window.fill(black)

    #Dibixar cos serp
    for pos in snake_body: # resorres las posiciones del cuerpo con cooredandes x i y
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10)) # dibuixem quadrats 10x10

    #Dibuixar menjar serp 
    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    """Condicions GAME OVER"""
    # Fora dels limits
    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10: # Coor x
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10: # Coord y
        game_over()

    # Xoc amb el cos de la serp
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:  # si alguna coord del cos coincideix amb el cap --> xoc
            game_over()

    #Actualitzar score
    show_score(1, white, 'consolas', 20) 
    
    #Mostrem per pantalla
    pygame.display.update()
    fps_controller.tick(difficulty) # Limita los FPS al jugo para que sea segun tu quieras