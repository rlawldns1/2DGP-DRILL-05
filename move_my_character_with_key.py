from pico2d import *

open_canvas()

background = load_image('TUK_GROUND.png')
boy = load_image('animation_sheet.png')

running = True

while running:
    clear_canvas()
    background.draw(400, 300)
    update_canvas()
    delay(0.5)

close_canvas()