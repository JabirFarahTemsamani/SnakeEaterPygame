# menu.py
import pygame
import sys

pygame.font.init()
# Colors
font = pygame.font.SysFont('comic sans', 30)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)  # crea rectangle de text 
    surface.blit(text_surface, (x, y))             # posa el rectangle de text on toca 

def show_menu():
    """Muestra el menú inicial."""
    frame_size_x, frame_size_y = 720, 480
    difficulty = 25           # Predeterminada
    size_option = (720, 480)  # Predeterminada

    menu_window = pygame.display.set_mode((frame_size_x, frame_size_y))
    pygame.display.set_caption("Snake Eater - Menu")
    
    clock = pygame.time.Clock()
    running = True
    selected_difficulty = "Medium"  # Predeterminada
    selected_size = "720x480"       # Predeterminada

    while running:
        menu_window.fill(black)
        
        draw_text(menu_window, "Snake Eater - Menu", font, white, 250, 50)
        draw_text(menu_window, "Select Difficulty:", font, blue, 100, 100)
        draw_text(menu_window, "1:  Easy", font, green if selected_difficulty == "Easy" else white, 100, 140)
        draw_text(menu_window, "2:  Medium", font, green if selected_difficulty == "Medium" else white, 100, 180)
        draw_text(menu_window, "3:  Hard", font, green if selected_difficulty == "Hard" else white, 100, 220)
        
        draw_text(menu_window, "Select Window Size:", font, blue, 100, 280)
        draw_text(menu_window, "A:  720x480", font, green if selected_size == "720x480" else white, 100, 320)
        draw_text(menu_window, "B:  1080x720", font, green if selected_size == "1080x720" else white, 100, 360)

        draw_text(menu_window, "Press Enter to Start", font, white, 250, 400)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = 10
                    selected_difficulty = "Easy"
                if event.key == pygame.K_2:
                    difficulty = 25
                    selected_difficulty = "Medium"
                if event.key == pygame.K_3:
                    difficulty = 40
                    selected_difficulty = "Hard"
                if event.key == pygame.K_a:
                    size_option = (720, 480)
                    selected_size = "720x480"
                if event.key == pygame.K_b:
                    size_option = (1080, 720)
                    selected_size = "1080x720"
                if event.key == pygame.K_RETURN: # al presionar enter sortim
                    running = False 

        pygame.display.update()
        clock.tick(30)

    return difficulty, size_option # retorna la tria del usuari
