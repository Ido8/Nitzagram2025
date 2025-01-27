import pygame
from helpers import screen
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from classes.PostImage import *
from classes.PostText import *
from helpers import *
from buttons import *
from classes.Post import *




def main():
    posts = []
    i = 0
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    # TODO: add a post here
    text = PostText('shalom', 'yeshiva tichonit', 'shalom from yeshiva tichonit', 0, [], 'shalom from the tzadicim', BLACK, (255, 255, 255))
    image_ronaldo = PostImage('shalom', 'yehsiva', 'ye', 0, [], "Images/ronaldo.jpg")
    image = PostImage('shalom', 'yehsiva', 'ye', 0, [], "Images/noa_kirel.jpg")
    posts.append(text)
    posts.append(image)
    posts.append(image_ronaldo)



    running = True
    while running:
        i = i % len(posts)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_in_button(like_button,mouse_pos):
                    posts[i].add_like()
                if mouse_in_button(comment_button,mouse_pos):
                    posts[i].add_comment(read_comment_from_user())
                if mouse_in_button(click_post_button,mouse_pos):
                    i += 1
                    i = i % len(posts)
                if mouse_in_button(view_more_comments_button,mouse_pos):
                    pass





        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        posts[i].display()
        # Update display - without input update everything
        pygame.display.update()
        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
