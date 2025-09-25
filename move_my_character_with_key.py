from pico2d import *

open_canvas()

background = load_image('TUK_GROUND.png')
boy = load_image('animation_sheet.png')

def handle_events():
    global running
    global dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                dir = 1
            elif event.key == SDLK_LEFT:
                dir = 2
            elif event.key == SDLK_UP:
                dir = 3
        elif event.type == SDL_KEYUP:
            dir = 0

def boy_move():
    global x, y
    global dir
    if dir == 1:
        x += 5
    elif dir == 2:
        x -= 5
    elif dir == 3:
        y += 5

running = True
frame = 0
x = 400
y = 90
dir = 0 # 1:right, 2:left, 3:up, 4:down





while running:
    clear_canvas()
    background.draw(400, 300)
    boy.clip_draw(frame*100, 300, 100, 100, x, y)
    update_canvas()
    handle_events()
    boy_move()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()