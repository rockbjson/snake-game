import random

from init import *

from pygame import Vector2

# sound effects
point_gained_sound = mixer.Sound('audio/gameboy-pluck.mp3')
life_lost_sound = mixer.Sound('audio/death-sound.mp3')


class Characters():
    def __init__(self):
        # initialize mouse attributes
        self.mouse_x = random.randint(0, cell_number - 1)
        self.mouse_y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.mouse_x, self.mouse_y)  # storing x and y position in a 2D vector
        self.image = pygame.image.load('graphics/mouse.png').convert_alpha()
        self.image_resized = pygame.transform.scale(self.image, (cell_size, cell_size))

        # initialize snake attributes
        self.snake_x, self.snake_y = 250, 250
        self.new_x, self.new_y = 25, 0
        self.head_direction = "graphics/head_right.png"
        self.snake_body = [(self.snake_x, self.snake_y)]

        # points system
        self.points = 0

    # snake movement
    def display_character(self, image):

        # update snake attributes
        self.snake_x = self.snake_x + self.new_x
        self.snake_y = self.snake_y + self.new_y

        if (self.check_snake_bounds() is True):
            flag = False
        else:
            flag = True

        self.snake_x = self.snake_x % 500
        self.snake_y = self.snake_y % 500

        self.snake_body.append((self.snake_x, self.snake_y))

        self.check_mouse_collision()

        head_image = pygame.image.load(image).convert_alpha()

        screen.blit(background, (0, 0))
        self.draw_mouse()
        self.draw_snake(image, head_image)

        return flag

    # checks to see if the snake collides with itself or with walls
    def check_snake_bounds(self):
        flag = False

        if (self.snake_body[0] in self.snake_body[1:]):
            flag = True
        else:
            flag = False

        if self.snake_x < 0 or self.snake_x >= 500 or self.snake_y < 0 or self.snake_y >= 500:
            print(self.snake_x, self.snake_y)
            life_lost_sound.play()
            flag = True
            return flag

        return flag

    # find snake direction from key event
    def find_snake_direction(self, event):

        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
                if (self.new_x != 25):
                    self.new_x = -25
                    self.head_direction = "graphics/head_left.png"
                self.new_y = 0
            elif (event.key == pygame.K_RIGHT):
                if (self.new_x != -25):
                    self.new_x = 25
                    self.head_direction = "graphics/head_right.png"
                self.new_y = 0
            elif (event.key == pygame.K_UP):
                if (self.new_y != 25):
                    self.new_y = -25
                    self.head_direction = "graphics/head_up.png"
                self.new_x = 0
            elif (event.key == pygame.K_DOWN):
                if (self.new_y != -25):
                    self.new_y = 25
                    self.head_direction = "graphics/head_down.png"
                self.new_x = 0

        return self.head_direction

    # checks for snake and mouse collision and updates mouse coordinates if true
    def check_mouse_collision(self):
        if self.mouse_x == int(self.snake_x / cell_size) and self.mouse_y == int(self.snake_y / cell_size):
            while (self.mouse_x * cell_size, self.mouse_y * cell_size) in self.snake_body:
                self.update_mouse_location()
                # update points and play sound
                self.points += 1
                point_gained_sound.play()
        else:
            del self.snake_body[0]

    def draw_snake(self, image, head_image):
        for (i, j) in self.snake_body:
            if self.snake_body[len(self.snake_body) - 1] == (i, j):
                screen.blit(head_image, (i, j))
            elif (image == 'graphics/head_right.png' or image == 'graphics/head_left.png'):
                if (self.snake_body[0] == (i, j)) and (len(self.snake_body) > 1):
                    if (image == 'graphics/head_right.png'):
                        tail_image = pygame.image.load("graphics/tail_right.png").convert_alpha()
                    else:
                        tail_image = pygame.image.load("graphics/tail_left.png").convert_alpha()
                    screen.blit(tail_image, (i, j))
                else:
                    body_image = pygame.image.load("graphics/body_hor.png").convert_alpha()
                    screen.blit(body_image, (i, j))
            elif (image == 'graphics/head_up.png' or image == 'graphics/head_down.png'):
                if (self.snake_body[0] == (i, j)) and (len(self.snake_body) > 1):
                    if (image == 'graphics/head_up.png'):
                        tail_image = pygame.image.load("graphics/tail_up.png").convert_alpha()
                    else:
                        tail_image = pygame.image.load("graphics/tail_down.png").convert_alpha()
                    screen.blit(tail_image, (i, j))
                else:
                    body_image = pygame.image.load("graphics/body_vert.png").convert_alpha()
                    screen.blit(body_image, (i, j))

    def draw_mouse(self):
        mouse_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        screen.blit(self.image_resized, mouse_rect)

    def get_mouse_location(self):
        return self.mouse_x, self.mouse_y

    def update_mouse_location(self):
        self.mouse_x = random.randint(0, cell_number - 1)
        self.mouse_y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.mouse_x, self.mouse_y)  # storing x and y position in a 2D vector
        self.image = pygame.image.load('graphics/mouse.png').convert_alpha()
        self.image_resized = pygame.transform.scale(self.image, (cell_size, cell_size))

