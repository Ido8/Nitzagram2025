from classes.Post import *
from constants import *

class Comment:
    def __init__(self, comment):
        self.comment = comment

    def display(self, i):
        y = FIRST_COMMENT_Y_POS + (i * COMMENT_TEXT_SIZE)
        print_text(self.comment, COMMENT_TEXT_SIZE, FIRST_COMMENT_X_POS, y, BLACK, FONT_NAME)

