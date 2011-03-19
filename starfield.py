#!/usr/bin/env python

"""starfield, by Jon Parise <jon@csh.rit.edu>

Simple program to display a moving parallax starfield.

The speed of the starfield can be altered using the up and down arrows.
The direction of the starfield can be changed using the left and right arrows.

The algorithm is based on code by Sean Bugel <bugelsea@rcn.com>.
"""

import random
import pygame
from pygame.locals import *

# Constants
NUM_STARS = 40
SCREEN_SIZE = [640, 480]
WHITE = 255, 255, 255
BLACK = 20, 20, 40
LIGHTGRAY = 180, 180, 180
DARKGRAY = 120, 120, 120
LEFT = 0
RIGHT = 1

def initStars(screen):
    "Create the starfield"

    # The starfield is represented as a dictionary of x and y values.
    stars = []

    # Create a list of (x,y) coordinates.
    for loop in range(0, NUM_STARS):
        star = [random.randrange(0, screen.get_width() - 1),
                random.randrange(0, screen.get_height() - 1)]
        stars.append(star);

    return stars

def moveStars(screen, stars, start, end, direction):
    "Correct for stars hitting the screen's borders"

    for loop in range(start, end):
        if (direction == LEFT):
            if (stars[loop][0] <> 1):
                stars[loop][0] = stars[loop][0] - 1
            else:
                stars[loop][1] = random.randrange(0, screen.get_height() - 1)
                stars[loop][0] = screen.get_width() - 1
        elif (direction == RIGHT):
            if (stars[loop][0] <> screen.get_width() - 1):
                stars[loop][0] = stars[loop][0] + 1
            else:
                stars[loop][1] = random.randrange(0, screen.get_height() - 1)
                stars[loop][0] = 1

    return stars

def main():
    "Main starfield code"

    random.seed()

    # Initialize the pygame library.
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN)
    pygame.display.set_caption("Starfield")
    pygame.mouse.set_visible(0)

    # Set the background to black.
    screen.fill(BLACK)

    # Simulation variables.
    delay = 8
    inc = 2
    direction = LEFT

    # Create the starfield.
    stars = initStars(screen)

    # Place ten white stars
    for loop in range(0, 10):
        screen.set_at(stars[loop], WHITE)

    # Main loop
    while 1:

        # Handle input events.
        event = pygame.event.poll()
        if (event.type == QUIT):
            break
        elif (event.type == KEYDOWN):
            if (event.key == K_ESCAPE):
                break
            elif (event.key == K_UP):
                if (delay >= 2): delay = delay - 1
            elif (event.key == K_DOWN):
                if (delay <= 16): delay = delay + 1
            elif (event.key == K_LEFT):
                direction = LEFT
            elif (event.key == K_RIGHT):
                direction = RIGHT 

        # Used to slow down the second and third field.
        inc = inc + 1

        # Erase the first star field.
        for loop in range(0, 10):
            screen.set_at(stars[loop], BLACK)

        # Check if first field's stars hit the screen border.
        stars = moveStars(screen, stars, 0, 10, direction)

        # Second star field algorythms.
        if (inc % 2 == 0):

            # Erase the second field.
            for loop in range(11, 20):
                screen.set_at(stars[loop], BLACK)

            # Checks to see if the second field's stars hit the screen border.
            stars = moveStars(screen, stars, 11, 20, direction)

            # Place ten light gray stars.
            for loop in range(11, 20):
                screen.set_at(stars[loop], LIGHTGRAY)

        # Third star field algorythms.
        if (inc % 5 == 0):
            
            # Erase the third field.
            for loop in range(21, NUM_STARS):
                screen.set_at(stars[loop], BLACK)

            # Checks to see if the third field's stars hit the screen border.
            stars = moveStars(screen, stars, 21, NUM_STARS, direction)

            # Place ten dark gray stars.
            for loop in range(21, NUM_STARS):
                screen.set_at(stars[loop], DARKGRAY)

        # Place ten white stars.
        for loop in range(0, 10):
            screen.set_at(stars[loop], WHITE)

        # Control the starfield speed.
        pygame.time.delay(delay)

        # Make sure this variable doesn't get too large.
        if (inc == 500): inc = 2

        # Update the screen.
        pygame.display.update()

# Start the program.
if __name__ == '__main__': main()
