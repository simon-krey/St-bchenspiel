import pygame as pg
pg.init()
pg.font.init()

import os
import random

from scrpts.ui import Button
from scrpts.utils import rendered_text
from scrpts.game import Game

SCREEN_SIZE = (1080, 720)
BASE_PATH = os.path.abspath(os.path.dirname(__file__))

def main():
    pg.display.set_caption("Streichholtz Spiel")
    screen = pg.display.set_mode(SCREEN_SIZE, vsync=1)

    strechholtz_image = pg.image.load(BASE_PATH + "/assets/streichholtz.png")

    # variables to select before the game starts
    turn = random.randint(0, 1)
    max_count = 20
    min_count = 10

    # to select while in game
    to_withdraw = 1

    current_scene = "menu"
    # ui elements for menu
    turn_button = Button((380, 100), "Flip Turns")

    min_count_sub_btn = Button((150, 215), "-", padding=1)
    min_count_add_btn = Button((170, 215), "+", padding=1)

    max_count_sub_btn = Button((230, 215), "-", padding=1)
    max_count_add_btn = Button((250, 215), "+", padding=1)

    start_button = Button((100, 275), "Start Game")

    # game
    game: Game

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

            new_min_count = min_count
            new_max_count = max_count

            other_min_max = False

            if min_count_sub_btn.update(pg.mouse.get_pos(), mouse_pressed):
                new_min_count -= 1

            if min_count_add_btn.update(pg.mouse.get_pos(), mouse_pressed):
                if new_min_count == max_count:
                    max_count += 1
                    min_count += 1

                    other_min_max = True

                else:
                    new_min_count += 1

            if max_count_sub_btn.update(pg.mouse.get_pos(), mouse_pressed):
                if new_max_count == min_count:
                    min_count -= 1
                    max_count -= 1

                    other_min_max = True

                else:  
                    new_max_count -= 1

            if max_count_add_btn.update(pg.mouse.get_pos(), mouse_pressed):
                new_max_count += 1

            if not other_min_max:
                new_min_count = min(max(new_min_count, 10), min(30, max_count))
                new_max_count = min(max(new_max_count, max(13, min_count)), 50)

                min_count = new_min_count
                max_count = new_max_count

            else:
                min_count = min(max(min_count, 10), 30)
                max_count = min(max(max_count, 13), 50)

            if start_button.update(pg.mouse.get_pos(), mouse_pressed):
                game = Game(min_count, max_count, turn)

                current_scene = "game"

            screen.blit(rendered_text("Settings", size=30), [100, 30])

            screen.blit(rendered_text("Select who should start: "), [100, 100])
            turn_button.render(screen)

            if turn:
                screen.blit(rendered_text("You're starting"), [100, 130])

            else:
                screen.blit(rendered_text("The PC is starting"), [100, 130])

            screen.blit(rendered_text(f"How much rods should exist: {min_count} - {max_count}"), [100, 190])
            
            min_count_sub_btn.render(screen)
            min_count_add_btn.render(screen)

            max_count_sub_btn.render(screen)
            max_count_add_btn.render(screen)

            start_button.render(screen)

        if current_scene == "game":
            pass

        pg.display.flip()
        
if __name__ == "__main__":
    main()
