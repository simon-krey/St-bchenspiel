import pygame as pg
import random

from scrpts.utils import cubic, rendered_text
import constants as c

stäbeLeft = 0

def game(StäbeNehmen, startingStäbe=None, startingPlayer=None):

    global stäbeLeft
    if startingStäbe:
        stäbeLeft=startingStäbe
    print(f"Stäbe: {stäbeLeft}")

    def chooseAlgorithm(stäbeLeft):
        StäbeNehmen = (stäbeLeft-1)%4

        print(StäbeNehmen)
        return StäbeNehmen
    
    if(startingPlayer):
        chooseAlgorithm(stäbeLeft)
        
    StäbeNehmen

class RodAnimation:
    def __init__(self, image, x, duration=0.6, max_y=c.SCREEN_SIZE[1]):
        self.finished = False

        self.duration = duration
        self.counter = self.duration

        self.value = 0
        self.image = image
    
        self.x = x
        self.max_y = max_y

    def update(self, delta_time):
        if not self.finished:
            self.counter -= delta_time

            self.value = cubic(0, self.duration, self.duration - self.counter) / self.duration

            if self.counter <= 0:
                self.finished = True

    def render(self, screen):
        if not self.finished:
            screen.blit(self.image, (self.x, self.max_y * self.value + 100))

class Game:
    def __init__(self, min_count, max_count, starting_turn):
        # starting turn = 1 means the player gets the first turn
        self.rods = random.randint(min_count, max_count)
        self.turn = starting_turn

        self.streichholz_image = pg.Surface.convert_alpha(pg.image.load(c.BASE_PATH + "/assets/streichholtz.png"))
        self.streichholz_image = pg.transform.scale(self.streichholz_image, [int(x * 0.25) for x in self.streichholz_image.get_size()])
        self.streichholz_pos_x = int(c.SCREEN_SIZE[0] / 2 - self.streichholz_image.get_size()[0] / 2)

        self.won = False
        self.winner = None

        self.animations: list[RodAnimation] = []

        self.user_pulled = 0

        self.pc_animations_left = 0
        self.pc_pull_delay = 0.5
        self.pc_pull_counter = 0

    def check_win(self):
        if self.rods <= 0:
            return True, not self.turn
        
        return False, 0

    def pc_turn(self, algorythmus="random"):
        withdraw_count: int

        if algorythmus == "modulo":
            withdraw_count = (self.rods - 1) % 4

        elif algorythmus == "random":
            withdraw_count = random.randint(1, 3)
            withdraw_count = min(withdraw_count, self.rods)

        withdraw_count = min(max(withdraw_count, 1), 3)

        self.pc_animations_left = withdraw_count
        self.pc_pull_counter = self.pc_pull_delay

        self.rods -= withdraw_count

    def user_turn(self, count):
        self.rods -= count
        self.turn = not self.turn

    def update(self, delta_time):
        if self.turn == 0 and not self.pc_animations_left > 0:
            self.pc_turn()

        finished = []
        for i, anim in enumerate(self.animations):
            anim.update(delta_time)

        finished.reverse()

        for i in finished:
            self.animations.pop(i)

        if self.pc_animations_left > 0:
            self.pc_pull_counter -= delta_time

            if self.pc_pull_counter <= 0:
                self.pc_pull_counter = self.pc_pull_delay
                self.pc_animations_left -= 1
                self._start_animation()

                won, turn = self.check_win()
                if won:
                    self.winner = turn
                    self.won = True

                if self.pc_animations_left == 0 and self.turn == 0:
                    self.turn = not self.turn

    def render(self, screen: pg.Surface):
        screen.blit(rendered_text(f"Rods left: {self.rods}"), [5, 5])
        screen.blit(rendered_text(f"Turn: {"user" if self.turn else "pc"}"), [5, 25])

        if True:
            if not self.won:
                screen.blit(self.streichholz_image, [self.streichholz_pos_x, 100])

            else:
                screen.blit(rendered_text(f"{"user" if self.winner else "pc"} won!"), [5, 45])

            for anim in self.animations:
                anim.render(screen)

    def _start_animation(self):
        self.animations.append(RodAnimation(self.streichholz_image, self.streichholz_pos_x))

    def pull_one(self, done_pulling):
        if not self.won and self.turn == 1:
            if done_pulling or self.user_pulled >= 3:
                if self.user_pulled > 0:
                    self.turn = not self.turn
                    self.user_pulled = 0

            else:
                self.user_pulled += 1
                self.rods -= 1
                self._start_animation()

                if self.user_pulled >= 3:
                    self.turn = not self.turn
                    self.user_pulled = 0
