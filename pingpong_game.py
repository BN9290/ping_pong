from pygame import *

win_width = 700
win_height = 500



window = display.set_mode((win_width, win_height))
display.set_caption("pingpong game")

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((136, 206, 235))
    display.update()

