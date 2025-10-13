import pygame as pg
pg.init()
pg.font.init()

import os
import random

from scrpts.ui import Button
from scrpts.utils import rendered_text

SCREEN_SIZE = (1080, 720)
BASE_PATH = os.path.abspath(os.path.dirname(__file__))

def main():
    pg.display.set_caption("Streichholtz Spiel")
    screen = pg.display.set_mode(SCREEN_SIZE, vsync=1)

    strechholtz_image = pg.image.load(BASE_PATH + "/assets/streichholtz.png")

    # variables to select before the game starts
    turn = 0
    total_count = random.randint(10, 20)

    # to select while in game
    to_withdraw = 1

    current_scene = "menu"
    # ui elements for menu
    turn_button = Button((380, 100), "Flip Turns")

    mouse_pressed = False

    running = True
    while running:
        mouse_pressed = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.MOUSEBUTTONUP:
                if event.button == pg.BUTTON_LEFT:
                    mouse_pressed = True

        screen.fill(pg.Color(225, 240, 225))

        if current_scene == "menu":
            if turn_button.update(pg.mouse.get_pos(), mouse_pressed):
                turn = not turn

            screen.blit(rendered_text("Settings", size=30), [100, 30])

            screen.blit(rendered_text("Select who should start: "), [100, 100])
            turn_button.render(screen)

            if turn:
                screen.blit(rendered_text("You're starting"), [100, 130])

            else:
                screen.blit(rendered_text("The PC is starting"), [100, 130])

        if current_scene == "game":
            pass

        pg.display.flip()
        
if __name__ == "__main__":
    main()
