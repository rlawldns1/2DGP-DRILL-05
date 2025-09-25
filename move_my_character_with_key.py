from pico2d import *

open_canvas()

background = load_image('TUK_GROUND.png')
boy = load_image('animation_sheet.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
    pass

running = True
frame = 0
x = 400
y = 90

while running:
    clear_canvas()
    background.draw(400, 300)
    boy.clip_draw(frame*100, 300, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x+=5
    y+=5
    delay(0.5)

close_canvas()