import sys
from characters import *
from init import *

pygame.init()

clock = pygame.time.Clock()

# setting the snake icon
icon = pygame.image.load('graphics/icon.png')
pygame.display.set_icon(icon)
screen.fill((50,168,52))

# loading and getting rectangle for the snake image
snake_image = pygame.image.load('graphics/snake.png').convert_alpha()
snake_rect = snake_image.get_rect()
snake_rect.center = (250, 250)

# function to create font
def render_text(font, text, color, pos):
    rendered_text = font.render(text, False, color)
    text_rect = rendered_text.get_rect()
    text_rect.center = pos
    return rendered_text, text_rect

# start screen constants
font = 'font/DisposableDroidBB.ttf'
white = (255, 255, 255)
dark_green = (21, 71, 52)

# adding start screen font
title_font = pygame.font.Font(font, 80)
title_text, title_rect = render_text(title_font, "PYTHON", white, (255, 140))
title_text_bg, title_bg_rect = render_text(title_font, "PYTHON", dark_green, (258, 143))
start_font = pygame.font.Font(font, 24)
start_text, start_rect = render_text(start_font, "Press any key to start", dark_green, (255, 410))

# font for the points system
points_font = pygame.font.Font(font, 30)
points_outline_font = pygame.font.Font(font, 30)

# create characters object
characters = Characters()

def display_lives_status():
    heart_full = pygame.image.load("graphics/heart_full.png").convert_alpha()
    heart_empty = pygame.image.load("graphics/heart_empty.png").convert_alpha()

    if (lives == 0):
        screen.blit(heart_full, (400, 15))
        screen.blit(heart_full, (430, 15))
        screen.blit(heart_full, (460, 15))
    elif(lives == 1):
        screen.blit(heart_full, (400, 15))
        screen.blit(heart_full, (430, 15))
        screen.blit(heart_empty, (460, 15))
    elif (lives == 2):
        screen.blit(heart_full, (400, 15))
        screen.blit(heart_empty, (430, 15))
        screen.blit(heart_empty, (460, 15))
    elif (lives == 3):
        screen.blit(heart_empty, (400, 15))
        screen.blit(heart_empty, (430, 15))
        screen.blit(heart_empty, (460, 15))
    else:
        display_game_over()

def display_points():
    # update points text and rectangle
    points_text, points_rect = render_text(
        points_font, f"Points: {characters.points}", white, (62, 18))

    points_outline_text, points_outline_rect = render_text(
        points_outline_font, f"Points: {characters.points}", dark_green, (64, 20))

    # blit points text and rectangle
    screen.blit(points_outline_text, points_outline_rect)
    screen.blit(points_text, points_rect)

def display_start_screen():
    # display start screen
    screen.blit(background, (0, 0))
    screen.blit(snake_image, snake_rect)
    screen.blit(title_text_bg, title_bg_rect)
    screen.blit(title_text, title_rect)
    screen.blit(start_text, start_rect)

def display_game_over():
    # adding game over screen font
    game_over_font = pygame.font.Font(font, 80)
    game_over_text, game_over_rect = render_text(game_over_font, "GAME OVER.", white, (255, 250))
    game_over_text_bg, game_over_bg_rect = render_text(title_font, "GAME OVER.", dark_green, (258, 253))
    score_font = pygame.font.Font(font, 24)
    score_text, score_rect = render_text(score_font, f"Your score was: {characters.points}", dark_green, (255, 410))

    screen.blit(background, (0, 0))
    screen.blit(game_over_text_bg, game_over_bg_rect)
    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)

running = True
start_game = False

# displaying the start screen
display_start_screen()

# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            start_game = True

    if start_game:
        # start the game here
        screen.blit(background, (0,0))

        # get head direction from key event
        head_direction = characters.find_snake_direction(event)

        # display characters

        if (characters.display_character((head_direction)) is False):
            lives = lives + 1

        if (lives>3):
            start_game = False

        # display points
        display_points()

        display_lives_status()

    # set game speed
    clock.tick(14)

    pygame.display.flip()

pygame.quit()
sys.exit()

