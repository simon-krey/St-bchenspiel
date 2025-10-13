import pygame as pg

def rendered_text(text, size=20):
    return pg.font.Font(pg.font.get_default_font(), size=size).render(text, True, pg.Color(0, 0, 0))
