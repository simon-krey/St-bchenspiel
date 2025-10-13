import pygame as pg

class Button:
    def __init__(self, pos, text, padding=5, font=pg.font.Font(pg.font.get_default_font())):
        self.pos = pos
        self.text = text
        self.padding = padding

        self.font = font
        self.text_size = self.font.render(self.text, True, pg.Color(0, 0, 0)).size

        self.box_pos = (self.pos[0] - self.padding, self.pos[1] - self.padding)
        self.box_size = (self.text_size[0] + self.padding * 2, self.text_size[1] + self.padding * 2)
        self.roundness = 0.2

        self.pressed = True

    def render(self, screen: pg.Surface):
        if not self.pressed:
            pg.draw.rect(screen, pg.Color(180, 200, 180), (*self.box_pos, *self.box_size))

        else:
            pg.draw.rect(screen, pg.Color(150, 170, 150), (*self.box_pos, *self.box_size))

        screen.blit(self.font.render(self.text, True, pg.Color(0, 0, 0)), self.pos)

    def update(self, mouse_pos, mouse_pressed):
        if self.box_pos[0] < mouse_pos[0] < self.box_pos[0] + self.box_size[0]:
            if self.box_pos[1] < mouse_pos[1] < self.box_pos[1] + self.box_size[1]:
                if mouse_pressed:
                    self.pressed = True
                    return
                
        self.pressed = False
        