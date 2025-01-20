import pygame

from classes.Post import *
from helpers import *
from constants import *


class PostText(Post):
    def __init__(self, username, location, description, likes_couter, comments, text, text_color, background_color):
        super().__init__(username, location, description, likes_couter, comments)
        self.textarr = from_text_to_array(text)
        self.text_color = text_color
        self.background_color = background_color

    def display(self):
        super().display()
        square = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.background_color, square)
        n = len(self.textarr)
        for i in range(n):
            font = pygame.font.SysFont(FONT_NAME, TEXT_POST_FONT_SIZE)
            text = font.render(self.textarr[i], True, self.text_color)
            pos = center_text(n, text, i)
            screen.blit(text, pos)
