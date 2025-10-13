import random

from scrpts.utils import cubic

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

class Game:
    def __init__(self, min_count, max_count, starting_turn):
        # starting turn = 1 means the player gets the first turn
        self.rods = random.randint(min_count, max_count)
        self.turn = starting_turn

        self.animation = {
            "on_going" : False,
            "counter" : 0,
            "duration" : 1,
            "interpolated_value" : 0
        }

    def check_win(self):
        if self.rods <= 0:
            return True, self.turn
        
        return False, 0

    def pc_turn(self, algorythmus="modulo"):
        withdraw_count: int

        if algorythmus == "modulo":
            withdraw_count = (self.rods - 1) % 4

        elif algorythmus == "random":
            withdraw_count = random.randint(1, 3)

        self.rods -= withdraw_count
        self.turn = not self.turn

    def user_turn(self, count):
        self.rods -= count
        self.turn = not self.turn

    def update(self, delta_time):
        if self.animation["on_going"]:
            self.animation["counter"] -= delta_time

            self.animation["interpolated_value"] = cubic(0, self.animation["duration"], self.animation["counter"])

            if self.animation["counter"] <= 0:
                self.animation["counter"] = 0
                self.animation["on_going"] = False
                self.animation["interpolated_value"] = 0

    def render(self, screen):
        pass

    def _start_animation(self, count, turn):
        self.animation["on_going"] = True
        self.animation["counter"] = self.animation["duration"]
