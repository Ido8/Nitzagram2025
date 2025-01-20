from classes.Post import *
from buttons import *
from constants import *
from helpers import *


class PostImage(Post):
    def __init__(self, username, location, description, likes_couter, comments, image):
        super().__init__(username, location, description, likes_couter, comments)
        img = pygame.image.load(image)
        self.img = pygame.transform.scale(img, (POST_WIDTH, POST_HEIGHT))

    def display(self):
        super().display()
        screen.blit(self.img, (POST_X_POS, POST_Y_POS))
