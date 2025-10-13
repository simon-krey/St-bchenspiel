import pygame as pg
pg.init()
pg.font.init()

import os
import random

from scrpts.ui import Button

SCREEN_SIZE = (1080, 720)
BASE_PATH = os.path.abspath(os.path.dirname(__file__))

def main():
    pg.display.set_caption("Streichholtz Spiel")
    screen = pg.display.set_mode(SCREEN_SIZE, vsync=1)

    b = Button((100, 200), "Test")

    strechholtz_image = pg.image.load(BASE_PATH + "/assets/streichholtz.png")

    # variables to select before the game starts
    turn = 0
    total_count = random.randint(10, 20)

    # to select while in game
    to_withdraw = 1

    font = pg.font.Font(pg.font.get_default_font(), size=20)

    current_scene = "menu"

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        b.update(pg.mouse.get_pos(), )

        screen.fill(pg.Color(225, 240, 225))

        if current_scene == "menu":
            screen.blit(font.render("Please Select the count of total rods: ", True, pg.Color(0, 0, 0)), [100, 100])
            b.render(screen)

        if current_scene == "game":
            pass

        pg.display.flip()
        
if __name__ == "__main__":
    main()
