import pygame
import random
import math

pygame.init()

FPS = 60  # Frame Per Second

WIDTH, HEIGHT = 800, 800
ROWS = 4
COLS = 4

RECT_WIDTH = WIDTH // ROWS
RECT_HEIGHT = HEIGHT // COLS

OUTLINE_COLOR = (167, 167, 167)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (215, 215, 215)
FONT_COLOR = (51, 51, 51)

FONT = pygame.font.SysFont("comicsans", 60, bold=True)
MOVE_VEL = 20

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

def draw_grid(window):
    """
    Draw grid on the screen of the game
    :param window:
    :return: a grid on the screen
    """
    # Draws the small grids or rectangles
    # Draws the horizontal lines
    for row in range(1, ROWS):
        y = row * RECT_WIDTH  # y coordinate moves row by row
        pygame.draw.line(window, OUTLINE_COLOR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)

    # Draws the vertical lines
    for col in range(1, COLS):
        x = col * RECT_WIDTH  # x coordinate moves column by column
        pygame.draw.line(window, OUTLINE_COLOR, (x, 0), (x, HEIGHT), OUTLINE_THICKNESS)

    # Draw the rectangle outline at the borders of the app
    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICKNESS)


def draw(window):
    """
    Draw the game
    :param window:
    :return:
    """

    # Window background
    window.fill(BACKGROUND_COLOR)

    # Draws the grid from the draw_grid function
    draw_grid(window)

    # Display the drawings
    pygame.display.update()

def main(window):
    """
    Main function of the application
    :param window:
    :return:
    """

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window)


    pygame.quit()


if __name__ == "__main__":
    main(WINDOW)

